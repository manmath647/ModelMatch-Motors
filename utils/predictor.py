"""
Model loading and prediction module for Used Car Price Predictor.

Loads 9 trained ML models and runs predictions simultaneously.
Target variable is log(listed_price) — all outputs are exp()-transformed.
"""

import os
import numpy as np
import pickle
import warnings
import joblib    

warnings.filterwarnings('ignore')

# ──────────────────────────────────────────────────────────────────────
# Model configurations with training metrics
# ──────────────────────────────────────────────────────────────────────
MODEL_CONFIGS = {
    'XGBoost': {
        'path': 'models/xgboost.pkl',
        'r2': 0.9494,
        'rmse': 0.1714,
        'family': 'Ensemble',
        'color': '#10B981'
    },
    'Random Forest': {
        'path': 'models/random_forest.pkl',
        'r2': 0.9464,
        'rmse': 0.1764,
        'family': 'Ensemble',
        'color': '#059669'
    },
    'Gradient Boosting': {
        'path': 'models/gradient_boosting.pkl',
        'r2': 0.9295,
        'rmse': 0.2023,
        'family': 'Ensemble',
        'color': '#34D399'
    },
    'Polynomial Regression': {
        'path': 'models/polynomial_regression.pkl',
        'r2': 0.9248,
        'rmse': 0.2089,
        'family': 'Regression',
        'color': '#6366F1'
    },
    'SVR': {
        'path': 'models/svr.pkl',
        'r2': 0.9225,
        'rmse': 0.2120,
        'family': 'Kernel',
        'color': '#8B5CF6'
    },
    'Linear Regression': {
        'path': 'models/linear_regression.pkl',
        'r2': 0.8701,
        'rmse': 0.2746,
        'family': 'Regression',
        'color': '#818CF8'
    },
    'Ridge Regression': {
        'path': 'models/ridge_regression.pkl',
        'r2': 0.8701,
        'rmse': 0.2746,
        'family': 'Regression',
        'color': '#A78BFA'
    },
    'AdaBoost': {
        'path': 'models/adaboost.pkl',
        'r2': 0.8351,
        'rmse': 0.3094,
        'family': 'Ensemble',
        'color': '#6EE7B7'
    },
    'Lasso Regression': {
        'path': 'models/lasso_regression.pkl',
        'r2': 0.8221,
        'rmse': 0.3213,
        'family': 'Regression',
        'color': '#C4B5FD'
    },
}


def get_available_models():
    """Return dict of models that have their .pkl files present."""
    available = {}
    for name, config in MODEL_CONFIGS.items():
        if os.path.exists(config['path']):
            available[name] = config
    return available


# Change this import at the top:
      # add this
# import pickle       # remove or keep (not needed for models)

# Change the load_model function:
def load_model(model_path):
    return joblib.load(model_path)   # ✅ correct


def predict_single(model, X_scaled):
    """
    Run prediction with a single model.

    Parameters
    ----------
    model : trained sklearn/xgboost model
    X_scaled : np.ndarray of shape (1, 41)

    Returns
    -------
    tuple : (log_prediction, actual_price)
    """
    log_pred = model.predict(X_scaled)[0]
    price = np.exp(log_pred)
    return log_pred, price


def predict_all(X_scaled, loaded_models):
    """
    Run predictions through all loaded models.

    Parameters
    ----------
    X_scaled : np.ndarray of shape (1, 41)
        Scaled feature vector.
    loaded_models : dict
        {model_name: model_object} — pre-loaded models.

    Returns
    -------
    dict : {model_name: {log_prediction, price, r2, rmse, family, color, rank}}
    """
    results = {}

    for name, model in loaded_models.items():
        config = MODEL_CONFIGS[name]
        try:
            log_pred, price = predict_single(model, X_scaled)
            results[name] = {
                'log_prediction': float(log_pred),
                'price': float(price),
                'r2': config['r2'],
                'rmse': config['rmse'],
                'family': config['family'],
                'color': config['color']
            }
        except Exception as e:
            results[name] = {
                'log_prediction': None,
                'price': None,
                'r2': config['r2'],
                'rmse': config['rmse'],
                'family': config['family'],
                'color': config['color'],
                'error': str(e)
            }

    # Rank by R² score (descending)
    sorted_names = sorted(
        [n for n in results if results[n]['price'] is not None],
        key=lambda n: results[n]['r2'],
        reverse=True
    )
    for rank, name in enumerate(sorted_names, 1):
        results[name]['rank'] = rank

    return results


def get_confidence_range(price, rmse):
    """
    Compute a pseudo-confidence interval using training RMSE.

    Since the model predicts log(price), the RMSE is in log-space.
    We compute: price * exp(-rmse) to price * exp(+rmse)
    """
    lower = price * np.exp(-rmse)
    upper = price * np.exp(rmse)
    return float(lower), float(upper)


def format_price_inr(price):
    """Format price in Indian Rupee notation (₹X,XX,XXX)."""
    if price is None:
        return "N/A"
    price = round(price)
    s = str(price)
    if len(s) <= 3:
        return f"₹{s}"

    # Last 3 digits
    result = s[-3:]
    s = s[:-3]

    # Group remaining in pairs
    while s:
        result = s[-2:] + ',' + result
        s = s[:-2]

    return f"₹{result}"
