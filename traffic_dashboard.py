import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler

# Load the trained Random Forest model
rf_model = pickle.load(open("random_forest_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Streamlit UI
st.title("🚦 Real-Time Traffic Prediction Dashboard")

# User Inputs
time_input = st.time_input("Select Time (HH:MM)")
day_input = st.selectbox("Select Day of the Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
lag_15 = st.number_input("Enter Traffic Count (15 min ago)", min_value=0)
lag_30 = st.number_input("Enter Traffic Count (30 min ago)", min_value=0)
lag_45 = st.number_input("Enter Traffic Count (45 min ago)", min_value=0)

# Convert time to minutes from midnight
minutes = time_input.hour * 60 + time_input.minute

# Create input features
day_columns = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_values = [1 if day == day_input else 0 for day in day_columns]

input_data = np.array([minutes] + day_values[1:] + [lag_15, lag_30, lag_45]).reshape(1, -1)

# Normalize data
input_data_scaled = scaler.transform(input_data)

# Predict
if st.button("Predict Traffic Count"):
    prediction = rf_model.predict(input_data_scaled)[0]
    st.success(f"🚗 Predicted Traffic Count (Next 15 min): {prediction:.2f}")


import pickle

# Save the trained Random Forest model
pickle.dump(rf_model, open("random_forest_model.pkl", "wb"))

# Save the MinMaxScaler
pickle.dump(scaler, open("scaler.pkl", "wb"))
