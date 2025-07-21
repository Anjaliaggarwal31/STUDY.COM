import streamlit as st
import pandas as pd
from datetime import datetime
from PIL import Image

# ---------------------- Page Configuration ----------------------
st.set_page_config(page_title="StudySync - Find Your Study Buddy", layout="wide")

# ---------------------- Branding ----------------------
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
    }
    .stSelectbox, .stTextInput, .stDateInput, .stFileUploader, .stTimeInput {
        background-color: #fff0f6;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------- App Header ----------------------
st.markdown("""
    <h1 style='text-align: center; color: #9c27b0;'>🎓 StudySync</h1>
    <h3 style='text-align: center; color: #e91e63;'>Find Study Buddies, Track Your Progress, and Enjoy Learning!</h3>
    <p style='text-align: center;'>🏆 Earn points for studying, give feedback, and build your academic network!</p>
""", unsafe_allow_html=True)

st.image("https://cdn.pixabay.com/photo/2017/01/31/17/44/study-2020463_1280.png", use_column_width=True)

# ---------------------- Sidebar ----------------------
menu = ["🏠 Dashboard", "📚 Register", "🔐 Login", "🧠 Find Study Partner", "💼 Subscription", "🏫 College Portal"]
choice = st.sidebar.selectbox("Navigate", menu)

# ---------------------- Dashboard ----------------------
if choice == "🏠 Dashboard":
    st.subheader("Welcome to StudySync")
    st.success("Your studies are going strong. Keep going! ✨")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("📚 Sessions Completed", "23")
        st.metric("🏆 Points Earned", "280")
    with col2:
        st.metric("👥 Partners Matched", "12")
        st.metric("📅 Upcoming Sessions", "3")

    st.image("https://cdn.pixabay.com/photo/2016/09/21/12/39/back-to-school-1683316_1280.png", use_column_width=True)

# ---------------------- Register ----------------------
elif choice == "📚 Register":
    st.header("Create Your Free StudySync Account")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    college = st.selectbox("Your College", [
        "IIT Delhi", "SRCC Delhi", "St. Stephen's College", "AIIMS Delhi", "JNU", 
        "Harvard University", "University of Cambridge", "NUS Singapore", "Other"
    ])
    discipline = st.selectbox("Discipline", ["Engineering", "Science", "Commerce", "Arts", "Law", "Medical"])
    subjects = st.multiselect("Subjects You Want to Study", [
        "Python", "Statistics", "Data Science", "Marketing", "Economics", "Physics", "AI/ML", "Finance"
    ])
    id_card = st.file_uploader("Upload Your Student ID (PDF/JPEG)")
    password = st.text_input("Create Password", type="password")

    if st.button("Register Now"):
        st.success(f"Welcome, {name}! You've joined StudySync 🎉")

# ---------------------- Login ----------------------
elif choice == "🔐 Login":
    st.header("Login to Your StudySync Account")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.success("You're now logged in. Welcome back!")

# ---------------------- Find Study Partner ----------------------
elif choice == "🧠 Find Study Partner":
    st.header("Match With a Study Partner or Group")
    subject = st.selectbox("Subject You Want to Study", [
        "Python", "Statistics", "AI/ML", "Marketing", "Finance", "Economics", "Physics", "Math"
    ])
    discipline = st.selectbox("Your Discipline", ["Engineering", "Science", "Commerce", "Arts", "Medical"])
    time = st.time_input("Your Preferred Study Time")
    mode = st.radio("Mode", ["1-on-1 Partner", "Group Study"])
    ready_now = st.checkbox("✅ I'm Ready to Study Now")

    if st.button("🔍 Find a Partner/Group"):
        st.success(f"Great! We've found a {mode} for {subject} at {time.strftime('%I:%M %p')}")
        st.markdown("""
        **Partner Found:**
        - 👤 Name: Priya Singh
        - 📘 Subject: Python
        - 🧠 Discipline: Engineering
        - 🕒 Time: 6:00 PM
        """)
        st.button("Connect with Priya")

    if st.button("✅ I studied today!"):
        st.success("Well done! You've earned 10 points. Did you enjoy studying with your partner?")
        feedback = st.text_area("Write a short feedback about the session")
        st.button("Submit Feedback")

    suggestion = st.text_area("🎯 Who would be your ideal partner? What features should we add?")
    if st.button("💡 Submit Suggestion"):
        st.success("Thanks for the suggestion! We'll try to make your next study experience even better.")

# ---------------------- Subscription ----------------------
elif choice == "💼 Subscription":
    st.header("Upgrade for Premium Features")
    plan = st.radio("Choose a Plan", ["Free - 1 Year", "Premium - ₹999/year"])
    if plan == "Premium - ₹999/year":
        st.markdown("""
        **Premium Includes:**
        - 🧑‍🏫 Teacher Assistance
        - 📈 Job/Placement Support
        - ✅ Verified Matching
        - 🎓 Discounts for Partner Colleges
        """)
        upload = st.file_uploader("Upload Valid Student ID")
        st.button("Proceed to Payment")

# ---------------------- College Portal ----------------------
elif choice == "🏫 College Portal":
    st.header("Onboard Your College to StudySync")
    cname = st.text_input("College Name")
    email = st.text_input("Official College Email")
    discount = st.slider("Discount for Your Students (%)", 0, 50, 10)
    doc = st.file_uploader("Upload College Affiliation Certificate")
    if st.button("Submit College Request"):
        if cname and doc:
            st.success(f"Thanks! {cname} has been submitted for onboarding.")
        else:
            st.warning("Please upload the required document and fill all details.")

# ---------------------- Footer ----------------------
st.markdown("""
    <hr>
    <p style='text-align: center;'>
        💡 "Use your mind, make the most of your time!" <br>
        🚀 StudySync - Designed to make your learning journey more joyful and social. <br>
        📬 support@studysync.com
    </p>
""", unsafe_allow_html=True)
