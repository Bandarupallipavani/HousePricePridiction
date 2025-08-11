import streamlit as st
import joblib
import numpy as np

st.title("House Price Prediction App")

st.divider()

bedrooms = st.number_input("Number of bedrooms",min_value=0,value=0)
bathrooms = st.number_input("Number of bathrooms",min_value=0,value=0)
livingarea = st.number_input("Living area",min_value=0,value=2000)
condition = st.number_input("Condition",min_value=0,value=3)
numberofschools = st.number_input("NUmber of schools nearby",min_value=0,value=0)

st.divider()


X = [[bedrooms,bathrooms,livingarea,condition,numberofschools]]

predictionbutton = st.button("Predict!")

model = joblib.load("model.pkl")

if predictionbutton:
    X_array = np.array(X)
    predictionbutton = model.predict(X_array)

    st.write(f"Prediction is {predictionbutton}")


else:
    st.write("Please use predict button after entering values")
