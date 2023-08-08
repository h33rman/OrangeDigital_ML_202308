import streamlit as st

def main():
    st.title("Welcome to Our Stroke Prediction App")
    st.write("This is a simple example of a Streamlit app.")
    st.write("Please feel free to complete the form to predict your situation.")

    # Gender
    gender = st.sidebar.selectbox("What is your gender?", ["Male","Female", "Other"])
    
    # Mariage Situation 
    ever_married = st.sidebar.selectbox("Have you ever married", ["Yes", "No"])

    # Age of the client
    age = st.sidebar.slider("Enter your age", 1, 100, 40)

    # Hypertension
    hypertension = st.selectbox("Do you have hypertension", ["Yes", "No"])

    # Heart Diseases
    heartdisease = st.selectbox("Do you have Heart Disease", ["Yes", "No"])

    # Work Type
    work_type = st.selectbox("What is your work type", ["Private", "Self Employed", "Government", "Children"])

    # Residence Type
    Residence_type = st.selectbox("Which type of residence do you live", ["Urban","Rural"])

    # Glucose Average
    avg_glucose_level = st.slider("Your Glucose Average in mg/dl", 1, 600, 256)

    # Smoking Status
    smoking_status = st.selectbox("Are you a smoker", ["Yes", "No"])

    height = st.sidebar.slider("Your height in cm", 1, 280, 170)
    weight = st.sidebar.slider("Your weight in kg", 1, 280, 75)
    bmi_avg = float(weight / (height ** 2))
    return
main()