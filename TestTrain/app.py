import streamlit as st
import pandas as pd
import joblib

# Load your trained model and preprocessor
model_RF = joblib.load('random_forest_model.pkl')
preprocessor = joblib.load('preprocessor.pkl')


def calculate_bmi(height, weight):
    return weight / (height / 100) ** 2

def get_user_input():
    st.sidebar.header('User Input Parameters')
    
    gender = st.sidebar.radio('Gender', ['Male', 'Female'])
    age = st.sidebar.slider('Age', 0, 100, 50)
    hypertension = st.sidebar.radio('Hypertension', [0, 1])
    heart_disease = st.sidebar.radio('Heart Disease', [0, 1])
    ever_married = st.sidebar.radio('Ever Married?', ['Yes', 'No'])
    work_type = st.sidebar.radio('Work Type', ['Private', 'Self-employed', 'Govt_job', 'Children', 'Never_worked'])
    residence_type = st.sidebar.radio('Residence Type', ['Urban', 'Rural'])
    avg_glucose_level = st.sidebar.slider('Average Glucose Level', 50, 300, 150)
    height = st.sidebar.slider('Height (in cm)', 100, 250, 165)
    weight = st.sidebar.slider('Weight (in kg)', 30, 200, 70)
    bmi = calculate_bmi(height, weight)
    st.sidebar.write("BMI :", bmi)
    smoking_status = st.sidebar.selectbox('Smoking Status', ['never smoked', 'formerly smoked', 'smokes', 'Unknown'])
    
    user_data = {
        'gender': gender,
        'age': age,
        'hypertension': hypertension,
        'heart_disease': heart_disease,
        'ever_married': ever_married,
        'work_type': work_type,
        'Residence_type': residence_type,
        'avg_glucose_level': avg_glucose_level,
        'bmi': bmi,
        'smoking_status': smoking_status
    }
    
    return pd.DataFrame([user_data])

st.image("data/images/loading.png")
st.header('Enter the details in the sidebar to predict if you are at risk of having a stroke.')

user_input = get_user_input()

if st.sidebar.button('Predict Situation'):
    # Preprocess the user input data
    user_input_processed = preprocessor.transform(user_input)
    
    # Predict the outcome using the model
    prediction = model_RF.predict(user_input_processed)
    
    # Display the prediction result
    if prediction == 1:
        st.error('There is a risk of a stroke. Please consult a healthcare professional.')
        st.image("data/images/health_care.png",width=200)
    else:
        st.success('There seems to be a low risk of a stroke. However, always consult with a healthcare professional.')
        st.image("data/images/insurance.png", width=200)
st.write('---')
st.write('Disclaimer: This tool is for predictive purposes only and should not replace professional medical advice.')
