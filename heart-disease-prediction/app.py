import streamlit as st
import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, 'heart_disease_model.pkl'))
scaler = joblib.load(os.path.join(BASE_DIR, 'scaler.pkl'))

st.set_page_config(page_title="Heart Disease Risk Predictor", page_icon="🫀", layout="centered")

st.markdown("""
    <div style='text-align: center; padding: 1.5rem 0;'>
        <h1 style='color: #B91C1C; margin-bottom: 0;'>🫀 Heart Disease Risk Predictor</h1>
        <p style='color: #6B7280; font-size: 1.05rem;'>
            Machine learning–based clinical risk assessment tool
        </p>
    </div>
    <hr style='margin-bottom: 2rem;'>
""", unsafe_allow_html=True)

st.subheader("Patient Information")

col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", 20, 100, 50)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 220, 120)
    chol = st.number_input("Cholesterol (mg/dl)", 100, 600, 200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    restecg = st.selectbox("Resting ECG (0-2)", [0, 1, 2])

with col2:
    thalach = st.number_input("Max Heart Rate Achieved", 60, 220, 150)
    exang = st.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 10.0, 1.0, step=0.1)
    slope = st.selectbox("Slope of Peak Exercise ST (0-2)", [0, 1, 2])
    ca = st.selectbox("Major Vessels Colored (0-3)", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia (0-3)", [0, 1, 2, 3])

st.markdown("<br>", unsafe_allow_html=True)

if st.button("Predict Risk", use_container_width=True, type="primary"):
    sex_val = 1 if sex == "Male" else 0
    input_df = pd.DataFrame([[age, sex_val, cp, trestbps, chol, fbs, restecg,
                               thalach, exang, oldpeak, slope, ca, thal]],
                            columns=['age','sex','cp','trestbps','chol','fbs',
                                     'restecg','thalach','exang','oldpeak',
                                     'slope','ca','thal'])
    input_scaled = scaler.transform(input_df)
    pred = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1]

    st.markdown("<br>", unsafe_allow_html=True)

    if pred == 1:
        st.markdown(f"""
            <div style='background-color:#FEF2F2; border:1px solid #FCA5A5; border-radius:10px; padding:1.5rem; text-align:center;'>
                <h3 style='color:#B91C1C; margin:0;'>⚠️ Elevated Risk Detected</h3>
                <p style='font-size:1.1rem; margin-top:0.5rem;'>Estimated probability: <b>{prob:.1%}</b></p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style='background-color:#F0FDF4; border:1px solid #86EFAC; border-radius:10px; padding:1.5rem; text-align:center;'>
                <h3 style='color:#15803D; margin:0;'>✅ Low Risk</h3>
                <p style='font-size:1.1rem; margin-top:0.5rem;'>Estimated probability: <b>{prob:.1%}</b></p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)
st.caption("⚠️ This tool is for educational purposes only and does not constitute medical advice. Always consult a healthcare professional.")
