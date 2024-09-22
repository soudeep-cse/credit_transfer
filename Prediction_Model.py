# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

load_model=pickle.load(open("E:/Ml_Course/Ml_Project/Streamlit_Deploy/trained_model.sav", "rb"))

input_data=(0,-1.3598071336738,-0.0727811733098497,2.53634673796914,1.37815522427443,-0.338320769942518,0.462387777762292,0.239598554061257,0.0986979012610507,0.363786969611213,0.0907941719789316,-0.551599533260813,-0.617800855762348,-0.991389847235408,-0.311169353699879,1.46817697209427,-0.470400525259478,0.207971241929242,0.0257905801985591,0.403992960255733,0.251412098239705,-0.018306777944153,0.277837575558899,-0.110473910188767,0.0669280749146731,0.128539358273528,-0.189114843888824,0.133558376740387,-0.0210530534538215,149.62)

input_data_as_array= np.asarray(input_data, dtype=float)

input_data_reshaped = input_data_as_array.reshape(1,-1)

prediction = load_model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]==0):
  print("Legit Transfer")
else:
  print("Fraud Transfer")