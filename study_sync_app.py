import streamlit as st
import pandas as pd

st.set_page_config(page_title="StudySync App", layout="wide")

# Session initialization
def init_session():
    if "registered" not in st.session_state:
        st.session_state.registered = False
    if "matched" not in st.session_state:
        st.session_state.matched = False
    if "partners" not in st.session_state:
        st.session_state.partners = []
init_session()

st.markdown("""
    <h1 style='text-align: center;'>🚀 StudySync</h1>
    <h4 style='text-align: center; color: gray;'>"Study alone if you must, but find your tribe and learn faster."</h4>
""", unsafe_allow_html=True)

menu = st.sidebar.selectbox("Navigation", ["🏠 Home", "📝 Register", "🤝 Find a Partner", "💼 Subscription Plans", "👩‍🏫 Teacher Registration", "🎯 Matched Partners"])

# Dummy partner data for matching
def generate_dummy_partners():
    return pd.DataFrame([
        {"Name": "Riya", "Gender": "Female", "Knowledge": "Advanced", "Subject": "Maths", "TimeZone": "IST", "Language": "English"},
        {"Name": "Kunal", "Gender": "Male", "Knowledge": "Beginner", "Subject": "Science", "TimeZone": "EST", "Language": "Hindi"},
        {"Name": "Lara", "Gender": "Female", "Knowledge": "Intermediate", "Subject": "English", "TimeZone": "UTC", "Language": "English"},
        {"Name": "Aman", "Gender": "Male", "Knowledge": "Advanced", "Subject": "CS", "TimeZone": "IST", "Language": "Hindi"},
    ])

# Home Screen
if menu == "🏠 Home":
    st.success("Welcome to StudySync — your personalized study buddy matcher! 🎓")
    st.info("Use the sidebar to register, find a study partner, or explore subscriptions.")

# Registration Form
if menu == "📝 Register":
    with st.form("register_form"):
        name = st.text_input("Full Name *", placeholder="Type your name and press Enter")
        email = st.text_input("Email *", placeholder="Type your email and press Enter")

        gender = st.selectbox("Gender *", ["Select an option", "Male", "Female", "Others"])
        if gender == "Others":
            gender = st.text_input("Please specify your gender *")

        location = st.text_input("Location *")

        university = st.selectbox("University *", ["Select an option", "IIT", "IIM", "NIT", "DERI", "International", "Others"])
        if university == "Others":
            university = st.text_input("Please specify your university *")

        course = st.selectbox("Course *", ["Select an option", "UG", "PG", "Professional", "PhD", "Others"])
        if course == "Others":
            course = st.text_input("Please specify your course *")

        timezone = st.selectbox("Time Zone *", ["Select an option", "IST", "UTC", "EST", "PST", "Others"])
        if timezone == "Others":
            timezone = st.text_input("Please specify your time zone *")

        study_goal = st.multiselect("Your Study Goal *", ["Crash Course", "Detailed Preparation", "Exam Tomorrow", "Professional Exam", "Competitive Exam", "Others"])
        if "Others" in study_goal:
            custom_goal = st.text_input("Please specify your goal *")

        language = st.selectbox("Preferred Language *", ["Select an option", "English", "Hindi", "Other"])
        if language == "Other":
            language = st.text_input("Please specify your language *")

        mode = st.multiselect("Preferred Study Mode", ["Video 🎥", "Audio 🎧", "Notes 📄", "Chat 💬"])
        uploaded_id = st.file_uploader("Upload Your ID *")

        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.registered = True
            st.success("🎉 Registration successful! Proceed to Find a Partner.")

# Find Partner
if menu == "🤝 Find a Partner" and st.session_state.registered:
    with st.form("find_partner_form"):
        partner_gender = st.selectbox("Preferred Partner Gender", ["Any", "Male", "Female", "Others"])
        if partner_gender == "Others":
            partner_gender = st.text_input("Please specify partner gender *")

        partner_knowledge = st.selectbox("Partner's Knowledge Level", ["Beginner", "Intermediate", "Advanced"])
        partner_subject = st.text_input("Subject to Study Together *")
        partner_language = st.selectbox("Partner's Preferred Language", ["English", "Hindi", "Other"])
        if partner_language == "Other":
            partner_language = st.text_input("Please specify partner language *")

        partner_timezone = st.selectbox("Partner's Time Zone", ["IST", "UTC", "EST", "PST", "Others"])
        if partner_timezone == "Others":
            partner_timezone = st.text_input("Please specify partner time zone *")

        partner_submit = st.form_submit_button("Find Matches")

        if partner_submit:
            df = generate_dummy_partners()
            results = df[
                ((df.Gender == partner_gender) | (partner_gender == "Any")) &
                (df.Knowledge == partner_knowledge) &
                (df.Subject.str.contains(partner_subject, case=False)) &
                (df.Language == partner_language) &
                (df.TimeZone == partner_timezone)
            ]
            if not results.empty:
                st.session_state.partners = results.to_dict("records")
                st.success("✅ Match found!")
            else:
                st.warning("No exact match found. Try relaxing filters.")

# Show matched partners
if menu == "🎯 Matched Partners" and st.session_state.partners:
    st.subheader("🎯 Your Matched Study Partners")
    st.table(pd.DataFrame(st.session_state.partners))

# Subscription Plans
if menu == "💼 Subscription Plans":
    st.subheader("💼 Subscription Tiers")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        ### 🟢 Basic Plan — ₹0
        - Find Study Partners
        - Set Goals & Preferences
        - Access Notes
        """)
    with col2:
        st.markdown("""
        ### 🔵 Premium Plan — ₹499
        - Everything in Basic
        - Access to Teachers
        - Chat/Video Support
        - Custom Reminders
        """)
    with col3:
        st.markdown("""
        ### 🔴 Elite Plan — ₹999
        - Everything in Premium
        - Job Placement Assistance
        - Personalized Coaching
        - Certificate of Completion
        """)

# Teacher Registration
if menu == "👩‍🏫 Teacher Registration":
    with st.form("teacher_form"):
        t_name = st.text_input("Full Name *")
        t_subject = st.text_input("Subject Expertise *")
        t_fee = st.selectbox("Hourly Teaching Fee", ["₹200", "₹500", "₹1000", "$10", "$20"])
        t_duration = st.selectbox("Available Duration", ["1 hour", "2–3 hours", "Flexible"])
        t_university = st.selectbox("University *", ["IIT", "IIM", "Other"])
        if t_university == "Other":
            t_university = st.text_input("Specify your university *")
        t_status = st.radio("Current Working Status", ["Student", "Faculty", "Other"])
        if t_status == "Other":
            t_status = st.text_input("Please specify your status *")
        t_id = st.file_uploader("Upload your ID")

        t_submit = st.form_submit_button("Register as Teacher")
        if t_submit:
            st.success("✅ Teacher registered successfully! Your profile will be reviewed.")
