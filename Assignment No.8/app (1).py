import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# App title
st.title("Diabetes Prediction System using Logistic Regression")
st.sidebar.header("Enter Patient Details")
# User inputs
Pregnancies = st.number_input("Pregnancies")
Glucose = st.number_input("Glucose")
BloodPressure = st.number_input("BloodPressure")
SkinThickness = st.number_input("SkinThickness")
Insulin = st.number_input("Insulin")
BMI = st.number_input("BMI")
DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction")
Age = st.number_input("Age")

# Input dataframe
input_data = pd.DataFrame({
    'Pregnancies':[Pregnancies],
    'Glucose':[Glucose],
    'BloodPressure':[BloodPressure],
    'SkinThickness':[SkinThickness],
    'Insulin':[Insulin],
    'BMI':[BMI],
    'DiabetesPedigreeFunction':[DiabetesPedigreeFunction],
    'Age':[Age]
})

# Prediction
prediction = model.predict(input_data)

# Output
if st.button("Predict"):

    if prediction[0] == 1:
        st.error("Patient is Diabetic")

    else:
        st.success("Patient is Not Diabetic")