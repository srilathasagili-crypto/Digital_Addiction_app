import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("digital_addiction_model.pkl")

st.set_page_config(
    page_title="Digital Addiction Prediction",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Digital Addiction Prediction")
st.write("Enter the details below to predict Academic Work Impact.")

st.markdown("---")

# -----------------------------
# User Inputs
# -----------------------------

age = st.number_input("Age", 10, 100, 20)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

daily_screen_time_hours = st.number_input(
    "Daily Screen Time (Hours)",
    0.0,
    24.0,
    5.0
)

social_media_hours = st.number_input(
    "Social Media Hours",
    0.0,
    24.0,
    2.0
)

gaming_hours = st.number_input(
    "Gaming Hours",
    0.0,
    24.0,
    1.0
)

work_study_hours = st.number_input(
    "Work/Study Hours",
    0.0,
    24.0,
    6.0
)

sleep_hours = st.number_input(
    "Sleep Hours",
    0.0,
    24.0,
    7.0
)

notifications_per_day = st.number_input(
    "Notifications Per Day",
    0,
    500,
    100
)

app_opens_per_day = st.number_input(
    "App Opens Per Day",
    0,
    500,
    60
)

weekend_screen_time = st.number_input(
    "Weekend Screen Time",
    0.0,
    24.0,
    7.0
)

stress_level = st.selectbox(
    "Stress Level",
    ["Low", "Medium", "High"]
)

st.markdown("---")

# -----------------------------
# Manual Encoding
# (Change according to LabelEncoder)
# -----------------------------

gender_map = {
    "Female": 0,
    "Male": 1
}

stress_map = {
    "High": 0,
    "Low": 1,
    "Medium": 2
}

# Create dataframe
input_data = pd.DataFrame({
    "age": [age],
    "gender": [gender_map[gender]],
    "daily_screen_time_hours": [daily_screen_time_hours],
    "social_media_hours": [social_media_hours],
    "gaming_hours": [gaming_hours],
    "work_study_hours": [work_study_hours],
    "sleep_hours": [sleep_hours],
    "notifications_per_day": [notifications_per_day],
    "app_opens_per_day": [app_opens_per_day],
    "weekend_screen_time": [weekend_screen_time],
    "stress_level": [stress_map[stress_level]]
})

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict"):

    prediction = model.predict(input_data)[0]

    # If target is encoded as 0 and 1
    if prediction == 1:
        st.error("⚠️ Prediction: Addicted")
    else:
        st.success("✅ Prediction: Not Addicted")