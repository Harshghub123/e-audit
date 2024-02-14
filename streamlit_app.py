import streamlit as st
import pandas as pd

# App title and introduction
st.title("Energy Audit App")
st.write("Calculate your energy consumption and estimated costs in INR.")

# Input form
num_appliances = st.number_input("Number of appliances:", min_value=1, max_value=10)
appliance_data = []
for i in range(num_appliances):
    name = st.text_input(f"Appliance {i+1} name:")
    wattage = st.number_input(f"{name}'s wattage:", min_value=1)
    hours_daily = st.number_input(f"{name}'s daily usage hours:", min_value=0.0)
    appliance_data.append({"name": name, "wattage": wattage, "hours": hours_daily})

# Electricity rate in INR per kWh
electricity_rate = st.number_input("Enter your electricity rate (e.g., 5 for ₹5 per kWh):", min_value=0.01)

# Calculations and report
def calculate_report(data, rate):
    daily_kwh = []
    for appliance in data:
        daily_kwh.append(appliance["wattage"] * appliance["hours"] / 1000)
    total_daily_kwh = sum(daily_kwh)

    monthly_kwh = total_daily_kwh * 30
    yearly_kwh = monthly_kwh * 12

    monthly_cost = monthly_kwh * rate
    yearly_cost = yearly_kwh * rate

    report = {
        "total_daily_kwh": total_daily_kwh,
        "monthly_kwh": monthly_kwh,
        "yearly_kwh": yearly_kwh,
        "monthly_cost": monthly_cost,
        "yearly_cost": yearly_cost,
    }
    return report

report_data = calculate_report(appliance_data, electricity_rate)

# Display report
st.header("Energy Audit Report")
st.write(f"Total daily energy consumption: {report_data['total_daily_kwh']:.2f} kWh")
st.write(f"Total monthly energy consumption: {report_data['monthly_kwh']:.2f} kWh")
st.write(f"Total yearly energy consumption: {report_data['yearly_kwh']:.2f} kWh")
st.write("Estimated monthly cost:", f"₹{report_data['monthly_cost']:.2f}")
st.write("Estimated yearly cost:", f"₹{report_data['yearly_cost']:.2f}")

# ... rest of the code remains the same

