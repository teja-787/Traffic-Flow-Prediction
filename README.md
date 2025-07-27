# MATHS-AND-DSA

# Traffic Prediction Using Machine Learning-sem2 project

## Project Overview

This project predicts **future traffic flow** using machine learning models. It includes a **real-time prediction dashboard** built with Streamlit.

## Dataset

- **Source**: Provided CSV file (`Traffic.csv`)
- **Features Used**: Time-based traffic count data
- **Target Variable**: Future traffic count (Next 15 min)

## Machine Learning Models Implemented

1️⃣ **Linear Regression**
2️⃣ **Random Forest Regressor** ✅ (Best Model)
3️⃣ **LSTM Neural Network**

### **Model Performance Comparison**

| Model                 | MAE       | RMSE      | R² Score |
| --------------------- | --------- | --------- | -------- |
| **Linear Regression** | 22.05     | 30.91     | 0.74     |
| **Random Forest** ✅  | **17.07** | **22.58** | **0.86** |
| **LSTM**              | 29.33     | 38.41     | 0.59     |

## 🎛️ Real-Time Prediction Dashboard

A **web application** using **Streamlit** allows users to:
✅ Input traffic data
✅ Get real-time predictions (Next 15 min traffic count)
✅ Visualize past trends

## 🚀 How to Run the Project

1️⃣ Install dependencies:

```bash
pip install streamlit tensorflow keras pandas numpy scikit-learn matplotlib seaborn
```

2️⃣ Run the Streamlit app:

```bash
streamlit run traffic_dashboard.py
```

THIS IS THE DASHBOARD WHERE WE CAN PREDICT FUTURE VEHICLE COUNT BY GIVING THE PREVIOUS TRAFFIC FLOW AND OUR RANDOM FOREST MODEL PREDICTS IT CORRECTLY

![image](https://github.com/user-attachments/assets/08282396-c828-445b-ad50-cb8b7d303c84)

## Project Files

- `traffic_dashboard.py` → Streamlit Web App
- `random_forest_model.pkl` → Best ML Model (Saved)
- `scaler.pkl` → Data Preprocessing Model
- `Traffic.csv` → Dataset

---

### ⭐ **Contributors**

📌 Teja prakash
📌 Surya
📌 Tej krishna
📌 Ankith
