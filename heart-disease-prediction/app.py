import streamlit as st
import pandas as pd
import joblib

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, 'heart_disease_model.pkl'))
scaler = joblib.load(os.path.join(BASE_DIR, 'scaler.pkl'))

st.title("❤️ Heart Disease Prediction")
st.write("Enter patient details to predict heart disease risk.")

age = st.number_input("Age", 20, 100, 50)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", 80, 220, 120)
chol = st.number_input("Cholesterol", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting ECG", [0, 1, 2])
thalach = st.number_input("Max Heart Rate", 60, 220, 150)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 10.0, 1.0, step=0.1)
slope = st.selectbox("Slope", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels", [0, 1, 2, 3])
thal = st.selectbox("Thal", [0, 1, 2, 3])

if st.button("Predict"):
    sex_val = 1 if sex == "Male" else 0
    input_df = pd.DataFrame([[age, sex_val, cp, trestbps, chol, fbs, restecg,
                               thalach, exang, oldpeak, slope, ca, thal]],
                            columns=['age','sex','cp','trestbps','chol','fbs',
                                     'restecg','thalach','exang','oldpeak',
                                     'slope','ca','thal'])
    input_scaled = scaler.transform(input_df)
    pred = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1]

    if pred == 1:
        st.error(f"⚠️ Heart Disease Detected — Probability: {prob:.2%}")
    else:
        st.success(f"✅ No Heart Disease — Probability: {prob:.2%}")
