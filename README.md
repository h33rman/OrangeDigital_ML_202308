# Stroke Prediction Web App

The primary purpose of this project is to provide an accessible and user-friendly tool for assessing stroke risk based on individual health parameters. Stroke is a leading cause of death and disability worldwide. Early identification of risk factors and timely intervention can drastically reduce the devastating impacts of this condition. This web application bridges the gap between individuals and preliminary stroke risk assessment, emphasizing the importance of health awareness and proactive measures.

![Stroke Prediction App Screenshot](data/images/loading.jpg)

## Features

- **User-Centric Design**: An intuitive and interactive interface allowing users to easily input health metrics.
- **Real-Time Predictions**: Immediate feedback on stroke risk based on a trained machine learning model.
- **Holistic Data Capture**: Captures a wide range of health data, including age, marital status, smoking habits, and more, ensuring a comprehensive risk assessment.

## Installation & Usage

1. **Clone the repository**:


2. **Set up a virtual environment** (optional but recommended):


3. **Install required packages**:


4. **Run the Streamlit app**:
type : streamlit run app.py



5. Open the app in your browser at `http://localhost:8501`.

## Model

The backbone of this application is the K-Nearest Neighbors (KNN) classifier. It's trained on a dataset comprising various health parameters and their associated stroke outcomes. Data preprocessing includes one-hot encoding for categorical variables and normalization using standard scaling.

## Contributing

Your insights are valuable! Feel free to fork the repository and propose changes through a pull request. For bug reports or suggestions, please open an issue.

