import numpy as np
import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
import pickle

with open("Notebooks/rfc.pkl", "rb") as file:
    model = pickle.load(file)


import streamlit as st

st.markdown('''
             Gender - 1 for Male ,0 for Female --|\n
             All other columns 1 stands with Yes and 0 stands with No --|\n
             MultipleLines feature 0:No,1:No phone service,2:Yes --|\n
             InternetService 0:DSL,1:Fiber optic,2:No --|\n
             OnlineSecurity 0:FiberOptic,1:No,2:Yes --|\n
             OnlineBackup  0:No,1:No internet service,2:Yes --|\n
             DeviceProtection  0:No,1:No internet service,2:Yes --|\n
             contract  0:month-month ,1 :One year, 2: Two year --|\n
             PaymentMethod 0:Bank transfer(automatic),1:Credit card (automatic),2:Electronic check,3:Mailed check --|
             ''')
with st.form("my_form"):
   st.write("Inside the form")
   Tenure = st.slider('Tenure', 1, 100)
   monthly_charges = st.slider('MonthlyCharges',1,150)
   total_charges = st.slider('TotalCharges',1,10000)
   gender = st.selectbox('Gender', [1,0],placeholder='Male 1, Female 0')
   SeniorCitizen = st.selectbox('SeniorCitizen', [1,0],placeholder='Male 1, Female 0')

   partner = st.selectbox('Partner', [1,0])
   dependents = st.selectbox('Dependents', [1,0])
   phoneservice = st.selectbox('PhoneService', [1,0])
   multiplelines = st.selectbox('MultipleLines', [2,1,0])
   InternetService = st.selectbox('InternetService', [2,1,0])
 
   OnlineSecurity = st.selectbox('onlinesecurity', [2,1,0])
   OnlineBackup = st.selectbox('onlinebackup', [2,1,0])
   DeviceProtection = st.selectbox('device protection',[2,1,0])
   TechSupport = st.selectbox('Tech Support', [2,1,0])
   StreamingTV = st.selectbox('Streaming TV', [2,1,0])

   StreamingMovies = st.selectbox('Streaming Movies', [2,1,0])
   Contract = st.selectbox('Contract', [2,1,0])
   PaperlessBilling = st.selectbox('PaperlessBilling', [1,0])
   PaymentMethod = st.selectbox('PaymentMethod', [3,2,1,0])


   submit_button = st.form_submit_button('Submit my picks')

   if submit_button:
       
       res = ss.fit_transform(np.array([Tenure,monthly_charges,total_charges]).reshape(3,1))
       inputs = list(res.reshape(3,))

       others = [gender,SeniorCitizen,partner,dependents,phoneservice,multiplelines,InternetService,
                 OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,
                 StreamingMovies,Contract,PaperlessBilling,PaymentMethod]
       
       inputs.extend(others)

       result = model.predict(np.array(inputs).reshape(1,19))
       if result==0:
           st.write("The customer won't churn")
       else:
           st.write("The customer will churn")

