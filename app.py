import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Mechanical Utility App", layout="wide")

# --- HEADER SECTION ---
st.title("🛠️ Mechanical Unit Converter & Material Density Checker")
st.markdown(f"**Student Name:** MUHAMMAD ALI ABDULLAH")
st.markdown(f"**Roll Number:** 25-ME-208")
st.divider()

# --- SIDEBAR NAVIGATION ---
option = st.sidebar.radio("Select Tool", ["Unit Converter", "Material Density Checker"])

# --- TOOL 1: UNIT CONVERTER ---
if option == "Unit Converter":
    st.header("Unit Converter")
    col1, col2 = st.columns(2)
    
    with col1:
        category = st.selectbox("Category", ["Length", "Pressure", "Force"])
        value = st.number_input("Enter Value", value=1.0)

    if category == "Length":
        units = {"Meters": 1, "Millimeters": 1000, "Inches": 39.3701, "Feet": 3.28084}
    elif category == "Pressure":
        units = {"Pascal (Pa)": 1, "Bar": 1e-5, "PSI": 0.000145038, "Atm": 9.8692e-6}
    elif category == "Force":
        units = {"Newton (N)": 1, "KiloNewton (kN)": 0.001, "Pound-force (lbf)": 0.224809}

    with col2:
        from_unit = st.selectbox("From", list(units.keys()))
        to_unit = st.selectbox("To", list(units.keys()))

    # Calculation
    base_value = value / units[from_unit]
    result = base_value * units[to_unit]
    
    st.success(f"**Result:** {value} {from_unit} = {result:.4f} {to_unit}")

# --- TOOL 2: MATERIAL DENSITY ---
else:
    st.header("Material Density Checker")
    st.write("Quick reference for common engineering materials.")

    # Density Data (kg/m^3)
    data = {
        "Material": ["Steel (Mild)", "Aluminum (6061)", "Titanium", "Copper", "ABS Plastic", "Carbon Fiber (CFRP)", "Concrete"],
        "Density (kg/m³)": [7850, 2700, 4500, 8960, 1040, 1550, 2400],
        "Modulus of Elasticity (GPa)": [200, 68.9, 116, 117, 2.3, 150, 30]
    }
    df = pd.DataFrame(data)

    search = st.text_input("Search Material", "")
    if search:
        filtered_df = df[df['Material'].str.contains(search, case=False)]
        st.table(filtered_df)
    else:
        st.table(df)

    st.info("Note: Values are approximate and vary based on specific alloy grades.")
