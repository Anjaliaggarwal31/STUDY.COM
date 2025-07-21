import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from datetime import datetime

# Initialize app session
if 'points' not in st.session_state:
    st.session_state.points = 0

# App layout and config
st.set_page_config(page_title="Study Sync", layout="wide")
st.markdown("""
    <style>
        body {
            background-color: #fce4ec;
            color: #880e4f;
        }
        .main, .block-container {
            background-color: #fff0f5;
            border-radius: 10px;
            padding: 2rem;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .big-font {
            font-size: 24px !important;
            font-weight: bold;
            color: #ad1457;
        }
    </style>
""", unsafe_allow_html=True)

# Banner
st.markdown("<h1 style='text-align: center; color: #e91e63;'>🎓 Welcome to Study Sync 🎓</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Your progress matters. Let's make studying fun & collaborative!</p>", unsafe_allow_html=True)

# Side menu
with st.sidebar:
    choice = option_menu("Navigation", ["Home", "Register", "Find Study Partner", "Subscriptions", "Feedback"],
                         icons=['house', 'person', 'people', 'gem', 'chat'], menu_icon="cast", default_index=0)

# Home Page
if choice == "Home":
    st.image("https://cdn.pixabay.com/photo/2015/01/08/18/29/student-593333_1280.jpg", use_container_width=True)
    st.subheader("🏆 Your Trophies and Rewards")
    st.success(f"You've earned {st.session_state.points} points. Keep studying to unlock more!")
    st.markdown("**Tips:** Complete weekly sessions to earn badges and support job placement opportunities.")

# Register
elif choice == "Register":
    st.header("📝 Student Registration")
    with st.form("register_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name")
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            language = st.text_input("Preferred Language")
            level = st.selectbox("Your Knowledge Level", ["Basic", "Intermediate", "Advanced"])
            goal = st.selectbox("Study Goal", ["Crash Revision", "Detailed Preparation", "Exam Tomorrow", "Concept Clarity"])
        with col2:
            college = st.selectbox("Select College", ["IIT Delhi", "DU", "NSUT", "IIIT-Delhi", "Oxford", "Harvard", "MIT"])
            timezone = st.selectbox("Select Timezone", ["IST (India)", "EST (USA)", "PST (USA)", "GMT", "CET", "AEST"])
            duration = st.slider("Study Duration (in hours)", 1, 12, 2)
            preferred_subjects = st.text_area("Subjects You Want to Study")
            id_proof = st.file_uploader("Upload College ID or Verification Document")
        submitted = st.form_submit_button("Register")
        if submitted:
            st.success("🎉 Registered Successfully! Let's match you with your perfect study partner.")
            st.session_state.points += 10

# Match Partner
elif choice == "Find Study Partner":
    st.header("🤝 Find Your Study Partner")
    col1, col2 = st.columns(2)
    with col1:
        preferred_gender = st.selectbox("Preferred Partner Gender", ["Any", "Male", "Female"])
        preferred_language = st.text_input("Preferred Language for Partner")
        level_match = st.selectbox("Partner Knowledge Level", ["Any", "Basic", "Intermediate", "Advanced"])
    with col2:
        common_subject = st.text_input("Study Subject")
        study_mode = st.radio("Study Mode", ["Audio", "Video", "Recording Upload", "Chat Only"])
        time_zone = st.selectbox("Preferred Partner Timezone", ["IST", "EST", "PST", "GMT", "CET", "AEST"])
    if st.button("🔍 Search Partner"):
        st.info("We found a match based on your preferences! Connect securely and start learning.")
        st.success("Partner matched successfully! Did you enjoy studying with them?")
        st.balloons()
        st.session_state.points += 20

# Subscriptions
elif choice == "Subscriptions":
    st.header("💎 Subscription Plans")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Free Plan")
        st.write("✔ Basic Partner Matching")
        st.write("✔ Weekly Study Tips")
    with col2:
        st.subheader("Pro Plan - ₹499/month")
        st.write("✔ All Free Features")
        st.write("✔ Access to Teachers")
        st.write("✔ Practice Materials & Mock Tests")
    with col3:
        st.subheader("Premium Yearly - ₹4999")
        st.write("✔ All Pro Features")
        st.write("✔ Job Placement Support")
        st.write("✔ Personalized Feedback & Reports")
    if st.button("🚀 Subscribe Now"):
        st.success("Subscribed successfully! Unlock your full academic potential.")
        st.session_state.points += 50

# Feedback
elif choice == "Feedback":
    st.header("🗣 Feedback After Group Study")
    with st.form("feedback_form"):
        rating = st.slider("How was your study session?", 1, 5, 3)
        comments = st.text_area("Leave a comment about your partner or session")
        submit_feedback = st.form_submit_button("Submit Feedback")
        if submit_feedback:
            st.success("Thank you for your feedback! 🎓 Keep learning and growing with Study Sync.")
            st.session_state.points += 5

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #6a1b9a;'>Well done! I helped you find a partner and study better. Use your mind. 🚀</p>", unsafe_allow_html=True)
