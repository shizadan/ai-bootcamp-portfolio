# 🫀 Heart Disease Risk Prediction

A machine learning web app that predicts a patient's risk of heart disease based on clinical attributes, deployed with Streamlit.

🔗 **Live App:** [Insert your Streamlit URL here]

## Overview
This project uses a dataset of 1,025 patient records with 13 clinical features (age, blood pressure, cholesterol, max heart rate, ECG results, etc.) to predict the presence of heart disease.

## Dataset
- **1,025 rows, 13 features, 1 target**
- Target: `1` = heart disease present, `0` = no heart disease
- No missing values

## Approach
1. Exploratory Data Analysis (distributions, correlations, class balance)
2. Preprocessing: feature scaling with `StandardScaler`
3. Models trained: Logistic Regression & Random Forest
4. Evaluation: Accuracy, ROC-AUC, Confusion Matrix

## Results
| Model | Accuracy | ROC-AUC |
|---|---|---|
| Logistic Regression | [add score] | [add score] |
| Random Forest | [add score] | [add score] |

## Tech Stack
- Python, pandas, scikit-learn
- Streamlit (deployment)
- joblib (model persistence)

## How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Disclaimer
This tool is for educational purposes only and does not constitute medical advice.
