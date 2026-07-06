import streamlit as st
import pandas as pd
import joblib

# ----------------------------
# Load trained model
# ----------------------------
model = joblib.load("digital_addiction_model.pkl")

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="Digital Addiction Prediction",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Digital Addiction Prediction App")
st.write("Enter user details to predict addiction level.")

st.markdown("---")

# ----------------------------
# Feature order (VERY IMPORTANT)
# Must match training features EXACTLY
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
    'stress_level'
]

# ----------------------------
# Encoding maps (must match training encoding)
# ----------------------------
gender_map = {
    "Male": 1,
    "Female": 0
}

stress_map = {
    "Low": 1,
    "Medium": 2,
    "High": 0
}

# ----------------------------
# UI Inputs
# ----------------------------
age = st.number_input("Age", 10, 100, 20)

gender = st.selectbox("Gender", ["Male", "Female"])

daily_screen_time_hours = st.number_input("Daily Screen Time (Hours)", 0.0, 24.0, 5.0)

social_media_hours = st.number_input("Social Media Hours", 0.0, 24.0, 2.0)

gaming_hours = st.number_input("Gaming Hours", 0.0, 24.0, 1.0)

work_study_hours = st.number_input("Work/Study Hours", 0.0, 24.0, 6.0)

sleep_hours = st.number_input("Sleep Hours", 0.0, 24.0, 7.0)

notifications_per_day = st.number_input("Notifications Per Day", 0, 500, 100)

app_opens_per_day = st.number_input("App Opens Per Day", 0, 500, 60)

weekend_screen_time = st.number_input("Weekend Screen Time", 0.0, 24.0, 7.0)

stress_level = st.selectbox("Stress Level", ["Low", "Medium", "High"])

st.markdown("---")

# ----------------------------
# Create input dataframe
# ----------------------------
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
    stress_map[stress_level]
]], columns=feature_order)

# ----------------------------
# Prediction
# ----------------------------
if st.button("Predict"):

    prediction = model.predict(input_data)[0]

    # If model is label encoded (0/1 or 0/1/2)
    if prediction == 1:
        st.error("⚠️ Result: Addicted")
    else:
        st.success("✅ Result: Not Addicted")
