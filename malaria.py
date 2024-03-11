import pickle
import streamlit as st
import sys

sys.path.insert(1, "C:/past/your/coppied/path/here/streamlit_option_menu")

from streamlit_option_menu import option_menu
malaria_model = pickle.load(open('malaria_model.sav','rb'))
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Malaria Prediction'],
                          icons=['apple'],
                          default_index=0)
    
    
#Diabetes Prediction Page
if (selected == 'Malaria Prediction'):
    
    # page title
    st.title('Malaria Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
    
    with col3:
        fever = st.text_input('Fever')
    
    with col1:
        cold = st.text_input('Cold')
    
    with col2:
        rigor = st.text_input('Rigor')
    
    with col3:
        fatigue = st.text_input('Fatigue')
    
    with col1:
        headace = st.text_input('Headache')
    
    with col2:
        bitter_tongue = st.text_input('Bitter tongue')
    
    with col3:
        vomitting = st.text_input('Vomiting')
    
    with col1:
        diarrhea= st.text_input('Diarrehea')
    
    with col2:
        Convulsion= st.text_input('Convulsion')
    
    with col3:
        Anemia = st.text_input('Anemia')
    
    with col1:
        jundice = st.text_input('Jaundice')
    
    with col2:
        cocacola_urine = st.text_input('Coco-cola Urine')
    
    with col3:
        hypoglycemia= st.text_input('Hypoglycemia')
    
    with col1:
        prostraction= st.text_input('prostraction')
    
    with col2:
        hyperpyrexia = st.text_input('Hyperpyrexia')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Malaria Test Result'):
        diab_prediction = malaria_model.predict([[age,sex,fever,cold,rigor,fatigue,headace,bitter_tongue,vomitting,diarrhea,Convulsion,Anemia,jundice,cocacola_urine,hypoglycemia,prostraction,hyperpyrexia]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)



