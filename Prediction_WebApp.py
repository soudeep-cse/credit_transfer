# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 18:45:45 2024

@author: ASUS
"""

import numpy as np
import pickle
import streamlit as st

# Loading the save model
load_model=pickle.load(open("E:/Ml_Course/Ml_Project/Streamlit_Deploy/trained_model.sav", "rb"))


def credt_prediction(input_data):
    
    input_data_as_array= np.asarray(input_data, dtype=float)

    input_data_reshaped = input_data_as_array.reshape(1,-1)

    prediction = load_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==0):
        return "Legit Transfer"
    else:
        return "Fraud Transfer"
        

def main():

    # Title of the web ------ ------->
    st.title("Credit Transfer Web App")
    
    #Getting the input from user
    Time=st.text_input("Enter the time")
    V1=st.text_input("Enter the V1")
    V2=st.text_input("Enter the V2")
    V3=st.text_input("Enter the V3")
    V4=st.text_input("Enter the V4")
    V5=st.text_input("Enter the V5")
    V6=st.text_input("Enter the V6")
    V7=st.text_input("Enter the V7")
    V8=st.text_input("Enter the V8")
    V9=st.text_input("Enter the V9")
    V10=st.text_input("Enter the V10")
    V11=st.text_input("Enter the V11")
    V12=st.text_input("Enter the V12")
    V13=st.text_input("Enter the V13")
    V14=st.text_input("Enter the V14")
    V15=st.text_input("Enter the V15")
    V16=st.text_input("Enter the V16")
    V17=st.text_input("Enter the V17")
    V18=st.text_input("Enter the V18")
    V19=st.text_input("Enter the V19")
    V20=st.text_input("Enter the V20")
    V21=st.text_input("Enter the V21")
    V22=st.text_input("Enter the V22")
    V23=st.text_input("Enter the V23")
    V24=st.text_input("Enter the V24")
    V25=st.text_input("Enter the V25")
    V26=st.text_input("Enter the V26")
    V27=st.text_input("Enter the V27")
    V28=st.text_input("Enter the V28")
    Amount=st.text_input("Enter the Amount")
    
    check=""
    
    if st.button("Credit Transfer Check"):
        check=credt_prediction([Time, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10,V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, Amount])
 
    st.success(check)
    

if __name__=="__main__":
    main()
 
    
 
    
    
    
    















