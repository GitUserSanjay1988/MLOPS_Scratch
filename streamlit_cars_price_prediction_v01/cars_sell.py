import streamlit as st 
import pandas as pd 
import numpy as np 
import datetime 
import pickle

st.header('Selling Price Prediction')

def model_pred(input):
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
        return(model.predict(input))
        
  
def transform_input(model_year,km_driven,model_mileage,engine_capacity,max_power,seats,seller_type,fuel_type,transmission):

    if km_driven >= 0 and km_driven <= 1000:
        km_driven = 0
    elif km_driven > 1000 and km_driven <= 25000:
        km_driven = 1
    elif km_driven > 25000 and km_driven <= 50000:
        km_driven = 2
    elif km_driven > 50000 and km_driven <= 75000:
        km_driven = 3
    elif km_driven > 75000 and km_driven <= 100000:
        km_driven = 4
    else:
        km_driven = 5
    
    mileage = model_mileage
    
    engine = engine_capacity 
    
    max_power = max_power
    
    seats = seats
    
    car_age = pd.Timestamp.today().year - model_year
    
    if seller_type == 'Individual':
        seller_type_Individual = 1
        seller_type_Dealer = 0
        seller_type_TrustmarkDealer = 0
    elif seller_type == 'Dealer':
        seller_type_Individual = 0
        seller_type_Dealer = 1
        seller_type_TrustmarkDealer = 0
    else:
        seller_type_Individual = 0
        seller_type_Dealer = 0
        seller_type_TrustmarkDealer = 1
    
    if fuel_type == 'Petrol':
        fuel_type_CNG = 0
        fuel_type_Diesel = 0
        fuel_type_Electric = 0
        fuel_type_Petrol = 1
        fuel_type_LPG = 0
    elif fuel_type == 'CNG':
        fuel_type_CNG = 1
        fuel_type_Diesel = 0
        fuel_type_Electric = 0
        fuel_type_Petrol = 0
        fuel_type_LPG = 0
    elif fuel_type == 'Diesel':
        fuel_type_CNG = 0
        fuel_type_Diesel = 1
        fuel_type_Electric = 0
        fuel_type_Petrol = 0
        fuel_type_LPG = 0
    elif fuel_type == 'Electric':
        fuel_type_CNG = 0
        fuel_type_Diesel = 0
        fuel_type_Electric = 1
        fuel_type_Petrol = 0
        fuel_type_LPG = 0
    else:
        fuel_type_CNG = 0
        fuel_type_Diesel = 0
        fuel_type_Electric = 0
        fuel_type_Petrol = 0
        fuel_type_LPG = 1
    
    if transmission == 'Automatic':
        transmission_type_Manual = 0
        transmission_type_Automatic = 1
    else:
        transmission_type_Manual = 1
        transmission_type_Automatic = 0
    
    return [[km_driven,mileage,engine,max_power,seats,car_age,
              seller_type_Dealer,seller_type_Individual,seller_type_TrustmarkDealer,
              fuel_type_CNG,fuel_type_Diesel,fuel_type_Electric,fuel_type_LPG,fuel_type_Petrol,
              transmission_type_Automatic,transmission_type_Manual]]

with st.form('my_form'):
    
    model_year = st.slider('Model Year',2009, 2023)
    engine_capacity = st.slider('Cubic Capacity',800, 6000)
    model_mileage = st.slider('Mileage',0, 35)
    km_driven = st.number_input('Kilometers Driven')
    max_power = st.slider('Power (HP)',5, 500)
    seats = st.slider('Seating Capacity',2, 14)
    seller_type = st.selectbox('Seller Type: ', ['Individual', 'Dealer', 'TrustmarkDealer'])
    fuel_type = st.selectbox('Fuel Type: ', ['Petrol', 'Diesel', 'Electric', 'LPG', 'CNG'])
    transmission = st.selectbox('Transmission: ', ['Manual', 'Automatic'])

    if st.form_submit_button('Predict'):
        input = transform_input(model_year,km_driven,model_mileage,engine_capacity,max_power,seats,seller_type,fuel_type,transmission)
        st.write(model_pred(input))
  


 