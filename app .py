# app.py
import streamlit as st
import joblib
import numpy as np

model = joblib.load('heart_disease_model.pkl')

st.title("Heart Disease Predictor")

# Example inputs
age = st.number_input("Age", 20, 100)
chol = st.number_input("Cholesterol", 100, 400)
sex = st.selectbox("Sex", ['M', 'F'])

# Add more features...

if st.button("Predict"):
    # Dummy encoding, update this based on your actual model input
    X_new = np.array([[age, chol, 1 if sex == 'M' else 0, ...]])
    pred = model.predict(X_new)
    st.success("Heart Disease Risk: " + ("Yes" if pred[0] == 1 else "No"))
