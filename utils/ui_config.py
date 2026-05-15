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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main .block-container {
    padding-top: 2rem;
    max-width: 1000px;
}

/* Hero header */
.hero-header {
    background-color: #1e1b4b;
    border-radius: 8px;
    padding: 2rem;
    margin-bottom: 2rem;
    text-align: left;
    border: 1px solid #312e81;
}
.hero-header h1 {
    font-size: 2rem;
    font-weight: 600;
    color: #e0e7ff;
    margin-bottom: 0.5rem;
}
.hero-header p {
    color: #94a3b8;
    font-size: 1rem;
}

/* Metric cards */
.metric-card {
    background-color: #1e1b4b;
    border-radius: 8px;
    padding: 1.5rem;
    text-align: left;
    border: 1px solid #312e81;
    margin-bottom: 1rem;
}
.metric-card .label {
    color: #a5b4fc;
    font-size: 0.9rem;
    font-weight: 500;
    margin-bottom: 0.5rem;
}
.metric-card .value {
    font-size: 1.8rem;
    font-weight: 600;
    color: #e0e7ff;
}
.metric-card .sub {
    color: #818cf8;
    font-size: 0.85rem;
    margin-top: 0.5rem;
}

/* Best prediction hero */
.best-card {
    background-color: #1e293b;
    border: 1px solid #334155;
}
.best-card .label { color: #94a3b8; }
.best-card .value { color: #f8fafc; font-size: 2rem; }
.best-card .sub { color: #cbd5e1; }

/* Range card */
.range-card {
    background-color: #1e1b4b;
    border: 1px solid #312e81;
    border-radius: 8px;
    padding: 1.5rem;
    text-align: left;
}
.range-card .label { color: #a5b4fc; font-size: 0.9rem; font-weight: 500; margin-bottom: 0.5rem; }
.range-card .value { color: #e0e7ff; font-size: 1.2rem; font-weight: 600; }

/* Table styling */
.model-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.95rem;
}
.model-table th, .model-table td {
    padding: 0.75rem 1rem;
    text-align: left;
    border-bottom: 1px solid #312e81;
}
.model-table th {
    color: #a5b4fc;
    font-weight: 600;
    font-size: 0.85rem;
    background-color: #1e1b4b;
}
.model-table td {
    color: #e0e7ff;
}

.rank-badge {
    font-weight: 600;
    color: #a5b4fc;
}

.r2-badge, .family-badge {
    font-size: 0.85rem;
    color: #cbd5e1;
}

/* Section headers */
.section-header {
    margin: 2rem 0 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid #312e81;
}
.section-header h3 {
    color: #e0e7ff;
    font-weight: 600;
    font-size: 1.2rem;
    margin: 0;
}

/* Note box */
.note-box {
    background-color: #1e1b4b;
    border: 1px solid #312e81;
    border-radius: 8px;
    padding: 1rem;
    color: #cbd5e1;
    font-size: 0.95rem;
    margin-top: 1rem;
}

/* Missing model warning */
.missing-model {
    background-color: #332701;
    border: 1px solid #715200;
    border-radius: 8px;
    padding: 0.8rem 1rem;
    color: #fde047;
    font-size: 0.95rem;
}
</style>
"""

