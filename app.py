from pdf_generator import generate_pdf
import streamlit as st
from ai_engine import generate_plan
from utils import calculate_bmi, calorie_estimator


if "plan" not in st.session_state:
    st.session_state.plan = None

if "user_data" not in st.session_state:
    st.session_state.user_data = None

if "bmi" not in st.session_state:
    st.session_state.bmi = None

if "calories" not in st.session_state:
    st.session_state.calories = None


st.set_page_config(page_title="AI Fitness Planner")

st.title("🏋️ Personalized Workout & Diet Planner (AI)")
st.write("Built for Students — Budget Friendly & Practical")


st.subheader("👤 Personal Info")

age = st.number_input("Age", 18, 60)
gender = st.selectbox("Gender", ["Male", "Female"])

height = st.number_input("Height (cm)", 140, 210)
weight = st.number_input("Weight (kg)", 40, 150)

if height > 0 and weight > 0:
    live_bmi = calculate_bmi(weight, height)

    st.metric("Your BMI", live_bmi)

    if live_bmi < 18.5:
        st.caption("Category: Underweight")
    elif live_bmi < 25:
        st.caption("Category: Normal Weight ✅")
    elif live_bmi < 30:
        st.caption("Category: Overweight")
    else:
        st.caption("Category: Obese")

st.divider()


with st.form("user_form"):

    goal = st.selectbox("Fitness Goal", ["Fat Loss", "Muscle Gain", "Maintain"])

    st.subheader("⏱ Lifestyle")
    time = st.selectbox("Daily Workout Time (minutes)", [20, 30, 40, 60])
    days = st.slider("Days Per Week", 3, 7)

    equipment = st.selectbox(
        "Available Equipment",
        ["None", "Dumbbells", "Resistance Bands", "Gym Access"]
    )

    st.subheader("🍛 Diet Preferences")
    diet = st.selectbox("Diet Type", ["Vegetarian", "Non-Vegetarian", "Eggetarian"])
    budget = st.selectbox("Budget", ["Low", "Medium", "High"])
    region = st.selectbox("Food Preference", ["South Indian", "North Indian", "Mixed"])

    submitted = st.form_submit_button("Generate Plan")


if submitted:
    bmi = calculate_bmi(weight, height)
    calories = calorie_estimator(goal, weight)

    user_data = {
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "goal": goal,
        "time": time,
        "days": days,
        "equipment": equipment,
        "diet": diet,
        "budget": budget,
        "region": region
    }

    st.session_state.user_data = user_data
    st.session_state.bmi = bmi
    st.session_state.calories = calories

    with st.spinner("AI is designing your personalized plan..."):
        st.session_state.plan = generate_plan(user_data)


if st.session_state.plan:

    st.subheader("📊 Your Health Summary")
    st.success(f"Your BMI: {st.session_state.bmi}")
    st.info(f"Estimated Daily Calories Needed: {st.session_state.calories} kcal")

    st.subheader("📋 Your Personalized Plan")
    st.write(st.session_state.plan)


if st.session_state.plan and st.session_state.user_data:

    pdf_file = generate_pdf(
        st.session_state.user_data,
        st.session_state.bmi,
        st.session_state.calories,
        st.session_state.plan
    )

    st.download_button(
        label="📥 Download Plan as PDF",
        data=pdf_file,
        file_name="AI_Fitness_Plan.pdf",
        mime="application/pdf"

    )
