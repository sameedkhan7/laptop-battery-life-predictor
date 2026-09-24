\# 🔋 Laptop Battery Life Predictor



A Machine Learning project that predicts laptop battery life in hours based on hardware specifications, usage conditions, and battery health.



\## 📌 Project Overview



This project uses Machine Learning regression models to estimate laptop battery life.



The project includes:



\- Data analysis and visualization

\- Feature engineering

\- Categorical data encoding

\- Multiple regression models

\- Model evaluation and comparison

\- Trained model saving using Joblib

\- Interactive Streamlit web application



\## 🛠️ Technologies Used



\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Scikit-learn

\- Joblib

\- Streamlit

\- Jupyter Notebook



\## 📊 Dataset



The dataset contains 5,000 laptop records with information such as:



\- Laptop brand

\- Operating system

\- Usage type

\- Battery capacity

\- CPU TDP

\- RAM

\- Screen size

\- Refresh rate

\- Brightness

\- CPU usage

\- GPU usage

\- Wi-Fi and Bluetooth

\- Temperature

\- Battery age

\- Battery health

\- Battery life



\## 🤖 Machine Learning Models



Three regression models were tested:



1\. Linear Regression

2\. Decision Tree Regressor

3\. Random Forest Regressor



\## 📈 Model Performance



| Model | MAE | RMSE | R² Score |

|---|---:|---:|---:|

| Linear Regression | 0.2872 | 0.3893 | 89.49% |

| Random Forest | 0.3488 | 0.4631 | 85.31% |

| Decision Tree | 0.5139 | 0.6901 | 66.99% |



Based on the test-set metrics, Linear Regression achieved the highest R² score among the three tested models.



\## 🖥️ Streamlit Application



The project includes an interactive Streamlit application where users can enter laptop specifications and receive a predicted battery-life estimate.



\## ▶️ How to Run



Clone the repository:



```bash

git clone https://github.com/sameedkhan7/laptop-battery-life-predictor.git

