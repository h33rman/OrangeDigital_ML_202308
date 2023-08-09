import streamlit as st
import base64
import re


def main():

    # Load the SVG file
    with open("data/images/undraw_medicine_b1ol.svg", 'r') as f:
        svg = f.read()

    # Remove width and height attributes from the SVG
    svg = re.sub(r'(<svg[^>]*?) (width="[^"]*"|height="[^"]*")', r'\1', svg, flags=re.DOTALL)

    # Wrap the SVG in a container and style it to be responsive
    svg_container = f"""
    <div style="width:50%; height:auto; margin-left:auto; margin-right:auto;">
        {svg}
    </div>
    """
    
    # Display the SVG in Streamlit
    st.markdown(svg_container, unsafe_allow_html=True)

    # st.image("data/images/undraw_medicine_b1ol.png", caption='Your Image Caption', use_column_width=True)
    st.title("Welcome to Our Stroke Prediction App")
    st.write("Understanding your risk factors for stroke can help you take proactive steps towards health.")

    # Sidebar: About Patient
    with st.sidebar:
        st.header("About Patient")

        # Gender
        gender = st.selectbox("What is your gender?", ["Male","Female", "Other"])

        # Marriage Situation 
        ever_married = st.selectbox("Have you ever been married?", ["Yes", "No"])


        # Age of the client
        age = st.slider("Enter your age", 1, 100, 40)

        # Height & Weight
        height = st.slider("Your height (cm)", 1, 280, 170)
        weight = st.slider("Your weight (kg)", 1, 280, 75)

        # Calculate BMI
        bmi_avg = float(weight / (height/100)**2)  # converting height from cm to meters
        st.text(f"Your BMI is: {bmi_avg:.2f}")

    # Main screen: Health Information
    st.header("Health Information")

    # Hypertension
    hypertension = st.selectbox("Do you have hypertension?", ["Yes", "No"])

    # Heart Diseases
    heartdisease = st.selectbox("Do you have any heart diseases?", ["Yes", "No"])

    # Work Type
    work_type = st.selectbox("What's your occupation?", ["Private", "Self Employed", "Government", "Children"])

    # Residence Type
    Residence_type = st.selectbox("Where do you reside?", ["Urban","Rural"])

    # Glucose Average
    avg_glucose_level = st.slider("Your average glucose level (mg/dl)", 1, 600, 256)

    # Smoking Status
    smoking_status = st.selectbox("Do you smoke?", ["Yes", "No"])

    st.write("Once you've filled out the above details, click below for your assessment!")
    if st.button("Get My Assessment"):
        # Placeholder result
        st.write("Your stroke risk assessment will appear here!")



main()
