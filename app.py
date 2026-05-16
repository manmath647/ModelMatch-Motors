"""Used Car Price Predictor — Streamlit App."""
import streamlit as st
import numpy as np
import sys
import plotly.graph_objects as go
from utils.preprocess import encode_and_scale, load_scaler
from utils.predictor import (
    get_available_models, load_model, predict_all,
    get_confidence_range, format_price_inr, MODEL_CONFIGS
)
from utils.ui_config import (
    EXAMPLES, CUSTOM_CSS, BODY_OPTIONS, TRANSMISSION_OPTIONS, FUEL_OPTIONS,
    VALVE_OPTIONS, DRIVE_OPTIONS, STEERING_OPTIONS, FRONT_BRAKE_OPTIONS,
    REAR_BRAKE_OPTIONS, TYRE_OPTIONS, OWNER_OPTIONS, FUEL_SUPPLY_OPTIONS,
    STATE_OPTIONS, PLOTLY_WHITE_LAYOUT
)

st.set_page_config(
    page_title="ModelMatch Motors",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


@st.cache_resource
def cached_load_scaler():
    return load_scaler()


@st.cache_resource
def cached_load_models():
    available = get_available_models()
    loaded = {}
    for name, config in available.items():
        try:
            loaded[name] = load_model(config['path'])
        except Exception as e:
            st.warning(f"Could not load {name}: {e}")
    return loaded


scaler = cached_load_scaler()
loaded_models = cached_load_models()

# ── Helper to get default value from example ──
def _get(key, default=None):
    ex = st.session_state.get('_example_data')
    if ex and key in ex:
        return ex[key]
    return default


def _idx(options, key, default=0):
    ex = st.session_state.get('_example_data')
    if ex and key in ex:
        val = ex[key]
        for i, o in enumerate(options):
            if o.lower() == str(val).lower():
                return i
    return default


# ── SIDEBAR ──
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <div class="sidebar-brand-name">🚗 ModelMatch Motors</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-label" style="margin-top:0;">QUICK START</div>', unsafe_allow_html=True)
    example_choice = st.selectbox("Load Example Car", list(EXAMPLES.keys()), label_visibility="collapsed")
    if example_choice != "-- Select Example --" and EXAMPLES[example_choice]:
        st.session_state['_example_data'] = EXAMPLES[example_choice]
        if st.session_state.get('_last_example') != example_choice:
            st.success("✓ Example loaded")
            st.session_state['_last_example'] = example_choice
    elif example_choice == "-- Select Example --":
        st.session_state['_example_data'] = None

    st.markdown("---")

    with st.expander("🚘 Basic Info", expanded=True):
        myear = st.number_input("Manufacture Year", 1990, 2026, _get('myear', 2019))
        body = st.selectbox("Body Type", BODY_OPTIONS, _idx(BODY_OPTIONS, 'body', 0))
        transmission = st.selectbox("Transmission", TRANSMISSION_OPTIONS, _idx(TRANSMISSION_OPTIONS, 'transmission', 0))
        fuel = st.selectbox("Fuel Type", FUEL_OPTIONS, _idx(FUEL_OPTIONS, 'fuel', 0))
        km = st.number_input("Kilometers Driven", 0, 500000, _get('km', 45000), step=1000)
        oem = st.text_input("Manufacturer (OEM)", _get('oem', ''))
        model_name = st.text_input("Model", _get('model', ''))
        variant = st.text_input("Variant", _get('variant', ''))

    with st.expander("📍 Location & Listing"):
        city = st.text_input("City", _get('City', ''))
        state = st.selectbox("State", STATE_OPTIONS, _idx(STATE_OPTIONS, 'state', 0))
        color = st.text_input("Color", _get('Color', ''))
        ext_color = st.text_input("Exterior Color", _get('exterior_color', ''))
        owner = st.selectbox("Owner Type", OWNER_OPTIONS, _idx(OWNER_OPTIONS, 'owner_type', 0))

    with st.expander("⚙️ Engine & Performance"):
        engine_type = st.text_input("Engine Type", _get('Engine Type', ''))
        cylinders = st.number_input("No. of Cylinders", 1, 16, _get('No of Cylinder', 4))
        valves_per = st.number_input("Valves per Cylinder", 1, 5, _get('Valves per Cylinder', 4))
        valve_config = st.selectbox("Valve Configuration", VALVE_OPTIONS, _idx(VALVE_OPTIONS, 'Valve Configuration', 0))
        turbo = st.selectbox("Turbo Charger", ['No', 'Yes'], 1 if _get('Turbo Charger', 'No') == 'Yes' else 0)
        supercharger = st.selectbox("Super Charger", ['No', 'Yes'], 1 if _get('Super Charger', 'No') == 'Yes' else 0)
        fuel_supply = st.selectbox("Fuel Supply System", FUEL_SUPPLY_OPTIONS, _idx(FUEL_SUPPLY_OPTIONS, 'Fuel Suppy System', 0))
        max_power = st.number_input("Max Power (bhp)", 10.0, 1000.0, float(_get('Max Power Delivered', 101.0)), step=1.0)
        max_power_at = st.number_input("Max Power At (rpm)", 1000, 12000, _get('Max Power At', 5127), step=100)
        max_torque = st.number_input("Max Torque (Nm)", 10.0, 1000.0, float(_get('Max Torque Delivered', 176.0)), step=1.0)
        max_torque_at = st.number_input("Max Torque At (rpm)", 500, 8000, _get('Max Torque At', 3177), step=100)
        acceleration = st.number_input("0-100 kmph (sec)", 2.0, 40.0, float(_get('Acceleration', 13.2)), step=0.1)

    with st.expander("📐 Dimensions"):
        length = st.number_input("Length (mm)", 2000, 6000, _get('Length', 4110), step=10)
        width = st.number_input("Width (mm)", 1200, 2500, _get('Width', 1724), step=10)
        height = st.number_input("Height (mm)", 1000, 2500, _get('Height', 1576), step=10)
        wheelbase = st.number_input("Wheel Base (mm)", 1500, 4000, _get('Wheel Base', 2543), step=10)
        kerb_wt = st.number_input("Kerb Weight (kg)", 400, 4000, _get('Kerb Weight', 1116), step=10)
        cargo = st.number_input("Cargo Volume (L)", 50, 1500, _get('Cargo Volume', 360), step=10)

    with st.expander("🔧 Transmission & Chassis"):
        gearbox = st.number_input("Gears", 3, 10, _get('Gear Box', 5))
        drive = st.selectbox("Drive Type", DRIVE_OPTIONS, _idx(DRIVE_OPTIONS, 'Drive Type', 0))
        seats = st.number_input("Seats", 2, 12, _get('Seats', 5))
        doors = st.number_input("Doors", 2, 6, _get('Doors', 5))
        steering = st.selectbox("Steering Type", STEERING_OPTIONS, _idx(STEERING_OPTIONS, 'Steering Type', 0))
        turning_r = st.number_input("Turning Radius (m)", 3.0, 8.0, float(_get('Turning Radius', 5.52)), step=0.1)
        front_brake = st.selectbox("Front Brake", FRONT_BRAKE_OPTIONS, _idx(FRONT_BRAKE_OPTIONS, 'Front Brake Type', 0))
        rear_brake = st.selectbox("Rear Brake", REAR_BRAKE_OPTIONS, _idx(REAR_BRAKE_OPTIONS, 'Rear Brake Type', 0))
        tyre = st.selectbox("Tyre Type", TYRE_OPTIONS, _idx(TYRE_OPTIONS, 'Tyre Type', 0))
        alloy_size = st.number_input("Alloy Wheel Size (in)", 10, 24, _get('Alloy Wheel Size', 15))

    st.markdown(f'<div style="text-align: center; color: #6B7280; font-size: 0.8rem; margin: 1rem 0;">{len(loaded_models)} models ready · 41 features</div>', unsafe_allow_html=True)
    predict_btn = st.button("🔍 Predict Price", use_container_width=True, type="primary")

# ── Build input dict ──
input_data = {
    'myear': myear, 'body': body, 'transmission': transmission, 'fuel': fuel,
    'km': km, 'oem': oem, 'model': model_name, 'variant': variant,
    'City': city, 'Color': color, 'Engine Type': engine_type,
    'No of Cylinder': cylinders, 'Valves per Cylinder': valves_per,
    'Valve Configuration': valve_config, 'Turbo Charger': turbo,
    'Super Charger': supercharger, 'Length': length, 'Width': width,
    'Height': height, 'Wheel Base': wheelbase, 'Kerb Weight': kerb_wt,
    'Gear Box': gearbox, 'Drive Type': drive, 'Seats': seats,
    'Steering Type': steering, 'Turning Radius': turning_r,
    'Front Brake Type': front_brake, 'Rear Brake Type': rear_brake,
    'Acceleration': acceleration, 'Tyre Type': tyre, 'Doors': doors,
    'Cargo Volume': cargo, 'state': state, 'exterior_color': ext_color,
    'owner_type': owner, 'Fuel Suppy System': fuel_supply,
    'Alloy Wheel Size': alloy_size, 'Max Power Delivered': max_power,
    'Max Power At': max_power_at, 'Max Torque Delivered': max_torque,
    'Max Torque At': max_torque_at,
}

# ── MAIN AREA ──
if not predict_btn:
    # Landing state
    st.markdown("""
    <div class="hero">
        <div class="hero-badge">🇮🇳 Indian Used Car Market</div>
        <h1 class="hero-title">ModelMatch Motors</h1>
        <p class="hero-subtitle">AI-powered price estimation using 7 machine learning models.<br>Fill in car details on the left and click Predict Price.</p>
        <div class="hero-chips">
            <span class="chip">XGBoost R²=0.9494</span>
            <span class="chip">41 Features</span>
            <span class="chip">7 Models</span>
            <span class="chip">Indian Market Data</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="card" style="border-left: 3px solid #1D4ED8;">
            <div class="card-value">7</div>
            <div class="card-sub">ML Models</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card" style="border-left: 3px solid #1D4ED8;">
            <div class="card-value">41</div>
            <div class="card-sub">Input Features</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="card" style="border-left: 3px solid #1D4ED8;">
            <div class="card-value">0.9494</div>
            <div class="card-sub">Best R² (XGBoost)</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="section-label">HOW IT WORKS</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="steps-row">
        <div class="step-card">
            <div class="step-number">1</div>
            <div class="step-title">📝 Enter Specs</div>
            <div class="step-desc">Provide 41 car features in the sidebar</div>
        </div>
        <div class="step-arrow">→</div>
        <div class="step-card">
            <div class="step-number">2</div>
            <div class="step-title">🤖 Run Models</div>
            <div class="step-desc">Data processed through 7 ML models</div>
        </div>
        <div class="step-arrow">→</div>
        <div class="step-card">
            <div class="step-number">3</div>
            <div class="step-title">💰 Get Price</div>
            <div class="step-desc">View consensus price & confidence range</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="section-label">EXAMPLE PREDICTIONS</div>', unsafe_allow_html=True)
    st.markdown("""
    <table class="model-table">
        <thead>
            <tr>
                <th>Car</th>
                <th>Segment</th>
                <th>Est. Range</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>2019 Maruti Swift VXI</td>
                <td><span class="badge badge-gray">Budget</span></td>
                <td><strong>₹4–6L</strong></td>
            </tr>
            <tr>
                <td>2021 Hyundai Creta SX</td>
                <td><span class="badge badge-gray">Mid-range</span></td>
                <td><strong>₹12–16L</strong></td>
            </tr>
            <tr>
                <td>2020 Toyota Innova Crysta</td>
                <td><span class="badge badge-gray">Premium</span></td>
                <td><strong>₹18–24L</strong></td>
            </tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)

else:
    # ── Run predictions ──
    with st.spinner("Running predictions across all models..."):
        X_scaled = encode_and_scale(input_data, scaler)
        results = predict_all(X_scaled, loaded_models)

    valid = {k: v for k, v in results.items() if v.get('price') is not None}
    if not valid:
        st.error("All models failed to produce predictions.")
        st.stop()

    best_name = min(valid, key=lambda n: valid[n].get('rank', 99))
    best = valid[best_name]
    avg_price = np.mean([v['price'] for v in valid.values()])
    lo, hi = get_confidence_range(best['price'], best['rmse'])

    pct = max(10, min(90, ((best['price'] - lo) / (hi - lo)) * 100)) if hi > lo else 50

    # ── Hero metrics ──
    st.markdown(f"""
    <div class="results-header">
        <h2>Price Estimate</h2>
        <span class="results-car-tag">{oem} {model_name} {myear}</span>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([5, 3, 4])
    with c1:
        st.markdown(f"""
        <div class="card-blue">
            <div class="card-label">BEST ESTIMATE ({best_name}) <span style="float:right;">🏆 #1</span></div>
            <div class="card-value-lg">{format_price_inr(best['price'])}</div>
            <div class="card-sub">R² = {best['r2']:.4f} · RMSE = {best['rmse']:.4f}<br>{best_name} · {best['family']} family</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="card">
            <div class="card-label">CONSENSUS</div>
            <div class="card-value" style="font-size: 1.8rem;">{format_price_inr(avg_price)}</div>
            <div class="card-sub">Average of {len(valid)} models</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="card-green">
            <div class="card-label">EXPECTED RANGE</div>
            <div class="card-value" style="font-size: 1.4rem;">{format_price_inr(lo)} – {format_price_inr(hi)}</div>
            <div class="card-sub">±1 RMSE confidence</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="confidence-wrapper">
        <div class="confidence-label">₹{format_price_inr(lo)}</div>
        <div class="confidence-track">
            <div class="confidence-fill" style="width: {pct}%;"></div>
            <div class="confidence-pointer" style="left: {pct}%;"></div>
        </div>
        <div class="confidence-label">₹{format_price_inr(hi)}</div>
    </div>
    """, unsafe_allow_html=True)

    st.code(f"Best Estimate: {format_price_inr(best['price'])} ({best_name})", language=None)

    # Price Breakdown Insight Card
    insights = []
    if myear >= 2020: insights.append("🗓 Recent model year adds ₹1–2L to value")
    if km < 30000: insights.append("📉 Low mileage — strong resale premium")
    if transmission == 'Automatic': insights.append("⚙️ Automatic transmission commands ~10% premium")
    if fuel == 'Diesel': insights.append("⛽ Diesel preferred for high-mileage buyers")
    if owner == 'First Owner': insights.append("👤 First owner status — highest trust premium")
    
    if insights:
        insights_html = "".join([f"<li>{i}</li>" for i in insights])
        st.markdown(f"""
        <div class="card-amber" style="margin-top: 1rem;">
            <div style="font-weight: 600; color: #111827; margin-bottom: 0.5rem;">What's driving this price?</div>
            <ul class="insight-list">
                {insights_html}
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Comparison Table ──
    st.markdown('<div class="section-label">MODEL BREAKDOWN</div>', unsafe_allow_html=True)

    rows_html = ""
    for name in sorted(valid, key=lambda n: valid[n].get('rank', 99)):
        v = valid[name]
        rank = v.get('rank', '-')
        
        # Rank medals
        rank_display = rank
        if rank == 1: rank_display = "🥇 1"
        elif rank == 2: rank_display = "🥈 2"
        elif rank == 3: rank_display = "🥉 3"
        
        r2c = 'badge-green' if v['r2'] >= 0.92 else 'badge-amber' if v['r2'] >= 0.85 else 'badge-red'
        bar_color = '#059669' if v['r2'] >= 0.92 else '#D97706' if v['r2'] >= 0.85 else '#DC2626'
        bar_width = max(0, v['r2']) * 100
        row_class = 'best-row' if rank == 1 else ''
        
        rows_html += f"""<tr class="{row_class}">
            <td>{rank_display}</td>
            <td><strong>{name}</strong></td>
            <td><span class="badge badge-gray">{v['family']}</span></td>
            <td>{format_price_inr(v['price'])}</td>
            <td><span class="badge {r2c}">{v['r2']:.4f}</span>
                <div class="inline-bar-track"><div class="inline-bar-fill" style="width:{bar_width}%; background:{bar_color};"></div></div>
            </td>
        </tr>"""

    st.markdown(f"""<table class="model-table">
        <thead><tr><th>Rank</th><th>Model</th><th>Family</th><th>Prediction</th><th>R² Score & Accuracy</th></tr></thead>
        <tbody>{rows_html}</tbody>
    </table>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Charts ──
    col_l, col_r = st.columns(2)

    with col_l:
        st.markdown('<div class="section-label">PRICE COMPARISON</div>', unsafe_allow_html=True)
        names = sorted(valid, key=lambda n: valid[n]['price'])
        prices = [valid[n]['price'] for n in names]
        
        blue_gradient = ['#DBEAFE', '#BFDBFE', '#93C5FD', '#60A5FA', '#3B82F6', '#2563EB', '#1D4ED8']
        colors = []
        for p in prices:
            idx = int(((p - min(prices)) / (max(prices) - min(prices) + 1e-9)) * (len(blue_gradient)-1))
            colors.append(blue_gradient[idx])

        fig1 = go.Figure()
        fig1.add_trace(go.Bar(
            x=prices, y=names, orientation='h',
            marker=dict(color=colors, line=dict(width=0)),
            text=[format_price_inr(p) for p in prices],
            textposition='auto', textfont=dict(size=11, color='white')
        ))
        fig1.add_vline(x=avg_price, line_dash="dash", line_color="#1D4ED8")
        fig1.update_layout(**PLOTLY_WHITE_LAYOUT)
        fig1.update_xaxes(title="Price (₹)")
        st.plotly_chart(fig1, use_container_width=True)

    with col_r:
        st.markdown('<div class="section-label">R² SCORE COMPARISON</div>', unsafe_allow_html=True)
        names_r2 = sorted(valid, key=lambda n: valid[n]['r2'])
        r2_vals = [valid[n]['r2'] for n in names_r2]
        r2_colors = ['#059669' if v >= 0.92 else '#D97706' if v >= 0.85 else '#DC2626' for v in r2_vals]

        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            x=r2_vals, y=names_r2, orientation='h',
            marker=dict(color=r2_colors, line=dict(width=0)),
            text=[f"{v:.4f}" for v in r2_vals],
            textposition='auto', textfont=dict(size=11, color='white')
        ))
        fig2.update_layout(**PLOTLY_WHITE_LAYOUT)
        fig2.update_xaxes(title="R² Score", range=[0.75, 1.0])
        st.plotly_chart(fig2, use_container_width=True)

    # ── Input Summary ──
    with st.expander("📋 View Input Summary"):
        st.markdown('<div style="font-family: monospace; font-size: 0.85rem;">', unsafe_allow_html=True)
        ic1, ic2, ic3 = st.columns(3)
        feats = list(input_data.items())
        third = len(feats) // 3
        for col, chunk in zip([ic1, ic2, ic3], [feats[:third], feats[third:2*third], feats[2*third:]]):
            with col:
                for k, v in chunk:
                    st.markdown(f"<span style='color:#6B7280;'>{k}:</span> <span style='color:#111827;font-weight:500;'>{v}</span>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ── Footer ──
st.markdown("""
<div class="footer-strip">
    ℹ️ Prices reflect Indian used car market trends · Model trained on CarDekho/CarWale data · Last updated 2024
</div>
""", unsafe_allow_html=True)
