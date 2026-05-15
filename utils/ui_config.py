"""UI configuration: example presets, CSS styles, and constants."""

EXAMPLES = {
    "-- Select Example --": None,
    "2019 Maruti Swift Petrol (Budget)": {
        'myear': 2019, 'body': 'Hatchback', 'transmission': 'Manual',
        'fuel': 'Petrol', 'km': 45000, 'oem': 'Maruti Suzuki',
        'model': 'Swift', 'variant': 'VXI', 'City': 'Mumbai',
        'state': 'Maharashtra', 'Color': 'White', 'exterior_color': 'White',
        'owner_type': 'First Owner', 'Engine Type': 'K12M',
        'No of Cylinder': 4, 'Valves per Cylinder': 4,
        'Valve Configuration': 'DOHC', 'Turbo Charger': 'No',
        'Super Charger': 'No', 'Fuel Suppy System': 'MPFI',
        'Max Power Delivered': 82.0, 'Max Power At': 6000,
        'Max Torque Delivered': 113.0, 'Max Torque At': 4200,
        'Acceleration': 11.5, 'Length': 3840, 'Width': 1735,
        'Height': 1530, 'Wheel Base': 2450, 'Kerb Weight': 865,
        'Cargo Volume': 268, 'Gear Box': 5, 'Drive Type': 'FWD',
        'Seats': 5, 'Doors': 5, 'Steering Type': 'Power',
        'Turning Radius': 4.8, 'Front Brake Type': 'Disc',
        'Rear Brake Type': 'Drum', 'Tyre Type': 'Tubeless Tyres',
        'Alloy Wheel Size': 15
    },
    "2021 Hyundai Creta Diesel (Mid-range)": {
        'myear': 2021, 'body': 'SUV', 'transmission': 'Automatic',
        'fuel': 'Diesel', 'km': 28000, 'oem': 'Hyundai',
        'model': 'Creta', 'variant': 'SX', 'City': 'Delhi',
        'state': 'Delhi', 'Color': 'Black', 'exterior_color': 'Black',
        'owner_type': 'First Owner', 'Engine Type': 'U2 CRDi',
        'No of Cylinder': 4, 'Valves per Cylinder': 4,
        'Valve Configuration': 'DOHC', 'Turbo Charger': 'Yes',
        'Super Charger': 'No', 'Fuel Suppy System': 'Common Rail Injection',
        'Max Power Delivered': 115.0, 'Max Power At': 4000,
        'Max Torque Delivered': 250.0, 'Max Torque At': 1500,
        'Acceleration': 11.0, 'Length': 4300, 'Width': 1790,
        'Height': 1635, 'Wheel Base': 2610, 'Kerb Weight': 1480,
        'Cargo Volume': 433, 'Gear Box': 6, 'Drive Type': 'FWD',
        'Seats': 5, 'Doors': 5, 'Steering Type': 'Electric',
        'Turning Radius': 5.3, 'Front Brake Type': 'Disc',
        'Rear Brake Type': 'Disc', 'Tyre Type': 'Tubeless Tyres',
        'Alloy Wheel Size': 17
    },
    "2020 Toyota Innova Crysta (Premium)": {
        'myear': 2020, 'body': 'MUV', 'transmission': 'Automatic',
        'fuel': 'Diesel', 'km': 55000, 'oem': 'Toyota',
        'model': 'Innova Crysta', 'variant': 'GX AT', 'City': 'Bangalore',
        'state': 'Karnataka', 'Color': 'Silver', 'exterior_color': 'Silver',
        'owner_type': 'First Owner', 'Engine Type': '2GD-FTV',
        'No of Cylinder': 4, 'Valves per Cylinder': 4,
        'Valve Configuration': 'DOHC', 'Turbo Charger': 'Yes',
        'Super Charger': 'No', 'Fuel Suppy System': 'Common Rail Injection',
        'Max Power Delivered': 149.0, 'Max Power At': 3400,
        'Max Torque Delivered': 360.0, 'Max Torque At': 1400,
        'Acceleration': 12.8, 'Length': 4735, 'Width': 1830,
        'Height': 1795, 'Wheel Base': 2750, 'Kerb Weight': 1920,
        'Cargo Volume': 300, 'Gear Box': 6, 'Drive Type': 'RWD',
        'Seats': 8, 'Doors': 5, 'Steering Type': 'Power',
        'Turning Radius': 5.6, 'Front Brake Type': 'Disc',
        'Rear Brake Type': 'Drum', 'Tyre Type': 'Tubeless Tyres',
        'Alloy Wheel Size': 16
    }
}

BODY_OPTIONS = ['Sedan', 'SUV', 'Hatchback', 'MUV', 'Coupe', 'Convertible',
                'Minivan', 'Pickup Truck', 'Wagon', 'Sports Car', 'Compact SUV']
TRANSMISSION_OPTIONS = ['Manual', 'Automatic']
FUEL_OPTIONS = ['Petrol', 'Diesel', 'CNG', 'Electric', 'Hybrid', 'LPG']
VALVE_OPTIONS = ['DOHC', 'SOHC', 'OHV', 'SV']
DRIVE_OPTIONS = ['FWD', 'RWD', 'AWD', '4WD', '4x4']
STEERING_OPTIONS = ['Power', 'Electric', 'Manual']
FRONT_BRAKE_OPTIONS = ['Disc', 'Ventilated Disc', 'Drum', 'Caliper Disc', 'Ceramic Disc']
REAR_BRAKE_OPTIONS = ['Disc', 'Drum', 'Ventilated Disc', 'Caliper Disc', 'Ceramic Disc']
TYRE_OPTIONS = ['Tubeless Tyres', 'Tube Tyres', 'Run Flat Tyres', 'Tube Type', 'Radial']
OWNER_OPTIONS = ['First Owner', 'Second Owner', 'Third Owner', 'Fourth Owner+']
FUEL_SUPPLY_OPTIONS = ['MPFI', 'Common Rail Injection', 'CRDI', 'EFI', 'Direct Injection',
                       'Carburettor', 'DI', 'PFI', 'SEFI', 'TDI', 'TFSI', 'IDC']
STATE_OPTIONS = sorted([
    'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
    'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand',
    'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
    'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan',
    'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
    'Uttarakhand', 'West Bengal', 'Chandigarh', 'Puducherry',
    'Jammu and Kashmir', 'Ladakh'
])

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main .block-container {
    padding-top: 2rem;
    max-width: 1200px;
}

/* Hero header */
.hero-header {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    border-radius: 20px;
    padding: 2.5rem 2rem;
    margin-bottom: 2rem;
    text-align: center;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    border: 1px solid rgba(255,255,255,0.05);
}
.hero-header h1 {
    font-size: 2.4rem;
    font-weight: 800;
    background: linear-gradient(90deg, #a78bfa, #6366f1, #10b981, #34d399);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
    letter-spacing: -0.5px;
}
.hero-header p {
    color: #94a3b8;
    font-size: 1.05rem;
    font-weight: 400;
}

/* Metric cards */
.metric-card {
    background: linear-gradient(145deg, #1e1b4b, #312e81);
    border-radius: 16px;
    padding: 1.8rem 1.5rem;
    text-align: center;
    border: 1px solid rgba(99, 102, 241, 0.3);
    box-shadow: 0 8px 32px rgba(99, 102, 241, 0.15);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.metric-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(99, 102, 241, 0.25);
}
.metric-card .label {
    color: #a5b4fc;
    font-size: 0.85rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 0.5rem;
}
.metric-card .value {
    font-size: 2rem;
    font-weight: 800;
    color: #e0e7ff;
    line-height: 1.2;
}
.metric-card .sub {
    color: #818cf8;
    font-size: 0.82rem;
    margin-top: 0.4rem;
    font-weight: 500;
}

/* Best prediction hero */
.best-card {
    background: linear-gradient(145deg, #064e3b, #065f46);
    border: 1px solid rgba(16, 185, 129, 0.4);
    box-shadow: 0 8px 32px rgba(16, 185, 129, 0.2);
}
.best-card:hover {
    box-shadow: 0 12px 40px rgba(16, 185, 129, 0.3);
}
.best-card .label { color: #6ee7b7; }
.best-card .value { color: #ecfdf5; font-size: 2.4rem; }
.best-card .sub { color: #34d399; }

/* Range card */
.range-card {
    background: linear-gradient(145deg, #1e1b4b, #312e81);
    border: 1px solid rgba(139, 92, 246, 0.3);
    border-radius: 16px;
    padding: 1.5rem;
    text-align: center;
}
.range-card .label { color: #c4b5fd; font-size: 0.85rem; font-weight: 600;
    text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.3rem; }
.range-card .value { color: #e0e7ff; font-size: 1.3rem; font-weight: 700; }

/* Table styling */
.model-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    border-radius: 12px;
    overflow: hidden;
    font-size: 0.92rem;
}
.model-table thead th {
    background: #1e1b4b;
    color: #a5b4fc;
    padding: 0.9rem 1rem;
    text-align: left;
    font-weight: 600;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-bottom: 2px solid #312e81;
}
.model-table tbody tr {
    transition: background 0.2s ease;
}
.model-table tbody tr:hover {
    background: rgba(99, 102, 241, 0.08);
}
.model-table tbody td {
    padding: 0.8rem 1rem;
    border-bottom: 1px solid rgba(99, 102, 241, 0.1);
    color: #e0e7ff;
}
.model-table .rank-badge {
    display: inline-block;
    width: 28px; height: 28px;
    border-radius: 50%;
    text-align: center;
    line-height: 28px;
    font-weight: 700;
    font-size: 0.8rem;
}
.rank-1 { background: linear-gradient(135deg, #f59e0b, #d97706); color: #fff; }
.rank-2 { background: linear-gradient(135deg, #9ca3af, #6b7280); color: #fff; }
.rank-3 { background: linear-gradient(135deg, #b45309, #92400e); color: #fff; }
.rank-other { background: #312e81; color: #a5b4fc; }

.r2-badge {
    display: inline-block;
    padding: 0.25rem 0.6rem;
    border-radius: 20px;
    font-weight: 600;
    font-size: 0.82rem;
}
.r2-high { background: rgba(16, 185, 129, 0.15); color: #34d399; }
.r2-mid { background: rgba(251, 191, 36, 0.15); color: #fbbf24; }
.r2-low { background: rgba(239, 68, 68, 0.15); color: #f87171; }

.family-badge {
    display: inline-block;
    padding: 0.2rem 0.55rem;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 600;
}
.family-ensemble { background: rgba(16, 185, 129, 0.12); color: #34d399; }
.family-regression { background: rgba(99, 102, 241, 0.12); color: #818cf8; }
.family-kernel { background: rgba(139, 92, 246, 0.12); color: #a78bfa; }

/* Section headers */
.section-header {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin: 2rem 0 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid rgba(99, 102, 241, 0.2);
}
.section-header h3 {
    color: #e0e7ff;
    font-weight: 700;
    font-size: 1.15rem;
    margin: 0;
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f0c29 0%, #1a1744 100%);
}
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stNumberInput label,
section[data-testid="stSidebar"] .stTextInput label {
    color: #a5b4fc !important;
    font-weight: 500;
    font-size: 0.85rem;
}

/* Predict button */
.stButton > button {
    background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.75rem 2rem !important;
    font-weight: 700 !important;
    font-size: 1.1rem !important;
    width: 100% !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(99, 102, 241, 0.5) !important;
}

/* Note box */
.note-box {
    background: rgba(99, 102, 241, 0.08);
    border: 1px solid rgba(99, 102, 241, 0.2);
    border-radius: 10px;
    padding: 1rem;
    color: #a5b4fc;
    font-size: 0.85rem;
    margin-top: 1rem;
}

/* Missing model warning */
.missing-model {
    background: rgba(251, 191, 36, 0.08);
    border: 1px solid rgba(251, 191, 36, 0.25);
    border-radius: 10px;
    padding: 0.8rem 1rem;
    color: #fbbf24;
    font-size: 0.85rem;
}
</style>
"""
