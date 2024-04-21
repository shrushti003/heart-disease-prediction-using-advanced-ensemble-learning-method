# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 22:23:06 2024

@author: Victus
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

#loading asved models 
#breast_cancer = pickle.load(open("C:/Users/Victus/OneDrive/Desktop/kaggle competition dataset/multiple disease prediction/breast_cancer_prediction_model.sav", 'rb'))

diabetes = pickle.load(open("C:/Users/Victus/OneDrive/Desktop/kaggle competition dataset/multiple disease prediction/daibetes_prediction_model.sav", 'rb'))

parkinsons_disease = pickle.load(open("C:/Users/Victus/OneDrive/Desktop/kaggle competition dataset/multiple disease prediction/parkinsons_disease_prediction_model.sav", 'rb'))


#creating the sidebar
with st.sidebar:
    selected = option_menu('multiple disease prediction system',
                           
                           ['diabetes prediction system',
                            'parkinsons disease prediction system'],
                           
                           icons = ['heart-pulse','person-fill'],
                           
                           default_index = 0)
 
#disease predctiction page
if (selected == 'diabetes prediction system'):
    
    #page title 
    st.title('diabetes prediction using ML')
    
    #getting the input data fromt he user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnacies')
        
    with col2:
        Glucose = st.text_input('Glucose Level') 
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure') 
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness') 
        
    with col2:
        Insulin = st.text_input('Insulin level in Blood') 
        
    with col3:
        BMI = st.text_input('Body Mass Index') 
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function') 
        
    with col2:
        Age = st.text_input('Age') 
        
        #code for predictiion
    diab_diagnosis = ''
    #creating a button for prediction 
    
    if st.button('Diabetes test result'):
        diab_prediction = daibetes_prediction_model.predict([['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']])
        if (diab_prediction[0]==1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
        st.success(diab_diagnosis)
        

    
    #page titie
    st.title('breast cancer prediction system using ML')
if (selected =='parkinsons disease prediction system'):
    
    #page title 
    st.title('parkinsons disease prediction system using ML')
    
    #getting the input data fromt he user
    col1, col2, col3 = st.columns(3)
    with col1:
        Fo= st.text_input("MDVPFo(Hz)")
        
    with col2:
        Fhi= st.text_input("MDVPFhi(Hz)") 
        
    with col3:
        Flo= st.text_input("MDVPFlo(Hz)") 
        
    with col1:
        Jitter_percentage = st.text_input("MDVPJitter(%)") 
        
    with col2:
        Jitter_Abs = st.text_input("MDVPJitter(Abs)") 
        
    with col3:
        RAP = st.text_input("RAP") 
        
    with col1:
        PPQ = st.text_input("MDVPPPQ") 
        
    with col2:
        Jitter_DDP = st.text_input("JitterDDP")

    with col3:
         Shimmer = st.text_input("MDVPShimmer") 
        
    with col1:
         Shimmer_dB = st.text_input("MDVPShimmer(dB)") 
         
    with col2:
         APQ3 = st.text_input("APQ3") 

    with col3:
         APQ5 = st.text_input("APQ5")
         
    with col1:
         APQ = st.text_input("APQ") 
     
    with col2:
         DDA = st.text_input(":DDA") 

    with col3:
         NHR = st.text_input("NHR") 
  
    with col1:
        HNR = st.text_input("HNR") 
    
    with col2:
        RPDE = st.text_input("RPDE") 

    with col3:
        DFA = st.text_input("DFA") 
    
    with col1:
        spread1= st.text_input("spread1") 
        
    with col2:
            spread2 = st.text_input("spread2") 

    with col3:
            D2 = st.text_input("D2") 
    
    with col1:
            PPE = st.text_input("PPE")

    #code for predictiion
    parkinsons_diagnosis = ''
    #creating a button for prediction 
    
    if st.button('Diabetes test result'):
        parkinsons_prediction = parkinsons_disease_prediction_model.predict([['Fo','Fhi','Flo','Jitter_percentage','Jitter_Abs','RAP','PPQ',
                                                                              'Jitter_DDP','Shimmer','Shimmer_dB','APQ3','AP5','APQ','DDA','NHR','HNR',
                                                                              'RPDE','DFA','spread1','spread2','D2','PPE']])
        if (parkinsons_prediction[0]==1):
            parkinsons_diagnosis = 'The person has parkinsons disease'
        else:
            parkinsons_diagnosis = 'The person does not have parkinsons disease'
        st.success(parkinsons_diagnosis)
        
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    