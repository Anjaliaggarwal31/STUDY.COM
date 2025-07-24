import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="StudySync App", layout="wide")

# Session initialization
def init_session():
    if "registered" not in st.session_state:
        st.session_state.registered = False
    if "matched" not in st.session_state:
        st.session_state.matched = False
    if "partners" not in st.session_state:
        st.session_state.partners = []
    if "menu" not in st.session_state:
        st.session_state.menu = "🏠 Home"
    if "partner_filters" not in st.session_state:
        st.session_state.partner_filters = {}
init_session()

# Header and quote
st.markdown("""
    <h1 style='text-align: center;'>🚀 StudySync</h1>
    <h4 style='text-align: center; color: gray;'>"Study alone if you must, but find your tribe and learn faster."</h4>
""", unsafe_allow_html=True)

# Sidebar navigation
menu = st.sidebar.radio("📌 Navigation", 
    ["🏠 Home", "📝 Register", "🤝 Find a Partner", "💼 Subscription Plans", "👩‍🏫 Teacher Registration", "🎯 Matched Partners"],
    index=["🏠 Home", "📝 Register", "🤝 Find a Partner", "💼 Subscription Plans", "👩‍🏫 Teacher Registration", "🎯 Matched Partners"].index(st.session_state.menu)
)
st.session_state.menu = menu

# Generate realistic dummy partners
def generate_dummy_partners():
    names = ["Disha", "Kartik", "Harsh", "Mehak", "Aarav", "Anaya", "Ishaan", "Riya", "Kabir", "Tanvi", "Yash", "Sneha", "Ved", "Simran"]
    genders = ["Male", "Female"]
    knowledge_levels = ["Beginner", "Intermediate", "Advanced"]
    subjects = ["Maths", "Science", "English", "CS", "Economics", "Accounts"]
    languages = ["English", "Hindi"]
    timezones = ["IST", "UTC", "EST", "PST"]

    data = []
    for _ in range(30):
        data.append({
            "Name": random.choice(names),
            "Gender": random.choice(genders),
            "Knowledge": random.choice(knowledge_levels),
            "Subject": random.choice(subjects),
            "TimeZone": random.choice(timezones),
            "Language": random.choice(languages)
        })
    return pd.DataFrame(data)

# 🏠 Home
if menu == "🏠 Home":
    st.success("Welcome to StudySync — your personalized study buddy matcher! 🎓")
    st.info("Use the sidebar to register, find a study partner, or explore subscriptions.")

# 📝 Register
if menu == "📝 Register":
    with st.form("register_form"):
        name = st.text_input("Full Name *")
        email = st.text_input("Email *")

        gender = st.selectbox("Gender *", ["Select an option", "Male", "Female", "Others"])
        gender_other = st.text_input("Please specify your gender *") if gender == "Others" else ""
        final_gender = gender_other if gender == "Others" else gender

        university = st.selectbox("University *", ["Select an option", "IIT", "IIM", "NIT", "DERI", "International", "Others"])
        university_other = st.text_input("Please specify your university *") if university == "Others" else ""
        final_university = university_other if university == "Others" else university

        course = st.selectbox("Course *", ["Select an option", "UG", "PG", "Professional", "PhD", "Others"])
        course_other = st.text_input("Please specify your course *") if course == "Others" else ""
        final_course = course_other if course == "Others" else course

        timezone = st.selectbox("Time Zone *", ["Select an option", "IST", "UTC", "EST", "PST", "Others"])
        timezone_other = st.text_input("Please specify your time zone *") if timezone == "Others" else ""
        final_timezone = timezone_other if timezone == "Others" else timezone

        study_goal = st.multiselect("Your Study Goal *", ["Crash Course", "Detailed Preparation", "Exam Tomorrow", "Professional Exam", "Competitive Exam", "Others"])
        custom_goal = st.text_input("Please specify your goal *") if "Others" in study_goal else ""

        language = st.selectbox("Preferred Language *", ["Select an option", "English", "Hindi", "Other"])
        language_other = st.text_input("Please specify your language *") if language == "Other" else ""
        final_language = language_other if language == "Other" else language

        mode = st.multiselect("Preferred Study Mode", ["Video 🎥", "Audio 🎧", "Notes 📄", "Chat 💬"])
        uploaded_id = st.file_uploader("Upload Your ID *")

        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.registered = True
            st.success("🎉 Registration successful! Taking you to partner finder...")
            st.session_state.menu = "🤝 Find a Partner"
            st.rerun()

# 🤝 Partner Match
if menu == "🤝 Find a Partner":
    with st.form("find_partner_form"):
        partner_gender = st.selectbox("Preferred Partner Gender", ["Any", "Male", "Female", "Others"])
        partner_gender_other = st.text_input("Please specify partner gender *") if partner_gender == "Others" else ""
        final_partner_gender = partner_gender_other if partner_gender == "Others" else partner_gender

        partner_knowledge = st.selectbox("Partner's Knowledge Level", ["Beginner", "Intermediate", "Advanced"])

        subject = st.selectbox("Subject to Study Together *", ["Maths", "Science", "English", "CS", "Economics", "Accounts", "Others"])
        subject_other = st.text_input("Please specify the subject *") if subject == "Others" else ""
        final_subject = subject_other if subject == "Others" else subject

        partner_language = st.selectbox("Partner's Preferred Language", ["English", "Hindi", "Other"])
        partner_language_other = st.text_input("Please specify partner language *") if partner_language == "Other" else ""
        final_partner_language = partner_language_other if partner_language == "Other" else partner_language

        partner_timezone = st.selectbox("Partner's Time Zone", ["IST", "UTC", "EST", "PST", "Others"])
        partner_timezone_other = st.text_input("Please specify partner time zone *") if partner_timezone == "Others" else ""
        final_partner_timezone = partner_timezone_other if partner_timezone == "Others" else partner_timezone

        partner_submit = st.form_submit_button("Find Matches")

        if partner_submit:
            df = generate_dummy_partners()

            # Apply full filtering
            filtered_df = df[
                ((df.Gender == final_partner_gender) | (final_partner_gender == "Any")) &
                (df.Knowledge == partner_knowledge) &
                (df.Subject.str.lower() == final_subject.lower()) &
                (df.Language == final_partner_language) &
                (df.TimeZone == final_partner_timezone)
            ]

            # Loosen filter if empty
            if filtered_df.empty:
                filtered_df = df[
                    ((df.Gender == final_partner_gender) | (final_partner_gender == "Any")) &
                    (df.Knowledge == partner_knowledge) &
                    (df.TimeZone == final_partner_timezone)
                ]
            if filtered_df.empty:
                filtered_df = df[df.Knowledge == partner_knowledge].sample(3)

            st.session_state.partners = filtered_df.to_dict("records")
            st.session_state.partner_filters = {
                "Gender": final_partner_gender if final_partner_gender != "Any" else None,
                "Knowledge": partner_knowledge,
                "Subject": final_subject,
                "Language": final_partner_language,
                "TimeZone": final_partner_timezone
            }
            st.session_state.matched = True

            st.success(f"✅ Found {len(filtered_df)} partner(s) matching your preference!")
            st.subheader("🎯 Your Matched Study Partners")

            columns_to_show = ["Name"] + [col for col, val in st.session_state.partner_filters.items() if val]
            st.table(filtered_df[columns_to_show])

# 🎯 Matched Partners List
if menu == "🎯 Matched Partners":
    if st.session_state.partners:
        st.subheader("🎯 Your Matched Study Partners")
        df = pd.DataFrame(st.session_state.partners)
        filters = st.session_state.get("partner_filters", {})
        columns_to_show = ["Name"] + [col for col, val in filters.items() if val]
        st.table(df[columns_to_show])
    else:
        st.info("You don't have any matches yet. Go to 'Find a Partner' to search.")

# 💼 Subscription Plans
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

# 👩‍🏫 Teacher Registration
if menu == "👩‍🏫 Teacher Registration":
    with st.form("teacher_form"):
        t_name = st.text_input("Full Name *")
        t_subject = st.text_input("Subject Expertise *")
        t_fee = st.selectbox("Hourly Teaching Fee", ["₹200", "₹500", "₹1000", "$10", "$20"])
        t_duration = st.selectbox("Available Duration", ["1 hour", "2–3 hours", "Flexible"])
        t_university = st.selectbox("University *", ["IIT", "IIM", "Other"])
        t_university_other = st.text_input("Specify your university *") if t_university == "Other" else ""
        final_t_university = t_university_other if t_university == "Other" else t_university

        t_status = st.radio("Current Working Status", ["Student", "Faculty", "Other"])
        t_status_other = st.text_input("Please specify your status *") if t_status == "Other" else ""
        final_t_status = t_status_other if t_status == "Other" else t_status

        t_id = st.file_uploader("Upload your ID")

        t_submit = st.form_submit_button("Register as Teacher")
        if t_submit:
            st.success("✅ Teacher registered successfully! Your profile will be reviewed.")
