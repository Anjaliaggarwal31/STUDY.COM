import streamlit as st
import pandas as pd
import time

# Initialize session state
if 'registered' not in st.session_state:
    st.session_state.registered = False
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'welcome'

# Dummy partner list with realistic names
partner_list = [
    {"Name": "Aarav Mehta", "University": "IIT Delhi", "Course": "UG", "Language": "English", "Knowledge Level": "Advanced", "Subject": "Maths", "Time Zone": "GMT+1"},
    {"Name": "Sara Khan", "University": "DERI", "Course": "PG", "Language": "Hindi", "Knowledge Level": "Intermediate", "Subject": "Physics", "Time Zone": "GMT+5.5"},
]

universities = ["DERI", "IIT", "IIM", "International Universities", "Others"]
courses = ["UG", "PG", "Professional", "PhD", "Others"]
subjects = ["Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Others"]
time_zones = [f"GMT{offset:+}" for offset in range(-12, 13)] + ["GMT+5.5"]

# Welcome screen
def welcome_screen():
    st.markdown("""
        <h1 style='text-align:center; font-size: 50px;'>📘 StudySync</h1>
        <h3 style='text-align:center; color: grey;'>Study Together. Proceed Together. Succeed Together.</h3>
    """, unsafe_allow_html=True)
    st.write("")
    col = st.columns(3)
    with col[1]:
        if st.button("👉 Register Now", key="start_registration"):
            st.session_state.current_page = 'register'

# Registration interface
def registration():
    st.markdown("""<h1 style='text-align: center;'>📝 Student Registration</h1>""", unsafe_allow_html=True)
    with st.form("student_registration_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        timezone = st.selectbox("Your Time Zone", time_zones)
        university = st.selectbox("University", universities)
        if university == "Others":
            university = st.text_input("Please specify your university")
        course = st.selectbox("Course", courses)
        if course == "Others":
            course = st.text_input("Please specify your course")
        goal = st.selectbox("Study Goal", [
            "Crash Revision", "Detailed Preparation", "Exam Tomorrow", "Competitive Exam", "Professional Exam"
        ])
        language = st.selectbox("Preferred Language", ["English", "Hindi", "Spanish", "French", "Other"])
        if language == "Other":
            language = st.text_input("Please specify language")
        uploaded_file = st.file_uploader("Upload Student ID (Optional)", type=["png", "jpg", "pdf"])
        st.text("OR")
        skip = st.checkbox("Skip for now")

        submitted = st.form_submit_button("Register Now")
        if submitted:
            if name:
                st.session_state.registered = True
                st.session_state.current_page = 'menu'
                st.success(f"🎉 {name}, you have registered successfully! 👍")
                time.sleep(2)
            else:
                st.error("Please enter your name to register.")

# Sidebar Menu after registration
def menu():
    st.sidebar.title("📚 Navigation")
    option = st.sidebar.radio("Choose an Option:", [
        "Find a Study Partner", "Teacher Assistant", "Subscription Plans", "Feedback"])

    if option == "Find a Study Partner":
        partner_matching()
    elif option == "Teacher Assistant":
        teacher_registration()
    elif option == "Subscription Plans":
        subscription_plans()
    elif option == "Feedback":
        feedback()

# Study Partner Matching interface
def partner_matching():
    st.header("👫 Find Study Partner")
    st.markdown("> 📌 Stay consistent, your success is one study session away!")
    study_type = st.selectbox("Study Type", ["One-to-One", "Group Study"])
    partner_gender = st.selectbox("Preferred Partner Gender", ["Male", "Female", "Other"])
    partner_level = st.selectbox("Partner's Knowledge Level", ["Beginner", "Intermediate", "Advanced"])
    partner_subject = st.selectbox("Preferred Subject", subjects)
    if partner_subject == "Others":
        partner_subject = st.text_input("Please specify the subject")
    partner_language = st.selectbox("Preferred Language", ["English", "Hindi", "Spanish", "French"])
    partner_timezone = st.selectbox("Partner's Time Zone", time_zones)

    if st.button("🔍 Find Partner"):
        st.success("Matching with partners...")
        time.sleep(2)
        st.subheader("🤝 Matched Partners")
        st.dataframe(pd.DataFrame(partner_list))

# Subscription Plans
def subscription_plans():
    st.header("💳 Subscription Plans (₹)")
    st.markdown("> ✨ Upgrade your access for more features!")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🟢 Basic Plan")
        st.markdown("Free Access to Study Partner Matching")
        if st.button("Choose Basic", key="basic_plan"):
            st.success("✅ You have subscribed to the Basic Plan!")

    with col2:
        st.subheader("🔵 Premium Plan")
        st.markdown("₹499 - Access to Teachers + Study Planner + Reminders")
        if st.button("Choose Premium", key="premium_plan"):
            method = st.selectbox("Payment Method", ["UPI", "Bank Transfer", "Net Banking"], key="premium_payment")
            st.success(f"✅ You have chosen the Premium Plan. Pay via {method} to proceed.")

    with col3:
        st.subheader("🟣 Elite Plan")
        st.markdown("₹999 - Premium + Job Placement + Certificate + Feedback Sessions")
        if st.button("Choose Elite", key="elite_plan"):
            method = st.selectbox("Payment Method", ["UPI", "Bank Transfer", "Net Banking"], key="elite_payment")
            st.success(f"✅ You have chosen the Elite Plan. Pay via {method} to proceed.")

# Teacher Registration interface
def teacher_registration():
    st.header("👩‍🏫 Teacher Registration")
    st.markdown("> 🌟 Great teachers inspire great students.")
    name = st.text_input("Full Name", key="teacher_name")
    subject = st.selectbox("Subject Expertise", subjects, key="teacher_subject")
    if subject == "Others":
        subject = st.text_input("Please specify your subject", key="teacher_subject_other")
    hourly_fee = st.selectbox("Teaching Fee (per hour)", ["₹100", "₹250", "₹500", "₹1000"], key="teacher_fee")
    duration = st.selectbox("Preferred Teaching Duration", ["1 hour", "2 hours", "3 hours"], key="teacher_duration")
    university = st.selectbox("University", universities, key="teacher_uni")
    if university == "Others":
        university = st.text_input("Please specify your university", key="teacher_uni_other")
    working_status = st.selectbox("Currently Working?", ["Yes", "No"], key="teacher_status")
    uploaded_file = st.file_uploader("Upload Teacher ID", type=["png", "jpg", "pdf"], key="teacher_id")

    if st.button("Register as Teacher", key="register_teacher"):
        if name:
            st.success(f"🎓 {name}, you are successfully registered as a Teacher! 👏")
            st.subheader("📢 Are you looking for students? These are the students available to teach:")
            st.dataframe(pd.DataFrame(partner_list))
        else:
            st.error("Please enter your full name")

# Feedback form
def feedback():
    st.header("🗣️ We value your feedback!")
    st.markdown("> 💬 Help us improve your study experience.")
    name = st.text_input("Your Name", key="feedback_name")
    rating = st.slider("Rate your experience", 1, 5)
    comments = st.text_area("Any suggestions or issues?")

    if st.button("📤 Submit Feedback"):
        st.success("🙌 Thank you for your feedback!")

# Page routing
if st.session_state.current_page == 'welcome':
    welcome_screen()
elif st.session_state.current_page == 'register':
    registration()
elif st.session_state.current_page == 'menu':
    menu()
