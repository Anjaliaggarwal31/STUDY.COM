import streamlit as st
import pandas as pd
from datetime import datetime
from PIL import Image

# ---------------------- Page Config ----------------------
st.set_page_config(page_title="StudySync - Find Your Study Buddy", layout="wide")

# ---------------------- Custom Styling ----------------------
st.markdown("""
    <style>
    .main {
        background-color: #fff0f6;
    }
    .css-1d391kg { background-color: #fce4ec !important; }
    .stButton>button {
        background-color: #ff69b4;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stSelectbox, .stTextInput, .stDateInput, .stFileUploader, .stTimeInput {
        background-color: #fff0f6;
    }
    .big-font {
        font-size: 18px !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------- Header ----------------------
st.markdown("""
    <h1 style='text-align: center; color: #9c27b0;'>🎓 StudySync</h1>
    <h3 style='text-align: center; color: #e91e63;'>Find Study Buddies, Earn Trophies & Enjoy Learning!</h3>
    <p style='text-align: center;'>🏆 Earn points, track your progress, and match with study partners.</p>
""", unsafe_allow_html=True)

st.image("https://cdn.pixabay.com/photo/2017/01/31/17/44/study-2020463_1280.png", use_container_width=True)

# ---------------------- Navigation Menu ----------------------
menu = ["🏠 Dashboard", "📚 Register", "🔐 Login", "🧠 Find Study Partner", "💼 Subscription", "🏫 College Portal"]
choice = st.sidebar.selectbox("Navigate", menu)

# ---------------------- Dashboard ----------------------
if choice == "🏠 Dashboard":
    st.subheader("Welcome to StudySync")
    st.success("Your studies are going strong. Keep going! 🚀")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("📚 Sessions Completed", "23")
        st.metric("🏆 Points Earned", "280")
    with col2:
        st.metric("👥 Partners Matched", "12")
        st.metric("📅 Upcoming Sessions", "3")

    st.image("https://cdn.pixabay.com/photo/2016/09/21/12/39/back-to-school-1683316_1280.png", use_container_width=True)

# ---------------------- Register ----------------------
elif choice == "📚 Register":
    st.header("📄 Create Your StudySync Profile")
    name = st.text_input("👤 Full Name")
    email = st.text_input("📧 Email")
    gender = st.radio("🧑 Gender", ["Male", "Female", "Other", "Prefer not to say"])
    language = st.selectbox("🗣️ Preferred Language", ["English", "Hindi", "Spanish", "French", "German", "Mandarin", "Other"])
    college = st.selectbox("🏫 Your College", [
        "IIT Delhi", "SRCC Delhi", "St. Stephen's", "AIIMS", "Jamia", "JNU",
        "Harvard University", "Cambridge University", "Stanford", "Oxford", "NUS Singapore", "Other"
    ])
    discipline = st.selectbox("🎓 Discipline", ["Engineering", "Science", "Commerce", "Arts", "Law", "Medical"])
    subjects = st.multiselect("📘 Subjects You Want to Study", [
        "Python", "Statistics", "Data Science", "Marketing", "Economics", "Physics", "AI/ML", "Finance"
    ])
    id_card = st.file_uploader("📎 Upload Your Student ID (PDF/JPEG)")
    password = st.text_input("🔒 Create Password", type="password")

    if st.button("🚀 Register Now"):
        st.success(f"Welcome {name}! You're now part of StudySync 🎉")

# ---------------------- Login ----------------------
elif choice == "🔐 Login":
    st.header("🔐 Login to StudySync")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.success("You're logged in! Ready to study 💪")

# ---------------------- Find Study Partner ----------------------
elif choice == "🧠 Find Study Partner":
    st.header("🎯 Match With a Study Partner or Group")
    subject = st.selectbox("📘 Subject You Want to Study", [
        "Python", "Statistics", "AI/ML", "Marketing", "Finance", "Economics", "Physics", "Math"
    ])
    discipline = st.selectbox("🎓 Your Discipline", ["Engineering", "Science", "Commerce", "Arts", "Medical"])
    gender_pref = st.radio("👥 Preferred Gender of Study Partner", ["Any", "Male", "Female", "Other"])
    language_pref = st.selectbox("🗣️ Preferred Language for Communication", ["English", "Hindi", "Spanish", "French", "German", "Mandarin", "Other"])
    knowledge_level = st.selectbox("📊 Your Knowledge Level", ["Beginner", "Intermediate", "Advanced"])
    goal = st.radio("🎯 Your Study Goal", ["Competitive Exam Prep", "Course Exams", "Skill Development", "Others"])
    time = st.time_input("🕒 Preferred Study Time")
    mode = st.radio("Mode", ["1-on-1 Partner", "Group Study"])
    ready_now = st.checkbox("✅ I'm Ready to Study Now")

    if st.button("🔍 Find a Study Partner"):
        st.success(f"🎉 Match found for {subject} at {time.strftime('%I:%M %p')} with preferred language {language_pref} and level {knowledge_level}!")
        st.markdown("""
        **Partner Match:**
        - 👤 Name: Priya Singh
        - 📘 Subject: Python
        - 🎓 Discipline: Engineering
        - 🕒 Time: 6:00 PM
        - 🧑 Gender: Female
        - 🗣️ Language: English
        - 📊 Level: Intermediate
        """)
        st.button("💬 Connect with Priya")

    if st.button("✅ I studied today!"):
        st.success("Well done! You've earned 10 points 🏅")
        feedback = st.text_area("📣 Share how your session went")
        st.button("📩 Submit Feedback")

    suggestion = st.text_area("💡 Suggest what would make StudySync better")
    if st.button("Submit Suggestion"):
        st.success("Thanks! Your feedback will help us improve the app.")

# ---------------------- Subscription ----------------------
elif choice == "💼 Subscription":
    st.header("💼 Choose a Subscription Plan")
    plan = st.radio("📦 Choose Your Plan", ["Free - 1 Year", "Premium - ₹999/year"])
    if plan == "Premium - ₹999/year":
        st.markdown("""
        **💎 Premium Benefits Include:**
        - 🧑‍🏫 Teacher Assistance
        - 📈 Job/Placement Support
        - ✅ Verified Partner Matching
        - 🎓 College Discounts
        """)
        upload = st.file_uploader("📎 Upload Valid Student ID")
        st.button("💳 Proceed to Payment")

# ---------------------- College Portal ----------------------
elif choice == "🏫 College Portal":
    st.header("📬 Request Onboarding of Your College")
    cname = st.text_input("🏫 College Name")
    email = st.text_input("📧 Official College Email")
    discount = st.slider("🎁 Discount for Your Students (%)", 0, 50, 10)
    doc = st.file_uploader("📄 Upload College Affiliation Certificate")
    if st.button("Submit College Request"):
        if cname and doc:
            st.success(f"🎉 Thank you! {cname} has been submitted for onboarding.")
        else:
            st.warning("❗ Please upload required document and fill all fields.")

# ---------------------- Footer ----------------------
st.markdown("""
    <hr>
    <p style='text-align: center;'>
        🧠 "Use your mind, make the most of your time!" <br>
        🎉 Did you enjoy studying with your partner? Keep going, champion!<br>
        📬 support@studysync.com <br>
        ❤️ StudySync - Built with love to make your learning fun!
    </p>
""", unsafe_allow_html=True)
