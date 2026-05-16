"""
Preprocessing module for Used Car Price Predictor.

Handles encoding of categorical features and scaling of all features
to match the pipeline used during model training.

NOTE: The saved label_encoders.pkl has a reference bug — all 20 categorical
columns share the same LabelEncoder object. Instead, we use the correct
alphabetically-sorted mappings that match sklearn's LabelEncoder behavior.
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
    'City', 'Color', 'Engine Type', 'Valve Configuration', 'Gear Box',
    'Drive Type', 'Steering Type', 'Front Brake Type', 'Rear Brake Type',
    'Tyre Type', 'state', 'exterior_color', 'owner_type', 'Fuel Suppy System'
]

NUMERIC_COLS = [
    'myear', 'km', 'No of Cylinder', 'Valves per Cylinder',
    'Turbo Charger', 'Super Charger', 'Length', 'Width', 'Height',
    'Wheel Base', 'Kerb Weight', 'Seats', 'Turning Radius',
    'Acceleration', 'Doors', 'Cargo Volume', 'Alloy Wheel Size',
    'Max Power Delivered', 'Max Power At', 'Max Torque Delivered', 'Max Torque At'
]

# ──────────────────────────────────────────────────────────────────────
# Correct alphabetically-sorted LabelEncoder mappings (matches training)
# ──────────────────────────────────────────────────────────────────────

# 11 values — alphabetical sort
BODY_MAP = {
    'convertible': 0, 'coupe': 1, 'hatchback': 2, 'hyper car': 3,
    'muv': 4, 'minivan': 5, 'pickup truck': 6, 'suv': 7,
    'sedan': 8, 'sports car': 9, 'wagon': 10
}

# 2 values — Automatic(0), Manual(1)
TRANSMISSION_MAP = {
    'automatic': 0, 'manual': 1
}

# 5 values — CNG(0), Diesel(1), Electric(2), Hybrid(3), Petrol(4)
FUEL_MAP = {
    'cng': 0, 'diesel': 1, 'electric': 2, 'hybrid': 3, 'petrol': 4
}

# 5 values — alphabetical
VALVE_CONFIG_MAP = {
    'dohc': 0, 'ohv': 1, 'sohc': 2, 'sv': 3, 'vvt': 4
}

# 11 values — digits sort before letters in Python string sort
GEAR_BOX_MAP = {
    '4': 0, '5': 1, '6': 2, '7': 3, '8': 4, '9': 5,
    'amt': 6, 'cvt': 7, 'dct': 8, 'imt': 9, 'ivt': 10,
    4: 0, 5: 1, 6: 2, 7: 3, 8: 4, 9: 5
}

# 6 values — 2WD(0), 4WD(1), 4x4(2), AWD(3), FWD(4), RWD(5)
DRIVE_TYPE_MAP = {
    '2wd': 0, '4wd': 1, '4x4': 2, 'awd': 3, 'fwd': 4, 'rwd': 5
}

# 2 values — Electric(0), Power(1)
STEERING_MAP = {
    'electric': 0, 'power': 1
}

# 5 values — alphabetical
FRONT_BRAKE_MAP = {
    'ceramic disc': 0, 'disc': 1, 'drum': 2,
    'hydraulic drum': 3, 'ventilated disc': 4
}

REAR_BRAKE_MAP = {
    'ceramic disc': 0, 'disc': 1, 'drum': 2,
    'hydraulic drum': 3, 'ventilated disc': 4
}

# 4 values — alphabetical
TYRE_MAP = {
    'radial tubeless': 0, 'run flat tyres': 1,
    'tube tyres': 2, 'tubeless tyres': 3
}

# 6 values — alphabetical
OWNER_MAP = {
    'first owner': 0, 'fourth & above owner': 1, 'second owner': 2,
    'test drive car': 3, 'third owner': 4, 'unregistered car': 5
}

# 14 values — correct full names from saved LabelEncoder
FUEL_SUPPLY_MAP = {
    'common rail injection': 0, 'diesel direct injection': 1,
    'direct injection': 2, 'distributor-type fuel injection': 3,
    'electric': 4, 'electronic fuel injection': 5,
    'gasoline direct injection': 6, 'gasoline port injection': 7,
    'indirect injection': 8, 'intake port injection': 9,
    'multi-point fuel injection': 10, 'three-phase ac induction motors': 11,
    'turbo intercooled diesel': 12, 'variable valve timing injection': 13,
    # Common abbreviations mapped to correct full-name index
    'mpfi': 10, 'crdi': 0, 'tdi': 12, 'di': 2, 'efi': 5,
    'gdi': 6, 'tfsi': 6, 'sefi': 7, 'pfi': 7, 'idc': 9,
    'carburettor': 3, 'arai certified': 9
}

# Indian states — alphabetical
STATE_MAP = {
    'andhra pradesh': 0, 'arunachal pradesh': 1, 'assam': 2,
    'bihar': 3, 'chandigarh': 4, 'chhattisgarh': 5, 'delhi': 6,
    'goa': 7, 'gujarat': 8, 'haryana': 9, 'himachal pradesh': 10,
    'jammu and kashmir': 11, 'jharkhand': 12, 'karnataka': 13,
    'kerala': 14, 'ladakh': 15, 'madhya pradesh': 16, 'maharashtra': 17,
    'manipur': 18, 'meghalaya': 19, 'mizoram': 20, 'nagaland': 21,
    'odisha': 22, 'puducherry': 23, 'punjab': 24, 'rajasthan': 25,
    'sikkim': 26, 'tamil nadu': 27, 'telangana': 28, 'tripura': 29,
    'uttar pradesh': 30, 'uttarakhand': 31, 'west bengal': 32
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

# Default values matching scaler means
FEATURE_DEFAULTS = {
    'myear': 2016,
    'body': 6,            # SUV area
    'transmission': 1,    # Manual
    'fuel': 4,            # Petrol
    'km': 62533,
    'oem': 21,
    'model': 160,
    'variant': 1793,
    'City': 287,
    'Color': 463,
    'Engine Type': 309,
    'No of Cylinder': 4,
    'Valves per Cylinder': 4,
    'Valve Configuration': 0,  # DOHC
    'Turbo Charger': 0,
    'Super Charger': 0,
    'Length': 4111,
    'Width': 1724,
    'Height': 1577,
    'Wheel Base': 2543,
    'Kerb Weight': 1116,
    'Gear Box': 2,         # '6' -> index 2
    'Drive Type': 4,       # FWD
    'Seats': 5,
    'Steering Type': 1,    # Power
    'Turning Radius': 5.52,
    'Front Brake Type': 2, # Drum
    'Rear Brake Type': 2,  # Drum
    'Acceleration': 13.2,
    'Tyre Type': 3,        # Tubeless Tyres
    'Doors': 5,
    'Cargo Volume': 360,
    'state': 17,           # Maharashtra
    'exterior_color': 463,
    'owner_type': 0,       # First Owner
    'Fuel Suppy System': 10, # Multi-Point Fuel Injection
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
    Uses correct alphabetically-sorted mappings matching sklearn LabelEncoder.
    """
    if value is None or (isinstance(value, str) and value.strip() == ''):
        return FEATURE_DEFAULTS.get(feature_name, 0)

    val_lower = str(value).strip().lower()

    mapping_lookup = {
        'body': BODY_MAP,
        'transmission': TRANSMISSION_MAP,
        'fuel': FUEL_MAP,
        'Valve Configuration': VALVE_CONFIG_MAP,
        'Gear Box': GEAR_BOX_MAP,
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
        # Partial match fallback
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
                feature_vector.append(float(raw_value) if raw_value is not None else 0.0)
        else:
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
