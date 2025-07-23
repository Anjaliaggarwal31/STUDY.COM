# STUDYSYNC FULL APP - STREAMLIT
import streamlit as st
import time
from datetime import datetime

# ----------------- APP CONFIGURATION -----------------
st.set_page_config(page_title="StudySync", layout="centered")

# ----------------- INITIAL SPLASH SCREEN -----------------
def splash_screen():
    st.markdown("""
        <h1 style='text-align: center; font-size: 60px;'>📘 StudySync</h1>
        <p style='text-align: center; font-size: 20px;'>"Empowering Students Through Smart Collaboration"</p>
    """, unsafe_allow_html=True)
    time.sleep(2)

# ----------------- TIMEZONES -----------------
timezones = [
    "Indian Standard Time (IST)", "Pacific Standard Time (PST)",
    "Eastern Standard Time (EST)", "Central European Time (CET)",
    "Greenwich Mean Time (GMT)", "China Standard Time (CST)",
    "Japan Standard Time (JST)", "Other"
]

# ----------------- LANGUAGES -----------------
languages = ["English", "Hindi", "Spanish", "French", "German", "Chinese", "Arabic", "Other"]

# ----------------- UNIVERSITIES -----------------
universities = ["DERI", "IITs", "IIMs", "Harvard", "Oxford", "Stanford", "Other"]

# ----------------- COURSES -----------------
courses = ["Undergraduate", "Postgraduate", "PhD", "CA", "CFA", "CMA", "ACCA", "Other"]

# ----------------- TEACHER FEE OPTIONS -----------------
fee_options = ["INR 500/month", "INR 1000/month", "USD 20/month", "USD 50/month", "Other"]

# ----------------- SUBSCRIPTION PLANS -----------------
def subscription_plans():
    st.subheader("📦 Subscription Plans")
    plans = {
        "Free": ["Basic Partner Matching", "Daily Study Reminders"],
        "Premium - ₹499/month": ["Access to Teachers", "Job Placement Support", "Detailed Preparation Modes"],
        "Elite - ₹999/month": ["One-on-One Coaching", "Distraction Blocker", "Certificate of Collaboration"]
    }
    for plan, benefits in plans.items():
        with st.expander(plan):
            for b in benefits:
                st.markdown(f"- {b}")

# ----------------- STUDENT REGISTRATION -----------------
def student_registration():
    st.subheader("👨‍🎓 Student Registration")
    with st.form("student_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        gender = st.radio("Gender", ["Male", "Female", "Other"])
        timezone = st.selectbox("Your Time Zone", timezones)
        university = st.selectbox("Your University", universities)
        course = st.selectbox("Course Type", courses)
        id_upload = st.file_uploader("Upload Student ID (PDF or Image)")
        block_distractions = st.checkbox("🔒 Block other activities while studying")
        submitted = st.form_submit_button("Register")

    if submitted:
        if name and email and university:
            st.success("✅ Registration Successful! Redirecting to Partner Matching...")
            time.sleep(2)
            st.session_state.registered = True
        else:
            st.error("❌ Please fill all required fields.")

# ----------------- PARTNER MATCHING -----------------
def partner_matching():
    st.subheader("🔍 Find a Study Partner")
    with st.form("partner_form"):
        study_mode = st.radio("Study Mode", ["1-on-1", "Group Study"])
        pref_gender = st.radio("Preferred Partner Gender", ["Any", "Male", "Female"])
        pref_language = st.selectbox("Preferred Language", languages)
        knowledge_level = st.selectbox("Partner Knowledge Level", ["Beginner", "Intermediate", "Advanced"])
        study_goal = st.selectbox("Study Goal", ["Crash Revision", "Detailed Preparation"])
        match = st.form_submit_button("Find Partner")
    if match:
        st.success("🎉 Partner Found Successfully!")
        st.info("Stay consistent for 1 week to unlock achievement badge!")

# ----------------- TEACHER REGISTRATION -----------------
def teacher_registration():
    st.subheader("👩‍🏫 Teacher Registration")
    with st.form("teacher_form"):
        t_name = st.text_input("Teacher Name")
        t_university = st.selectbox("University Affiliation", universities)
        t_subjects = st.text_input("Subjects You Teach")
        t_duration = st.selectbox("Preferred Teaching Duration (daily)", ["1 hour", "2 hours", "3 hours", "Other"])
        t_fee = st.selectbox("Expected Monthly Fee", fee_options)
        t_currency = st.selectbox("Currency", ["INR", "USD", "EUR", "Other"])
        t_available = st.radio("Are you currently available to teach?", ["Yes", "No"])
        t_submit = st.form_submit_button("Register as Teacher")
    if t_submit:
        if t_name and t_subjects:
            st.success("🎓 Teacher Profile Registered Successfully!")
        else:
            st.error("Please provide all required information.")

# ----------------- MAIN INTERFACE FLOW -----------------
def main_app():
    splash_screen()

    if "registered" not in st.session_state:
        student_registration()
    elif st.session_state.registered:
        tab1, tab2, tab3 = st.tabs(["Partner Matching", "Teacher Zone", "Subscriptions"])

        with tab1:
            partner_matching()

        with tab2:
            teacher_registration()

        with tab3:
            subscription_plans()

# ----------------- RUN APP -----------------
main_app()
