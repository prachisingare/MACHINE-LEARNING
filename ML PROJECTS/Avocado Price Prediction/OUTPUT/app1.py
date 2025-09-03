import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="🥑 Avocado Price Prediction", page_icon="🥑", layout="centered")

st.title("🥑 Avocado Price Prediction App")

st.markdown("Fill in the details below to predict the **Average Price** of avocados.")

# User inputs
col1, col2 = st.columns(2)

with col1:
    year = st.number_input("Year", min_value=2010, max_value=2025, value=2018)
    avocado_type = st.selectbox("Type", ["conventional", "organic"])
    region = st.selectbox("Region", ["Albany", "California", "Chicago"])  # extend with your dataset regions

with col2:
    total_volume = st.number_input("Total Volume", min_value=0.0, value=10000.0, step=100.0)
    total_bags = st.number_input("Total Bags", min_value=0.0, value=5000.0, step=100.0)
    small_bags = st.number_input("Small Bags", min_value=0.0, value=4000.0, step=100.0)
    large_bags = st.number_input("Large Bags", min_value=0.0, value=800.0, step=50.0)
    xlarge_bags = st.number_input("XLarge Bags", min_value=0.0, value=200.0, step=10.0)

# Encode categorical inputs (must match training encoding)
type_encoded = 1 if avocado_type == "organic" else 0
region_mapping = {"Albany": 0, "California": 1, "Chicago": 2}  # update with your dataset encoding
region_encoded = region_mapping.get(region, 0)

# Prediction button
if st.button("Predict Price"):
    features = np.array([[total_volume, total_bags, small_bags, large_bags, 
                          xlarge_bags, type_encoded, year, region_encoded]])
    prediction = model.predict(features)[0]
    st.success(f"✅ Predicted Avocado Price: **${prediction:.2f}**")
