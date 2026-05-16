"""UI configuration: example presets, CSS styles, and constants."""

EXAMPLES = {
    "-- Select Example --": None,
    "2019 Maruti Swift VXI (Budget)": {
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
    "2021 Hyundai Creta SX (Mid-range)": {
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

PLOTLY_WHITE_LAYOUT = dict(
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(color='#374151', family='Inter', size=12),
    height=380,
    margin=dict(l=10, r=20, t=20, b=30),
    xaxis=dict(
        showgrid=True,
        gridcolor='#F3F4F6',
        gridwidth=1,
        linecolor='#E5E7EB',
        tickfont=dict(color='#6B7280', size=11),
        title_font=dict(color='#6B7280', size=11),
    ),
    yaxis=dict(
        showgrid=False,
        linecolor='#E5E7EB',
        tickfont=dict(color='#374151', size=11),
    ),
    hoverlabel=dict(
        bgcolor='white',
        bordercolor='#E5E7EB',
        font=dict(color='#111827', family='Inter')
    )
)

CUSTOM_CSS = """
<style>
/* === RESET & BASE === */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu {visibility:hidden;} footer {visibility:hidden;} header {visibility:hidden;}
.main .block-container { padding-top: 1.5rem; max-width: 1100px; }

/* === SIDEBAR === */
[data-testid="stSidebar"] {
    background-color: #F8F9FA;
    border-right: 1px solid #E5E7EB;
    min-width: 320px; max-width: 320px;
}
[data-testid="stSidebar"] .stButton > button {
    background: #1D4ED8; color: white; font-weight: 600;
    height: 48px; border-radius: 8px; border: none;
    font-size: 0.95rem; letter-spacing: 0.01em;
    transition: background 0.2s;
}
[data-testid="stSidebar"] .stButton > button:hover { background: #1E3A8A; }

/* === CARDS === */
.card { background: white; border: 1px solid #E5E7EB; border-radius: 12px; padding: 1.5rem; }
.card-blue { background: #EFF6FF; border: 1px solid #BFDBFE; border-left: 4px solid #1D4ED8; border-radius: 12px; padding: 1.5rem; }
.card-green { background: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 12px; padding: 1.5rem; }
.card-amber { background: white; border: 1px solid #E5E7EB; border-left: 3px solid #F59E0B; border-radius: 12px; padding: 1.5rem; }
.card-label { font-size: 0.72rem; font-weight: 600; color: #6B7280; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 0.5rem; }
.card-value { font-size: 2rem; font-weight: 700; color: #111827; line-height: 1.1; }
.card-value-lg { font-size: 2.4rem; font-weight: 700; color: #111827; line-height: 1.1; }
.card-sub { font-size: 0.82rem; color: #6B7280; margin-top: 0.4rem; }

/* === HERO === */
.hero { background: white; border: 1px solid #E5E7EB; border-radius: 16px; padding: 2.5rem; margin-bottom: 2rem; }
.hero-badge { display: inline-block; background: #EFF6FF; color: #1D4ED8; font-size: 0.78rem; font-weight: 600; padding: 4px 12px; border-radius: 20px; margin-bottom: 1rem; }
.hero-title { font-size: 2.2rem; font-weight: 700; color: #111827; margin: 0 0 0.5rem; }
.hero-subtitle { color: #6B7280; font-size: 1rem; line-height: 1.6; margin-bottom: 1.2rem; }
.hero-chips { display: flex; gap: 8px; flex-wrap: wrap; }
.chip { background: #F3F4F6; color: #374151; font-size: 0.8rem; font-weight: 500; padding: 4px 12px; border-radius: 20px; border: 1px solid #E5E7EB; }

/* === TABLE === */
.model-table { width: 100%; border-collapse: collapse; font-size: 0.875rem; }
.model-table thead tr { border-bottom: 2px solid #E5E7EB; }
.model-table th { font-size: 0.72rem; font-weight: 600; color: #6B7280; text-transform: uppercase; letter-spacing: 0.05em; padding: 0.6rem 1rem; text-align: left; }
.model-table td { padding: 0.75rem 1rem; color: #374151; border-bottom: 1px solid #F3F4F6; }
.model-table tbody tr:hover td { background: #F9FAFB; }
.model-table .best-row td { background: #EFF6FF; font-weight: 600; }

/* === BADGES === */
.badge { display: inline-block; padding: 3px 10px; border-radius: 12px; font-size: 0.78rem; font-weight: 600; }
.badge-green { background: #D1FAE5; color: #065F46; }
.badge-amber { background: #FEF3C7; color: #92400E; }
.badge-red { background: #FEE2E2; color: #991B1B; }
.badge-blue { background: #DBEAFE; color: #1E40AF; }
.badge-gray { background: #F3F4F6; color: #374151; }

/* === SECTION LABELS === */
.section-label { font-size: 0.72rem; font-weight: 600; color: #9CA3AF; text-transform: uppercase; letter-spacing: 0.08em; margin: 1.5rem 0 0.75rem; }

/* === HOW IT WORKS === */
.steps-row { display: flex; gap: 1rem; align-items: flex-start; }
.step-card { flex: 1; background: white; border: 1px solid #E5E7EB; border-radius: 12px; padding: 1.2rem; text-align: center; }
.step-number { width: 32px; height: 32px; background: #1D4ED8; color: white; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 0.85rem; font-weight: 700; margin-bottom: 0.5rem; }
.step-title { font-weight: 600; color: #111827; font-size: 0.9rem; margin-bottom: 0.3rem; }
.step-desc { font-size: 0.82rem; color: #6B7280; line-height: 1.4; }
.step-arrow { font-size: 1.5rem; color: #D1D5DB; align-self: center; }

/* === CONFIDENCE BAR === */
.confidence-wrapper { display: flex; align-items: center; gap: 12px; margin: 1rem 0; }
.confidence-label { font-size: 0.8rem; font-weight: 500; color: #6B7280; white-space: nowrap; }
.confidence-track { flex: 1; height: 8px; background: #E5E7EB; border-radius: 4px; position: relative; }
.confidence-fill { height: 100%; border-radius: 4px; background: linear-gradient(90deg, #BFDBFE, #1D4ED8); }
.confidence-pointer { position: absolute; top: -4px; width: 16px; height: 16px; border-radius: 50%; background: #1D4ED8; border: 2px solid white; box-shadow: 0 1px 3px rgba(0,0,0,0.2); transform: translateX(-50%); }

/* === RESULTS HEADER === */
.results-header { display: flex; align-items: baseline; gap: 12px; margin-bottom: 1.5rem; }
.results-header h2 { font-size: 1.6rem; font-weight: 700; color: #111827; margin: 0; }
.results-car-tag { background: #F3F4F6; color: #374151; font-size: 0.85rem; font-weight: 500; padding: 4px 12px; border-radius: 20px; border: 1px solid #E5E7EB; }

/* === SIDEBAR BRAND === */
.sidebar-brand { padding: 1rem 0 0.75rem; border-bottom: 2px solid #1D4ED8; margin-bottom: 1rem; }
.sidebar-brand-name { font-size: 1.1rem; font-weight: 700; color: #111827; }
.sidebar-brand-sub { font-size: 0.78rem; color: #6B7280; margin-top: 2px; }

/* === MISC === */
.divider { height: 1px; background: #E5E7EB; margin: 1.25rem 0; }
.inline-bar-track { display: inline-block; width: 80px; height: 6px; background: #E5E7EB; border-radius: 3px; vertical-align: middle; margin-left: 8px; }
.inline-bar-fill { height: 100%; border-radius: 3px; }
.footer-strip { background: #F8F9FA; border: 1px solid #E5E7EB; border-radius: 8px; padding: 0.6rem 1rem; font-size: 0.78rem; color: #9CA3AF; margin-top: 2rem; }
.insight-list { list-style: none; padding-left: 0; margin-top: 0.5rem; font-size: 0.9rem; color: #374151; }
.insight-list li { margin-bottom: 0.4rem; }
</style>
"""
