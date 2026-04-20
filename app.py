import streamlit as st
import pandas as pd
import joblib

# Load the trained model
# Make sure 'random_forest_model.pkl' is in the same directory as this app.py file
model = joblib.load('random_forest_model.pkl')

st.title('Salary Prediction App')
st.write('Enter the details below to predict the salary.')

# Input features
education = st.selectbox('Education Level', options=[0, 1, 2, 3], format_func=lambda x: {0: 'High School', 1: 'Bachelor\'s', 2: 'Master\'s', 3: 'PhD'}[x])
experience = st.slider('Years of Experience', 0, 30, 5)
location = st.selectbox('Location', options=[0, 1, 2], format_func=lambda x: {0: 'Rural', 1: 'Urban', 2: 'Suburban'}[x]) # Assuming these are the encoded values
job_title = st.selectbox('Job Title', options=[0, 1, 2, 3], format_func=lambda x: {0: 'Junior Developer', 1: 'Senior Developer', 2: 'Manager', 3: 'Analyst'}[x]) # Assuming these are the encoded values
age = st.slider('Age', 18, 70, 30)
gender = st.selectbox('Gender', options=[0, 1], format_func=lambda x: {0: 'Female', 1: 'Male'}[x]) # Assuming 0 for Female, 1 for Male


if st.button('Predict Salary'):
    # Create a DataFrame from user input
    input_data = pd.DataFrame([[education, experience, location, job_title, age, gender]],
                              columns=['Education', 'Experience', 'Location', 'Job_Title', 'Age', 'Gender'])

    # Make prediction
    prediction = model.predict(input_data)[0]

    st.success(f'The predicted salary is: ${prediction:,.2f}')
