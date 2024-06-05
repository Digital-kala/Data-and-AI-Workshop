# Import required libraries
import streamlit as st
from utils import PrepProcesor, columns
import numpy as np
import pandas as pd
import joblib

# Set Streamlit page configuration
st.set_page_config(layout="wide", page_title="Titanic Survival Prediction", page_icon=":ship:")

# Load the pre-trained XGBoost model pipeline
model = joblib.load('xgbpipe.joblib')

# Create a subheader on the page with a custom divider color
st.subheader('Will you survive the Titanic? :ship:', divider="red")

# Dictionary mapping class labels to numerical codes
ticket_classes = {
    'Upper Class': 1,
    'Middle Class': 2,
    'Lower Class': 3
}

# Dictionary mapping ports of embarkation to their codes
port_of_embarkation = {
    'Cherbourg': 'C',
    'Queenstown': 'Q',
    'Southampton': 'S'
}

# Add a manual break using markdown for spacing
st.markdown('<br>', unsafe_allow_html=True)

# Create layout with columns for different inputs
col1, _, col2, _, col3 = st.columns([8,1,8,1,8])

# Allow user to select ticket class
pclass = ticket_classes[col1.radio("Choose Ticket Class", ticket_classes.keys(), horizontal=True)]

# Allow user to select gender
sex = col2.radio("Choose a Sex", ['male','female'], horizontal=True)

# Allow user to select port of embarkation
embarked = port_of_embarkation[col3.radio("Choose Port of Embarkation", port_of_embarkation.keys(), horizontal=True)]
st.markdown('<br>', unsafe_allow_html=True)

# More input fields for age, number of siblings/spouses, and number of parents/children
col1, _, col2, _, col3 = st.columns([8,1,8,1,8])
age = col1.slider("Choose Your Age",0,100)
sibsp = col2.slider("Choose the no. of siblings / spouses aboard the Titanic",0,10)
parch = col3.slider("Choose the no. of parents / children aboard the Titanic",0,2)
st.markdown('<br>', unsafe_allow_html=True)

# Input for fare price
fare = st.number_input("Input Fare Price", 0,1000, step=1)

# Add some extra spacing before the prediction button
st.markdown('<br><br>', unsafe_allow_html=True)

# Button to trigger the prediction
trigger = st.button('🤔 &nbsp; Predict')

# Process the prediction if the button is clicked
if trigger:
    # Prepare input data for the model
    row = np.array([np.nan, pclass, np.nan, sex, age, sibsp, parch, np.nan, fare, np.nan, embarked]) 
    X = pd.DataFrame([row], columns=columns)
    
    # Make prediction using the model
    prediction = model.predict(X)[0]
    
    # Display results based on the prediction outcome
    if prediction == 1:
        st.success('You Survived :thumbsup:')
    else:
        st.error('You did not Survive :thumbsdown:')
