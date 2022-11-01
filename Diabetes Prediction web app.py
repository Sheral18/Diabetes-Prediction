# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 18:57:24 2022

@author: 91913
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('D:/CISCO/trained_model.sav','rb'))

#creating a function for Prediction

def diabetes_prediction(input_data) :
  #  input_data = (5,166,72,19,175,25.8,0.587,51)

    # Change the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
def main():
    #giving title
    st.title('Diabetes Prediction Web App')
    
    # getting input data from user
    Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    
    BloodPressure = st.text_input('Blood Pressure')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    
    BMI = st.text_input('BMI Value')
    
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunctio')
    Age = st.text_input('Age value')
    
    #code for Prediction
    
    diagnosis = ''
    
    #creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)
    
    
    
if __name__ == '_main_':
    main()