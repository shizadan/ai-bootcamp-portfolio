---

## How to Run the Notebook

### Option 1 — Google Colab (Recommended)

1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Click **File → Upload notebook** and select `Car_Price_Prediction.ipynb`
3. Run **Cell 1** to import all libraries
4. When you reach the data loading cell, authenticate your Google Drive when prompted
5. Run all remaining cells in order (`Runtime → Run all`)

### Option 2 — Local (Jupyter)

```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn jupyter

# Launch notebook
jupyter notebook Car_Price_Prediction.ipynb
```

---

## Key Results

| Metric | Score |
|---|---|
| MAE | 1.22 Lakhs ₹ |
| RMSE | 1.88 Lakhs ₹ |
| R² Score | 0.85 |

The model explains approximately **85% of variance** in used car prices.

---

## Top Insights

- **Present Price** is the strongest predictor of resale value
- **Car Age** significantly reduces selling price — older cars sell for less
- **Diesel & Automatic** cars command a price premium
- **High mileage** lowers price but has less impact than age
- **Linear Regression** predicted a negative price for the oldest car — a known limitation when extrapolating beyond training data
