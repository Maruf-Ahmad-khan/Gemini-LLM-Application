import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
import streamlit as st
import pickle
import numpy as np

import streamlit as st
import pickle
import numpy as np

# Load the pre-trained electric car linear regression model
with open(r"C:\Users\mk744\Downloads\Car price\lr_model_wout.pkl", "rb") as file:
    elr_model = pickle.load(file)

# Streamlit app title
st.title("Electric Car Price Prediction")

# Input fields for car features
st.header("Input Car Features")

engine_size = st.number_input("Engine Size (in cc)", min_value=500, max_value=10000, value=2000)
curb_weight = st.number_input("Curb Weight (in kg)", min_value=500, max_value=3000, value=1500)
horsepower = st.number_input("Horsepower", min_value=50, max_value=1000, value=300)
city_mpg = st.number_input("City MPG", min_value=5, max_value=100, value=30)
highway_mpg = st.number_input("Highway MPG", min_value=5, max_value=100, value=40)

# Create a button for prediction
if st.button("Predict Price"):
    # Prepare the input data as a 2D array for prediction
    input_data = np.array([[engine_size, curb_weight, horsepower, city_mpg, highway_mpg]])
    
    # Predict the car price using the loaded model
    predicted_price = elr_model.predict(input_data)[0]
    
    # Display the result
    st.success(f"The predicted price of the electric car is: ${predicted_price:,.2f}")

