import streamlit as st

st.title("Electrical Circuit Dashboard ⚡")
st.write("Welcome to my first interactive app!")

# Slider for voltage
voltage = st.slider("Select Voltage (V)", 0, 50, 12)
st.write(f"Current Voltage: {voltage} V")

# Simple button
if st.button("Calculate"):
    st.success(f"Calculation complete for {voltage} V!")
    
