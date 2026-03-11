import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_model.pkl")

st.title("Fraud Detection System")

st.write("Enter transaction details")

amt = st.number_input("Transaction Amount")
city_pop = st.number_input("City Population")
lat = st.number_input("Latitude")
long = st.number_input("Longitude")

if st.button("Check Fraud"):

    input_data = pd.DataFrame([[amt, city_pop, lat, long]],
                              columns=["amt","city_pop","lat","long"])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Fraud Transaction Detected")
    else:
        st.success("Normal Transaction")