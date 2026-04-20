import streamlit as st
import pandas as pd
import joblib
import os

# -------------------------------
# Load Model Safely
# -------------------------------
BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "random_forest_model.pkl")

try:
    model = joblib.load(model_path)
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# -------------------------------
# App UI
# -------------------------------
st.set_page_config(page_title="Salary Prediction App", page_icon="💰")

st.title("💰 Salary Prediction App")
st.write("Enter the details below to predict the salary.")

# -------------------------------
# Input Features
# -------------------------------
education = st.selectbox(
    "Education Level",
    options=[0, 1, 2, 3],
    format_func=lambda x: {
        0: "High School",
        1: "Bachelor's",
        2: "Master's",
        3: "PhD"
    }[x]
)

experience = st.slider("Years of Experience", 0, 30, 5)

location = st.selectbox(
    "Location",
    options=[0, 1, 2],
    format_func=lambda x: {
        0: "Rural",
        1: "Urban",
        2: "Suburban"
    }[x]
)

job_title = st.selectbox(
    "Job Title",
    options=[0, 1, 2, 3],
    format_func=lambda x: {
        0: "Junior Developer",
        1: "Senior Developer",
        2: "Manager",
        3: "Analyst"
    }[x]
)

age = st.slider("Age", 18, 70, 30)

gender = st.selectbox(
    "Gender",
    options=[0, 1],
    format_func=lambda x: {
        0: "Female",
        1: "Male"
    }[x]
)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Salary"):
    try:
        # Create DataFrame
        input_data = pd.DataFrame(
            [[education, experience, location, job_title, age, gender]],
            columns=["Education", "Experience", "Location", "Job_Title", "Age", "Gender"]
        )

        # Prediction
        prediction = model.predict(input_data)[0]

        st.success(f"💵 Predicted Salary: ${prediction:,.2f}")

    except Exception as e:
        st.error(f"❌ Prediction error: {e}")

# -------------------------------
# Debug (optional - remove later)
# -------------------------------
# st.write("Files in directory:", os.listdir(BASE_DIR))
