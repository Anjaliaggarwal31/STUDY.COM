import streamlit as st
import time

# Global session state to manage transitions
if 'registered' not in st.session_state:
    st.session_state.registered = False
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'register'  # Directly go to registration

# Dummy partner list for demonstration
partner_list = [
    {"Name": "Alice", "University": "IIT Delhi", "Course": "UG", "Language": "English", "Knowledge Level": "Advanced", "Subject": "Maths", "Time Zone": "GMT+1"},
    {"Name": "Bob", "University": "DERI", "Course": "PG", "Language": "Hindi", "Knowledge Level": "Intermediate", "Subject": "Physics", "Time Zone": "GMT+5.5"},
]

universities = ["DERI", "IIT", "IIM", "International Universities", "Others"]
courses = ["UG", "PG", "Professional", "PhD", "Others"]
subjects = ["Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Others"]
time_zones = ["GMT-12", "GMT-11", "GMT-10", "GMT-9", "GMT-8", "GMT-7", "GMT-6", "GMT-5", "GMT-4", "GMT-3", "GMT-2", "GMT-1", "GMT", "GMT+1", "GMT+2", "GMT+3", "GMT+4", "GMT+5", "GMT+5.5", "GMT+6", "GMT+7", "GMT+8", "GMT+9", "GMT+10", "GMT+11", "GMT+12"]

# Registration interface
def registration():
    st.markdown("<h1 style='text-align: center;'>Student Registration</h1>", unsafe_allow_html=True)
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
    goal = st.selectbox("Study Goal", ["Crash Revision", "Detailed Preparation"])
    language = st.selectbox("Preferred Language", ["English", "Hindi", "Spanish", "French", "Other"])
    if language == "Other":
        language = st.text_input("Please specify language")
    uploaded_file = st.file_uploader("Upload Student ID (Optional)", type=["png", "jpg", "pdf"])
    st.text("OR")
    skip = st.checkbox("Skip for now")

    if st.button("Register Now", key="register_now_center"):
        if name:
            st.session_state.registered = True
            st.session_state.current_page = 'partner'
            st.success(f"🎉 {name}, you have registered successfully!")
            time.sleep(2)
        else:
            st.error("Please enter your name to register.")

# Study Partner Matching interface
def partner_matching():
    st.header("Find Study Partner")
    study_type = st.selectbox("Study Type", ["One-to-One", "Group Study"])
    partner_gender = st.selectbox("Preferred Partner Gender", ["Male", "Female", "Other"])
    partner_level = st.selectbox("Partner's Knowledge Level", ["Beginner", "Intermediate", "Advanced"])
    partner_subject = st.selectbox("Preferred Subject", subjects)
    if partner_subject == "Others":
        partner_subject = st.text_input("Please specify the subject")
    partner_language = st.selectbox("Preferred Language", ["English", "Hindi", "Spanish", "French"])
    partner_timezone = st.selectbox("Partner's Time Zone", time_zones)

    if st.button("Find Partner"):
        st.success("Matching with partners...")
        time.sleep(2)
        st.subheader("Partner List")
        for partner in partner_list:
            st.markdown(f"**{partner['Name']}** from **{partner['University']}** - {partner['Course']} | Subject: {partner['Subject']} | Language: {partner['Language']} | Knowledge Level: {partner['Knowledge Level']} | Time Zone: {partner['Time Zone']}")

# Subscription Plans
def subscription_plans():
    st.header("Subscription Plans (₹)")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Basic Plan")
        st.markdown("Free Access to Study Partner Matching")
        if st.button("Choose Basic", key="basic_plan"):
            st.success("You have subscribed to the Basic Plan!")

    with col2:
        st.subheader("Premium Plan")
        st.markdown("₹499 - Access to Teachers + Study Planner + Reminders")
        if st.button("Choose Premium", key="premium_plan"):
            method = st.selectbox("Payment Method", ["UPI", "Bank Transfer", "Net Banking"], key="premium_payment")
            st.success(f"You have chosen the Premium Plan. Pay via {method} to proceed.")

    with col3:
        st.subheader("Elite Plan")
        st.markdown("₹999 - Premium + Job Placement + Certificate + Feedback Sessions")
        if st.button("Choose Elite", key="elite_plan"):
            method = st.selectbox("Payment Method", ["UPI", "Bank Transfer", "Net Banking"], key="elite_payment")
            st.success(f"You have chosen the Elite Plan. Pay via {method} to proceed.")

# Teacher Registration interface
def teacher_registration():
    st.header("Teacher Registration")
    name = st.text_input("Full Name", key="teacher_name")
    subject = st.selectbox("Subject Expertise", subjects, key="teacher_subject")
    hourly_fee = st.selectbox("Teaching Fee (per hour)", ["₹100", "₹250", "₹500", "₹1000"], key="teacher_fee")
    duration = st.selectbox("Preferred Teaching Duration", ["1 hour", "2 hours", "3 hours"], key="teacher_duration")
    university = st.selectbox("University", universities, key="teacher_uni")
    if university == "Others":
        university = st.text_input("Please specify your university", key="teacher_uni_other")
    working_status = st.selectbox("Currently Working?", ["Yes", "No"], key="teacher_status")
    uploaded_file = st.file_uploader("Upload Teacher ID", type=["png", "jpg", "pdf"], key="teacher_id")

    if st.button("Register as Teacher", key="register_teacher"):
        if name:
            st.success(f"{name}, you are successfully registered as a Teacher!")
        else:
            st.error("Please enter your full name")

# Main rendering logic
if st.session_state.current_page == 'register':
    registration()
elif st.session_state.current_page == 'partner':
    partner_matching()

# Always display subscription and teacher registration on main interface
st.markdown("---")
subscription_plans()
st.markdown("---")
teacher_registration()
