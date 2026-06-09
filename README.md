# 🚗 Car Price Prediction — End-to-End Machine Learning Project

**Bootcamp Assignment 2 | Linear Regression**
**Author:** Dan Shizamuayi Shina

---

## Project Overview

This project builds a machine learning model that predicts the selling price of used cars based on their features. It was developed as a complete end-to-end regression project covering data exploration, preprocessing, model training, evaluation, and business insights.

The dataset contains 301 records of used cars with features such as fuel type, transmission, kilometres driven, age, and present showroom price.

---

## Dataset

| Column | Description |
|---|---|
| Car_Name | Model name |
| Year | Year of manufacture |
| Selling_Price | Target — price sold |
| Present_Price | Current ex-showroom price |
| Kms_Driven | Total kilometres driven |
| Fuel_Type | Petrol / Diesel / CNG |
| Seller_Type | Dealer or Individual |
| Transmission | Manual or Automatic |
| Owner | Number of previous owners |

---

## Repository Structure

- `Car_Price_Prediction.ipynb` — Main notebook
- `car_data_cleaned.csv` — Preprocessed dataset
- `README.md` — This file

---

## Steps Taken

1. **Problem Understanding** — Defined the business goal and identified features vs target variable
2. **EDA** — Checked missing values, summary statistics, visualised distributions and relationships
3. **Preprocessing** — Dropped Car_Name, engineered Car_Age from Year, label encoded categorical variables
4. **Model Building** — Trained a Linear Regression model on an 80/20 train-test split
5. **Evaluation** — Assessed with MAE, RMSE, and R² Score; plotted Actual vs Predicted and Residuals
6. **Predictions** — Generated predictions for 5 sample cars
7. **Insights** — Interpreted feature coefficients and surfaced surprising findings from the data

---

## How to Run the Notebook

1. Go to colab.research.google.com
2. Click File → Upload notebook and select Car_Price_Prediction.ipynb
3. Run the first cell to import all libraries
4. When you reach the data loading cell, authenticate your Google Drive when prompted
5. Run all remaining cells in order via Runtime → Run all

---

## Key Results

| Metric | Score |
|---|---|
| MAE | 1.22 |
| RMSE | 1.88 |
| R² Score | 0.85 |

The model explains approximately 85% of variance in used car selling prices.

---

## Top Insights

- Present Price is the strongest predictor of resale value
- Car Age significantly reduces selling price — older cars sell for less
- Diesel and Automatic cars command a price premium
- High mileage lowers price but has less impact than age
- Linear Regression predicted a negative price for the oldest car — a known limitation when extrapolating beyond training data
