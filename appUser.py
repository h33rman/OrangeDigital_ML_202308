import streamlit as st
import pandas as pd
import joblib

# Load your trained model and preprocessor
model_RF = joblib.load('random_forest_model.pkl')
preprocessor = joblib.load('preprocessor.pkl')


def calculate_bmi(height, weight):
    return weight / (height / 100) ** 2

def get_user_input():
    st.sidebar.title('Remplissez ce formulaire')
    
    gender = st.sidebar.selectbox('Genre', ['Male', 'Female'])
    age = st.sidebar.number_input('Age', min_value=0, max_value= 100, value=25)
    hypertension = st.sidebar.selectbox('Hypertension', ["No", "Yes"])
    heart_disease = st.sidebar.selectbox('Maladie Cardiaque', ["No", "Yes"])
    ever_married = st.sidebar.selectbox('Déjà Marié(e)?', ['Yes', 'No'])
    work_type = st.sidebar.selectbox('Type de  travail', ['Private', 'Self-employed', 'Govt_job', 'Children', 'Never_worked'])
    residence_type = st.sidebar.selectbox('Type de Residence', ['Urban', 'Rural'])
    avg_glucose_level = st.sidebar.number_input('Niveau Moyen de Glucose (mg/dl)', min_value=20.50, max_value=300.50, value=80.50, step=0.01)
    height = st.sidebar.number_input('Taille (in cm)', min_value=3, max_value=280, value=165)
    weight = st.sidebar.number_input('Masse (in kg)', min_value=1.5, max_value=300.5, value=70.50, step=0.01)
    bmi = calculate_bmi(height, weight)
    st.sidebar.markdown(f"<h3 style='text-align: left; color: #f63366;'>BMI: {bmi:.2f}</h3>", unsafe_allow_html=True)
    #st.sidebar.write("BMI :", bmi)
    smoking_status = st.sidebar.selectbox('Fumeur ?', ['never smoked', 'formerly smoked', 'smokes', 'Unknown'])
    
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
st.header("Entrez les détails dans la barre latérale pour prédire si vous risquez d'avoir un AVC")

user_input = get_user_input()

if st.sidebar.button('Prédire la Situation'):
    # Preprocess the user input data
    user_input_processed = preprocessor.transform(user_input)
    
    # Predict the outcome using the model
    prediction = model_RF.predict(user_input_processed)
    
    # Display the prediction result
    if prediction == 1:
        st.error("Risque d'AVC détecté. Consultez un professionnel de santé.")
        st.image("data/images/health_care.png",width=200)
    else:
        st.success("Risque d'AVC semble faible. Néanmoins, consultez toujours un professionnel de santé.")
        st.image("data/images/insurance.png", width=200)

    with st.expander('Informations sur la prévention des AVC') :
        st.markdown("""
        1. **Consultez un médecin** : Pour une évaluation précise du risque d'AVC.
        2. **Maîtrisez votre tension** : Évitez l'hypertension; surveillez votre pression régulièrement.
        3. **Mangez équilibré** : Privilégiez les fruits, légumes, et réduisez sel et graisses.
        4. **Bougez** : L'exercice renforce le cœur et réduit le risque d'AVC.
        5. **Contrôlez votre diabète** : Stabilisez votre glycémie.
        6. **Dites non au tabac** : Fumer augmente le risque d'AVC.
        7. **Modérez l'alcool** : Consommez avec discernement.
        8. **Suivez les directives médicales** : Respectez les prescriptions et conseils de votre médecin.
        """)

st.write('---')
st.write('Disclaimer: This tool is for predictive purposes only and should not replace professional medical advice.')


# Add a footer
st.markdown("""
    <style>
        .footer {
            position: right;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #262730;  # Streamlit's dark theme background color
            color: #ffffff;  # White text color to ensure text is readable
            text-align: center;
            padding-top: 3px;
            padding-bottom: 3px;
        }
    </style>
    <div class="footer">
        <p>Copyright &copy; 2023 E-Indri Team. All Rights Reserved.</p>
    </div>
""", unsafe_allow_html=True)