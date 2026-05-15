# 🚗 Used Car Price Predictor

AI-powered used car price estimation using **9 machine learning models** trained on Indian used car market data.

## Features

- **9 ML Models** running simultaneously: XGBoost, Random Forest, Gradient Boosting, Polynomial Regression, SVR, Linear Regression, Ridge, AdaBoost, Lasso
- **41 input features** covering car specs, engine, dimensions, and location
- **Example presets** for quick testing (Budget / Mid-range / Premium cars)
- **Interactive visualizations** with Plotly charts
- **Confidence intervals** based on model RMSE
- Premium dark-theme UI

## Project Structure

```
vehicle_price_predictor/
├── app.py                    # Main Streamlit app
├── utils/
│   ├── __init__.py
│   ├── predictor.py          # Model loading + prediction
│   ├── preprocess.py         # Feature encoding + scaling
│   └── ui_config.py          # UI presets, CSS, options
├── models/                   # Trained .pkl model files
├── data/                     # Scaler, feature names, encoders
├── requirements.txt
└── README.md
```

## Setup

```bash
# 1. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

App opens at `http://localhost:8501`

## Models & Performance

| Model | R² Score | RMSE |
|-------|----------|------|
| XGBoost | 0.9494 | 0.1714 |
| Random Forest | 0.9464 | 0.1764 |
| Gradient Boosting | 0.9295 | 0.2023 |
| Polynomial Regression | 0.9248 | 0.2089 |
| SVR | 0.9225 | 0.2120 |
| Linear Regression | 0.8701 | 0.2746 |
| Ridge Regression | 0.8701 | 0.2746 |
| AdaBoost | 0.8351 | 0.3094 |
| Lasso Regression | 0.8221 | 0.3213 |

## Notes

- Target variable is `log(listed_price)` — predictions are `exp()`-transformed
- Models trained with scikit-learn 1.6.1 — version is pinned in requirements
- High-cardinality categorical fields use deterministic hash encoding
- Missing models (e.g., `random_forest.pkl`, `xgboost.pkl`) are skipped gracefully
