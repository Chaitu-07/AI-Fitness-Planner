import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use supported model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_plan(user_data):
    prompt = f"""
You are a certified fitness trainer and Indian nutrition expert.

Create a personalized workout and diet plan for a college student.

Profile:
Age: {user_data['age']}
Gender: {user_data['gender']}
Height: {user_data['height']} cm
Weight: {user_data['weight']} kg
Goal: {user_data['goal']}
Workout Time: {user_data['time']} minutes/day
Workout Days: {user_data['days']} days/week
Equipment: {user_data['equipment']}
Diet Type: {user_data['diet']}
Budget: {user_data['budget']}
Region Preference: {user_data['region']}

Requirements:
- Keep workouts simple and practical.
- Use Indian, budget-friendly foods.
- No supplements.
- Give weekly workout split.
- Provide full-day meal plan.
- Mention approximate calories.
- Format clearly using headings and bullet points.
"""

    response = model.generate_content(prompt)

    return response.text