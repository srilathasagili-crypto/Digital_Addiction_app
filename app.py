import streamlit as st
import pandas as pd
import joblib

# ----------------------------
# Load trained model
# ----------------------------
model = joblib.load("digital_addiction_model.pkl")

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Digital Addiction Prediction",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Digital Addiction Prediction")
st.write("Enter the details below to predict Digital Addiction.")

st.markdown("---")

# ----------------------------
# Feature Order
# (Must match X.columns exactly)
# ----------------------------
feature_order = [
    'age',
    'gender',
    'daily_screen_time_hours',
    'social_media_hours',
    'gaming_hours',
    'work_study_hours',
    'sleep_hours',
    'notifications_per_day',
    'app_opens_per_day',
    'weekend_screen_time',
    'stress_level',
    'academic_work_impact'
]

# ----------------------------
# Encoding Maps
# ----------------------------
gender_map = {
    "Female": 0,
    "Male": 1
}

stress_map = {
    "High": 0,
    "Low": 1,
    "Medium": 2
}

academic_map = {
    "High": 0,
    "Low": 1,
    "Medium": 2
}

# ----------------------------
# User Inputs
# ----------------------------

age = st.number_input(
    "Age",
    min_value=10,
    max_value=100,
    value=20
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

daily_screen_time_hours = st.number_input(
    "Daily Screen Time (Hours)",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

social_media_hours = st.number_input(
    "Social Media Hours",
    min_value=0.0,
    max_value=24.0,
    value=2.0
)

gaming_hours = st.number_input(
    "Gaming Hours",
    min_value=0.0,
    max_value=24.0,
    value=1.0
)

work_study_hours = st.number_input(
    "Work / Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=6.0
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)

notifications_per_day = st.number_input(
    "Notifications Per Day",
    min_value=0,
    max_value=1000,
    value=100
)

app_opens_per_day = st.number_input(
    "App Opens Per Day",
    min_value=0,
    max_value=1000,
    value=60
)

weekend_screen_time = st.number_input(
    "Weekend Screen Time (Hours)",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)

stress_level = st.selectbox(
    "Stress Level",
    ["Low", "Medium", "High"]
)

academic_work_impact = st.selectbox(
    "Academic Work Impact",
    ["Low", "Medium", "High"]
)

st.markdown("---")

# ----------------------------
# Prediction
# ----------------------------
if st.button("Predict"):

    input_data = pd.DataFrame([[
        age,
        gender_map[gender],
        daily_screen_time_hours,
        social_media_hours,
        gaming_hours,
        work_study_hours,
        sleep_hours,
        notifications_per_day,
        app_opens_per_day,
        weekend_screen_time,
        stress_map[stress_level],
        academic_map[academic_work_impact]
    ]], columns=feature_order)

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Addicted")
    else:
        st.success("✅ Not Addicted")

    st.markdown("---")

    st.write("### Input Summary")
    st.dataframe(input_data)
