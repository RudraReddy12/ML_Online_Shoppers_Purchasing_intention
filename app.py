import streamlit as st
import joblib
import pandas as pd
import numpy as np

########### load model #################
model = joblib.load('random_forest_customer.pkl')

st.title('Customer Purchase Intention Detection')

st.write('Enter the session details to predict whether customer will purchase or not')

################ user inputs ################

Administrative = st.number_input('Enter Administrative value')
Administrative_Duration = st.number_input('Enter Administrative_Duration value')
Informational = st.number_input('Enter Informational value')
Informational_Duration = st.number_input('Enter Informational_Duration value')
ProductRelated = st.number_input('Enter ProductRelated value')
ProductRelated_Duration = st.number_input('Enter ProductRelated_Duration value')
BounceRates = st.number_input('Enter BounceRates value')
ExitRates = st.number_input('Enter ExitRates value')
PageValues = st.number_input('Enter PageValues value')
SpecialDay = st.number_input('Enter SpecialDay value')
OperatingSystems = st.number_input('Enter OperatingSystems value')
Browser = st.number_input('Enter Browser value')
Region = st.number_input('Enter Region value')
TrafficType = st.number_input('Enter TrafficType value')
Weekend = st.number_input('Weekend (0 = No, 1 = Yes)')

Month = st.selectbox(
    'Month',
    ['Feb','Mar','May','June','Jul','Aug','Sep','Oct','Nov','Dec']
)

Visitor_Type = st.selectbox(
    'Visitor Type',
    ['Returning_Visitor','New_Visitor','Other']
)

############ create dataframe ############

input_data = pd.DataFrame([{
    'Administrative': Administrative,
    'Administrative_Duration': Administrative_Duration,
    'Informational': Informational,
    'Informational_Duration': Informational_Duration,
    'ProductRelated': ProductRelated,
    'ProductRelated_Duration': ProductRelated_Duration,
    'BounceRates': BounceRates,
    'ExitRates': ExitRates,
    'PageValues': PageValues,
    'SpecialDay': SpecialDay,
    'OperatingSystems': OperatingSystems,
    'Browser': Browser,
    'Region': Region,
    'TrafficType': TrafficType,
    'Weekend': Weekend,
    'Month': Month,
    'VisitorType': Visitor_Type
}])

############ prediction ############

if st.button('Predict'):

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader('Prediction Result')

    if prediction == 1:
        st.success("Customer is going to purchase a product")
    else:
        st.error("Customer will not make a purchase")

    st.write(f"Purchase Probability: {probability:.2%}")