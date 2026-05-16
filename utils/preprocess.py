"""
Preprocessing module for Used Car Price Predictor.

Handles encoding of categorical features and scaling of all features
to match the pipeline used during model training.

NOTE: The saved label_encoders.pkl has a reference bug — all 20 categorical
columns share the same LabelEncoder object. Instead, we use deterministic
hash encoding for high-cardinality fields and hardcoded mappings for
low-cardinality fields.
"""

import numpy as np
import pickle
import os
import hashlib

# ──────────────────────────────────────────────────────────────────────
# Feature order — MUST match exactly what the scaler was fit on
# ──────────────────────────────────────────────────────────────────────
FEATURE_ORDER = [
    'myear', 'body', 'transmission', 'fuel', 'km', 'oem', 'model', 'variant',
    'City', 'Color', 'Engine Type', 'No of Cylinder', 'Valves per Cylinder',
    'Valve Configuration', 'Turbo Charger', 'Super Charger', 'Length', 'Width',
    'Height', 'Wheel Base', 'Kerb Weight', 'Gear Box', 'Drive Type', 'Seats',
    'Steering Type', 'Turning Radius', 'Front Brake Type', 'Rear Brake Type',
    'Acceleration', 'Tyre Type', 'Doors', 'Cargo Volume', 'state',
    'exterior_color', 'owner_type', 'Fuel Suppy System', 'Alloy Wheel Size',
    'Max Power Delivered', 'Max Power At', 'Max Torque Delivered', 'Max Torque At'
]

CATEGORICAL_COLS = [
    'body', 'transmission', 'fuel', 'oem', 'model', 'variant',
    'City', 'Color', 'Engine Type', 'Valve Configuration',
    # ✅ 'Gear Box' removed — it's numeric (number of gears)
    'Drive Type', 'Steering Type', 'Front Brake Type', 'Rear Brake Type',
    'Tyre Type', 'state', 'exterior_color', 'owner_type', 'Fuel Suppy System'
]

NUMERIC_COLS = [
    'myear', 'km', 'No of Cylinder', 'Valves per Cylinder',
    'Turbo Charger', 'Super Charger', 'Length', 'Width', 'Height',
    'Wheel Base', 'Kerb Weight', 'Seats', 'Turning Radius',
    'Acceleration', 'Doors', 'Cargo Volume', 'Alloy Wheel Size',
    'Max Power Delivered', 'Max Power At', 'Max Torque Delivered', 'Max Torque At',
    'Gear Box'  # ✅ added here — just a number (4, 5, 6...)
]

# ──────────────────────────────────────────────────────────────────────
# Low-cardinality hardcoded mappings
# ──────────────────────────────────────────────────────────────────────
BODY_MAP = {
    'convertible': 0, 'coupe': 1, 'hatchback': 2, 'hyper car': 3,
    'minivan': 4, 'muv': 5, 'pickup truck': 6, 'sedan': 7,
    'sports car': 8, 'suv': 9, 'super car': 10, 'wagon': 11,
    'micro van': 12, 'compact suv': 13
}

TRANSMISSION_MAP = {'manual': 0, 'automatic': 1}

FUEL_MAP = {
    'petrol': 0, 'diesel': 1, 'cng': 2, 'electric': 3,
    'hybrid': 4, 'lpg': 5
}

VALVE_CONFIG_MAP = {
    'dohc': 0, 'ohv': 1, 'sohc': 2, 'sv': 3
}

DRIVE_TYPE_MAP = {
    '4wd': 0, 'awd': 1, 'fwd': 2, 'rwd': 3, '4x4': 4
}

STEERING_MAP = {
    'electric': 0, 'manual': 1, 'power': 2
}

FRONT_BRAKE_MAP = {
    'caliper disc': 0, 'disc': 1, 'drum': 2,
    'ventilated disc': 3, 'ceramic disc': 4
}

REAR_BRAKE_MAP = {
    'caliper disc': 0, 'disc': 1, 'drum': 2,
    'ventilated disc': 3, 'ceramic disc': 4
}

TYRE_MAP = {
    'run flat tyres': 0, 'tube tyres': 1, 'tubeless tyres': 2,
    'tube type': 3, 'radial': 4
}

OWNER_MAP = {
    'first owner': 0, 'second owner': 1, 'third owner': 2,
    'fourth owner': 3, 'fourth owner+': 3, 'unregistered car': 4
}

FUEL_SUPPLY_MAP = {
    'arai certified': 0, 'carburettor': 1, 'common rail injection': 2,
    'crdi': 3, 'di': 4, 'direct injection': 5, 'distributor type': 6,
    'efi': 7, 'electronic fuel injection': 8, 'idc': 9,
    'mpfi': 10, 'pfi': 11, 'sefi': 12, 'tdi': 13, 'tfsi': 14
}

# Indian states mapping
STATE_MAP = {
    'andhra pradesh': 0, 'arunachal pradesh': 1, 'assam': 2,
    'bihar': 3, 'chhattisgarh': 4, 'delhi': 5, 'goa': 6,
    'gujarat': 7, 'haryana': 8, 'himachal pradesh': 9,
    'jharkhand': 10, 'karnataka': 11, 'kerala': 12,
    'madhya pradesh': 13, 'maharashtra': 14, 'manipur': 15,
    'meghalaya': 16, 'mizoram': 17, 'nagaland': 18,
    'odisha': 19, 'punjab': 20, 'rajasthan': 21,
    'sikkim': 22, 'tamil nadu': 23, 'telangana': 24,
    'tripura': 25, 'uttar pradesh': 26, 'uttarakhand': 27,
    'west bengal': 28, 'chandigarh': 29, 'puducherry': 30,
    'jammu and kashmir': 31, 'ladakh': 32
}

# Approximate unique counts for high-cardinality fields (for hash encoding)
HIGH_CARDINALITY_SIZES = {
    'oem': 42,
    'model': 321,
    'variant': 3586,
    'City': 573,
    'Color': 927,
    'Engine Type': 619,
    'exterior_color': 927
}

# Default mean values for each feature (from scaler) — used as fallback
FEATURE_DEFAULTS = {
    'myear': 2017,
    'body': 6,
    'transmission': 1,
    'fuel': 3,
    'km': 45000,
    'oem': 21,
    'model': 160,
    'variant': 1793,
    'City': 287,
    'Color': 463,
    'Engine Type': 309,
    'No of Cylinder': 4,
    'Valves per Cylinder': 4,
    'Valve Configuration': 1,
    'Turbo Charger': 0,
    'Super Charger': 0,
    'Length': 4110,
    'Width': 1724,
    'Height': 1576,
    'Wheel Base': 2543,
    'Kerb Weight': 1116,
    'Gear Box': 5,         # ✅ fixed: default is 5 gears, not encoded index
    'Drive Type': 4,
    'Seats': 5,
    'Steering Type': 1,
    'Turning Radius': 5.52,
    'Front Brake Type': 2,
    'Rear Brake Type': 3,
    'Acceleration': 13.2,
    'Tyre Type': 3,
    'Doors': 5,
    'Cargo Volume': 360,
    'state': 17,
    'exterior_color': 463,
    'owner_type': 2,
    'Fuel Suppy System': 6,
    'Alloy Wheel Size': 15.66,
    'Max Power Delivered': 101,
    'Max Power At': 5127,
    'Max Torque Delivered': 176,
    'Max Torque At': 3177,
}


def hash_encode(val, n_classes):
    """Deterministic hash encoding for high-cardinality categorical features."""
    val_bytes = str(val).strip().lower().encode('utf-8')
    hash_int = int(hashlib.md5(val_bytes).hexdigest(), 16)
    return hash_int % n_classes


def encode_categorical(feature_name, value):
    """
    Encode a single categorical feature value to an integer.

    Uses hardcoded mappings for low-cardinality features and
    deterministic hash encoding for high-cardinality features.
    """
    if value is None or (isinstance(value, str) and value.strip() == ''):
        return FEATURE_DEFAULTS.get(feature_name, 0)

    val_lower = str(value).strip().lower()

    mapping_lookup = {
        'body': BODY_MAP,
        'transmission': TRANSMISSION_MAP,
        'fuel': FUEL_MAP,
        'Valve Configuration': VALVE_CONFIG_MAP,
        'Drive Type': DRIVE_TYPE_MAP,
        'Steering Type': STEERING_MAP,
        'Front Brake Type': FRONT_BRAKE_MAP,
        'Rear Brake Type': REAR_BRAKE_MAP,
        'Tyre Type': TYRE_MAP,
        'owner_type': OWNER_MAP,
        'Fuel Suppy System': FUEL_SUPPLY_MAP,
        'state': STATE_MAP,
    }

    if feature_name in mapping_lookup:
        m = mapping_lookup[feature_name]
        if val_lower in m:
            return m[val_lower]
        if value in m:
            return m[value]
        for k, v in m.items():
            if str(k) in val_lower or val_lower in str(k):
                return v
        return FEATURE_DEFAULTS.get(feature_name, 0)

    # High-cardinality: hash encode
    if feature_name in HIGH_CARDINALITY_SIZES:
        return hash_encode(value, HIGH_CARDINALITY_SIZES[feature_name])

    return FEATURE_DEFAULTS.get(feature_name, 0)


def load_scaler(data_dir='data'):
    """Load the fitted StandardScaler from pickle."""
    scaler_path = os.path.join(data_dir, 'scaler.pkl')
    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)
    return scaler


def encode_and_scale(input_dict, scaler):
    """
    Convert user input dictionary to a scaled numpy array ready for prediction.

    Parameters
    ----------
    input_dict : dict
        Raw user input with keys matching FEATURE_ORDER.
    scaler : sklearn StandardScaler
        The fitted scaler loaded from scaler.pkl.

    Returns
    -------
    np.ndarray of shape (1, 41)
        Scaled feature vector.
    """
    feature_vector = []

    for feat in FEATURE_ORDER:
        raw_value = input_dict.get(feat, None)

        if feat in CATEGORICAL_COLS:
            encoded = encode_categorical(feat, raw_value)
            feature_vector.append(float(encoded))
        elif feat in ('Turbo Charger', 'Super Charger'):
            if isinstance(raw_value, str):
                feature_vector.append(1.0 if raw_value.strip().lower() in ('yes', '1', 'true') else 0.0)
            else:
                feature_vector.append(float(raw_value) if raw_value else 0.0)
        else:
            # Numeric features (including Gear Box)
            if raw_value is not None and raw_value != '':
                try:
                    feature_vector.append(float(raw_value))
                except (ValueError, TypeError):
                    feature_vector.append(float(FEATURE_DEFAULTS.get(feat, 0)))
            else:
                feature_vector.append(float(FEATURE_DEFAULTS.get(feat, 0)))

    X = np.array(feature_vector).reshape(1, -1)
    X_scaled = scaler.transform(X)
    return X_scaled
