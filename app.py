import streamlit as st
import pandas as pd
import joblib

# Load your trained model and preprocessor
model = joblib.load('knn_model.pkl')
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
    
    # Get height and weight to calculate BMI
    height = st.sidebar.slider('Height (in cm)', 100, 250, 165)
    weight = st.sidebar.slider('Weight (in kg)', 30, 200, 70)
    bmi = calculate_bmi(height, weight)
    st.sidebar.write("BMI :", bmi)
    
    smoking_status = st.sidebar.selectbox('Smoking Status', ['never smoked', 'formerly smoked', 'smokes', 'Unknown'])
    
    # Create a data frame with the input values
    user_data = pd.DataFrame({
        'gender': [gender],
        'age': [age],
        'hypertension': [hypertension],
        'heart_disease': [heart_disease],
        'ever_married': [ever_married],
        'work_type': [work_type],
        'Residence_type': [residence_type],
        'avg_glucose_level': [avg_glucose_level],
        'bmi': [bmi],
        'smoking_status': [smoking_status]
    })
    
    return user_data

# App title and description
st.title('Stroke Prediction App')
st.write('Enter the details in the sidebar to predict if you are at risk of having a stroke.')

# Get user input
user_input = get_user_input()

# Display button to make prediction
if st.sidebar.button('Predict'):
    # Process user input data
    processed_input = preprocessor.transform(user_input)
    
    # Predict the outcome using the model
    prediction = model.predict(processed_input)
    
    # Display the prediction result
    if prediction == 1:
        st.error('Based on the data provided, there is a risk of a stroke. Please consult a healthcare professional.')
    else:
        st.success('Based on the data provided, there seems to be a low risk of a stroke. However, always consult with a healthcare professional for a complete assessment.')

st.write('---')
st.write('Disclaimer: This tool is for predictive purposes only and should not replace professional medical advice.')
