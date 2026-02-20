# 🏋️ Personalized Workout & Diet Planner with AI

An AI-powered web application that generates **personalized workout routines and diet plans** for students based on their lifestyle, goals, cultural food preferences, and available resources.

Built using **Streamlit + Gemini API**, this project focuses on practical, budget-friendly fitness recommendations tailored for Indian students.

---

## 🚀 Features

* Personalized workout plans (based on goals & time availability)
* Indian diet recommendations (veg / non-veg / regional)
* Budget-aware meal suggestions
* Live BMI calculation
* Daily calorie estimation
* AI-generated weekly schedule
* Downloadable PDF fitness report
* Clean and interactive Streamlit UI

---

## 🧠 Tech Stack

| Layer          | Technology        |
| -------------- | ----------------- |
| Frontend       | Streamlit         |
| AI Engine      | Google Gemini API |
| Backend        | Python            |
| PDF Generation | ReportLab         |
| Environment    | python-dotenv     |
| Data Handling  | Pandas            |

---

## 📂 Project Structure

fitness_ai_app/
│
├── app.py                
├── ai_engine.py          
├── utils.py              
├── pdf_generator.py      
├── requirements.txt               
└── README.md

---

## ⚙️ Installation & Setup

### 1️⃣ Create Virtual Environment

python -m venv venv

Activate it:

**Windows**
venv\Scripts\activate

---

### 2️⃣ Install Dependencies

pip install -r requirements.txt

---

### 3️⃣ Run the Application

streamlit run app.py

---

## 📊 How It Works

1. User enters personal details → BMI calculated instantly
2. Lifestyle + diet preferences collected
3. Gemini AI generates customized workout & meal plan
4. System estimates calories & structures recommendations
5. User downloads a formatted PDF fitness report

---

## 🎯 Use Case

Unlike generic fitness apps, this system:

* Considers **student budgets**
* Supports **Indian food habits**
* Works with **limited equipment**
* Generates **practical, real-life routines**

---

## 🔮 Future Improvements

* Structured table outputs instead of text
* Progress tracking dashboard
* Database for user history
* Visual analytics (calorie/macronutrient charts)

---


