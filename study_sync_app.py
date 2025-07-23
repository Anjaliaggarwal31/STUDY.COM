import streamlit as st
import pandas as pd

# Initialize session state
if 'points' not in st.session_state:
    st.session_state.points = 0
if 'registered' not in st.session_state:
    st.session_state.registered = False

st.set_page_config(page_title="Study Sync", layout="wide")
st.markdown("""
    <style>
        body { background-color: #f4f6f7; color: #1a237e; }
        .main, .block-container {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 2rem;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .big-font {
            font-size: 24px !important;
            font-weight: bold;
            color: #1a237e;
        }
    </style>
""", unsafe_allow_html=True)

# Distraction blocker simulation
block_distraction = st.checkbox("🛡️ Block background distractions")
if block_distraction:
    st.warning("Distraction blocker active. You cannot switch apps while studying.")
    confirm = st.radio("Are you sure you want to switch to another app?", ["No", "Yes"])
    if confirm == "Yes":
        st.error("Switching blocked while studying. Please disable blocker to switch.")

# Navigation logic
if not st.session_state.registered:
    page = "Register"
else:
    page = st.selectbox("📂 Choose Section", ["Find Study Partner", "Teacher Registration", "Subscriptions", "Feedback"])

# Student Registration
if page == "Register":
    st.title("📝 Student Registration")
    with st.form("register_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name")
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            level = st.selectbox("Knowledge Level", ["Basic", "Intermediate", "Advanced"])
            goal = st.selectbox("Study Goal", ["Crash Revision", "Detailed Preparation", "Exam Tomorrow", "Concept Clarity"])
            mode = st.selectbox("Study Mode", ["One-to-One", "Group Study"])
            course_type = st.selectbox("Course Type", ["UG", "PG", "Professional (CA, ACCA, CFA, CMA)", "PhD", "Other"])
        with col2:
            language = st.text_input("Preferred Language")
            university = st.selectbox("University", ["IIT", "IIM", "DU", "NSUT", "IIIT-Delhi", "Oxford", "Harvard", "DERI", "MIT", "Other"])
            timezone = st.selectbox("Timezone", ["IST (India)", "EST", "PST", "GMT", "CET", "AEST"])
            duration = st.slider("Daily Study Duration (hours)", 1, 12, 2)
            preferred_subjects = st.text_area("Subjects You Want to Study")
        submit = st.form_submit_button("Register")
        if submit:
            if name and language and preferred_subjects:
                st.session_state.registered = True
                st.session_state.points += 10
                st.success("✅ Registered Successfully! Let's find you a study partner.")
            else:
                st.error("❌ Registration failed. Please complete all fields.")

# Study Partner Matching
if page == "Find Study Partner":
    st.title("🔍 Find Your Study Partner")
    with st.form("match_form"):
        col1, col2 = st.columns(2)
        with col1:
            partner_gender = st.selectbox("Preferred Partner Gender", ["Any", "Male", "Female"])
            partner_level = st.selectbox("Partner's Knowledge Level", ["Any", "Basic", "Intermediate", "Advanced"])
            partner_lang = st.text_input("Preferred Partner Language")
        with col2:
            study_subject = st.text_input("Study Subject")
            mode = st.radio("Study Mode", ["Audio", "Video", "Recording Upload", "Chat Only"])
            time_zone = st.selectbox("Preferred Partner Timezone", ["IST", "EST", "PST", "GMT", "CET", "AEST"])
        matched = st.form_submit_button("Search Partner")
        if matched:
            st.success("🎉 Partner matched successfully based on your preferences!")
            st.info("👥 Matched Partner List:\n- Alex (Advanced, IST)\n- Priya (Intermediate, GMT)")
            st.session_state.points += 20

# Teacher Registration
if page == "Teacher Registration":
    st.title("👨‍🏫 Teacher Registration")
    with st.form("teacher_form"):
        name = st.text_input("Full Name")
        university = st.text_input("University/Institute")
        subject = st.text_input("Subjects you can teach")
        experience = st.slider("Years of Teaching Experience", 0, 40, 2)
        charges = st.text_input("Fee (e.g., ₹500/hour or $20/hour)")
        availability = st.selectbox("Availability", ["Weekdays", "Weekends", "Evenings", "Anytime"])
        submit_teacher = st.form_submit_button("Register as Teacher")
        if submit_teacher:
            if name and university and subject and charges:
                st.success("✅ Teacher registered! Students can now view your profile.")
            else:
                st.error("❌ Registration failed. Please fill all fields.")

# Subscriptions
if page == "Subscriptions":
    st.title("💎 Subscription Plans")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Free Plan")
        st.write("✔ Basic Matching")
        st.write("✔ Weekly Tips")
    with col2:
        st.subheader("Pro Plan ₹499/month")
        st.write("✔ Teacher Access")
        st.write("✔ Mock Tests & Materials")
    with col3:
        st.subheader("Premium $49/year")
        st.write("✔ Job Support")
        st.write("✔ Personalized Feedback")
    if st.button("🚀 Subscribe"):
        st.success("🎯 Subscription successful!")
        st.session_state.points += 50

# Feedback
if page == "Feedback":
    st.title("📢 Feedback")
    with st.form("feedback_form"):
        rating = st.slider("Session Rating", 1, 5, 3)
        comments = st.text_area("Your Comments")
        submitted = st.form_submit_button("Submit Feedback")
        if submitted:
            st.success("✅ Feedback received. Thank you!")
            st.session_state.points += 5

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #1a237e;'>Study smart. Connect. Achieve. 🚀</p>", unsafe_allow_html=True)
