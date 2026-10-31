import streamlit as st
import pandas as pd
import joblib

# Load trained model
@st.cache_resource
def load_model():
    return joblib.load("hdb_resale_model.pkl")

bundle = load_model()

model = bundle["model"]
feature_columns = bundle["feature_columns"]

# Application title
st.title("Singapore HDB Resale Price Predictor")

st.write("Predict HDB resale prices using Random Forest Machine Learning.")

# User inputs
st.header("Enter HDB Property Details")

town = st.selectbox("Town", bundle["towns"])

flat_type = st.selectbox("Flat Type", bundle["flat_types"])

floor_area = st.number_input(
    "Floor Area (sqm)", min_value=20.0, value=90.0
)

storey_mid = st.number_input(
    "Storey Midpoint", min_value=1.0, value=5.0
)

remaining_lease = st.number_input(
    "Remaining Lease (Years)", min_value=1.0, value=70.0
)

year = st.number_input(
    "Transaction Year",
    min_value=2000,
    max_value=2026,
    value=2024
)

# Predict price
if st.button("Predict Resale Price"):

    input_df = pd.DataFrame({
        "floor_area_sqm": [floor_area],
        "storey_mid": [storey_mid],
        "remaining_lease_yrs": [remaining_lease],
        "year": [year],
        "town": [town],
        "flat_type": [flat_type]
    })

    input_df = pd.get_dummies(
        input_df,
        columns=["town", "flat_type"],
        drop_first=True
    )

    input_df = input_df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    prediction = model.predict(input_df)

    st.success(
        f"Estimated HDB Resale Price: S${prediction[0]:,.2f}"
    )
