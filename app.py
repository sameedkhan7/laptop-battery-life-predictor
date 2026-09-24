import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("battery_life_model.pkl")

# Load feature columns
feature_columns = joblib.load("feature_columns.pkl")

# Page configuration
st.set_page_config(
    page_title="Laptop Battery Life Predictor",
    page_icon="🔋",
    layout="wide"
)

# Title
st.title("🔋 Laptop Battery Life Predictor")

st.write(
    "Predict laptop battery backup using Machine Learning."
)

st.divider()



st.subheader("💻 Laptop Information")

col1, col2 = st.columns(2)

with col1:

    brand = st.selectbox(
        "Laptop Brand",
        ["Acer", "Apple", "ASUS", "Dell", "HP", "Lenovo", "MSI"]
    )

    os = st.selectbox(
        "Operating System",
        ["Windows", "Linux", "macOS"]
    )

    usage_type = st.selectbox(
        "Usage Type",
        ["Office", "Coding", "Gaming", "Video", "Browsing"]
    )



    battery_capacity = st.number_input(
        "Battery Capacity (Wh)",
        min_value=30.0,
        max_value=100.0,
        value=55.0
    )

    cpu_tdp = st.number_input(
        "CPU TDP (W)",
        min_value=8.0,
        max_value=65.0,
        value=25.0
    )

    ram = st.selectbox(
        "RAM (GB)",
        [4, 8, 16, 32, 64]
    )

    screen_size = st.number_input(
        "Screen Size (inch)",
        min_value=11.6,
        max_value=17.3,
        value=15.0
    )




with col2:



    refresh_rate = st.selectbox(
        "Refresh Rate (Hz)",
        [60, 75, 90, 120, 144, 165, 240]
    )

    brightness = st.slider(
        "Brightness (%)",
        0,
        100,
        60
    )

    cpu_usage = st.slider(
        "CPU Usage (%)",
        0,
        100,
        40
    )

    gpu_usage = st.slider(
        "GPU Usage (%)",
        0,
        100,
        10
    )

    wifi = st.selectbox(
        "Wi-Fi",
        ["ON", "OFF"]
    )

    bluetooth = st.selectbox(
        "Bluetooth",
        ["ON", "OFF"]
    )

    temperature = st.number_input(
        "Temperature (°C)",
        min_value=28.0,
        max_value=90.0,
        value=45.0
    )

    battery_age = st.number_input(
        "Battery Age (months)",
        min_value=0,
        max_value=100,
        value=12
    )

    battery_health = st.slider(
        "Battery Health (%)",
        55,
        100,
        90
    )   



st.divider()

if st.button("🔮 Predict Battery Life", type="primary"):

    # Numerical inputs
    input_data = pd.DataFrame({
        "battery_capacity_wh": [battery_capacity],
        "cpu_tdp_w": [cpu_tdp],
        "ram_gb": [ram],
        "screen_size_inch": [screen_size],
        "refresh_rate_hz": [refresh_rate],
        "brightness_percent": [brightness],
        "cpu_usage_percent": [cpu_usage],
        "gpu_usage_percent": [gpu_usage],
        "wifi_on": [1 if wifi == "ON" else 0],
        "bluetooth_on": [1 if bluetooth == "ON" else 0],
        "temperature_c": [temperature],
        "battery_age_months": [battery_age],
        "battery_health_percent": [battery_health]
    })

    # Categorical inputs
    categorical_data = pd.DataFrame({
        "brand": [brand],
        "os": [os],
        "usage_type": [usage_type]
    })

    # One-hot encoding
    categorical_data = pd.get_dummies(
        categorical_data,
        drop_first=True
    )

    # Combine numerical + categorical data
    input_data = pd.concat(
        [input_data, categorical_data],
        axis=1
    )

    # Match training columns
    input_data = input_data.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Show result
    st.subheader("🔋 Prediction Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Predicted Battery Life",
            f"{prediction:.2f} Hours"
        )

    with col2:
        st.metric(
            "Battery Health",
            f"{battery_health}%"
        )

    st.success(
        f"Your laptop is predicted to provide approximately "
        f"{prediction:.2f} hours of battery backup."
    )