import streamlit as st
import pandas as pd

st.set_page_config(page_title="StudySync", layout="wide")

# ---- SESSION STATE INIT ----
if "registered" not in st.session_state:
    st.session_state.registered = False
if "show_partner_form" not in st.session_state:
    st.session_state.show_partner_form = False
if "partner_data" not in st.session_state:
    # Add some sample data
    st.session_state.partner_data = pd.DataFrame([
        {"Name": "Sneha", "Gender": "Female", "Education Level": "UG", "Preferred Study Language": "Hindi", "Study Type": "Crash Revision", "Subject": "Math", "Knowledge Level": "Intermediate", "Partner Gender Preference": "Male", "Time Zone": "IST", "Preferred Mode": "Video 🎥", "Goal": "Exam Tomorrow", "Additional Info": "Quick sessions needed"},
        {"Name": "Harsh", "Gender": "Male", "Education Level": "PG", "Preferred Study Language": "English", "Study Type": "Detailed Preparation", "Subject": "Science", "Knowledge Level": "Advanced", "Partner Gender Preference": "Female", "Time Zone": "IST", "Preferred Mode": "Audio 🎧", "Goal": "Competitive Exam", "Additional Info": "Looking for focused study"},
        {"Name": "Ankita", "Gender": "Female", "Education Level": "PhD", "Preferred Study Language": "English", "Study Type": "Crash Revision", "Subject": "History", "Knowledge Level": "Beginner", "Partner Gender Preference": "No Preference", "Time Zone": "UTC", "Preferred Mode": "Chat 💬", "Goal": "Crash Course", "Additional Info": "Group study preferred"},
    ])

# ---- SIDEBAR ----
st.sidebar.title("📌 Menu")
menu_option = st.sidebar.radio("Select an option:", ["Home", "Register", "Find a Study Partner", "Teacher Assistant", "Subscription", "Feedback"])

# ---- HOME PAGE ----
if menu_option == "Home":
    st.markdown("<h1 style='text-align: center;'>📖 StudySync</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Study Together, Succeed Together!</h4>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.success("Welcome to the StudySync Home. Use the sidebar to explore features.")

# ---- REGISTRATION ----
elif menu_option == "Register":
    st.header("🎓 Student Registration")

    with st.form("register_form"):
        name = st.text_input("Full Name *", key="name")
        email = st.text_input("Email *")
        gender = st.selectbox("Gender *", ["Male", "Female", "Others"])
        if gender == "Others":
            gender_specify = st.text_input("Please specify your gender")

        university = st.selectbox("University *", ["IIT", "IIM", "NIT", "DERI", "International", "Others"])
        if university == "Others":
            university_other = st.text_input("Please specify your university")

        course = st.selectbox("Course *", ["UG", "PG", "Professional", "PhD", "Others"])
        if course == "Others":
            course_other = st.text_input("Please specify your course")

        timezone = st.selectbox("Time Zone *", ["IST", "UTC", "EST", "PST", "Others"])
        if timezone == "Others":
            timezone_other = st.text_input("Please specify your time zone")

        study_goal = st.multiselect("Your Study Goal *", ["Crash Course", "Detailed Preparation", "Exam Tomorrow", "Professional Exam", "Competitive Exam", "Others"])
        if "Others" in study_goal:
            goal_other = st.text_input("Please specify your goal")

        mode_pref = st.multiselect("Preferred Study Mode", ["Video 🎥", "Audio 🎧", "Notes 📄", "Chat 💬"])
        uploaded_id = st.file_uploader("Upload Your ID")

        submitted = st.form_submit_button("Submit")

        if submitted:
            if name.strip() == "":
                st.error("Please enter your name")
            else:
                st.success(f"✅ {name}, you have registered successfully!")
                st.balloons()
                st.session_state.registered = True
                st.session_state.show_partner_form = True

# ---- PARTNER MATCHING ----
elif menu_option == "Find a Study Partner" and st.session_state.registered:
    st.header("🤝 Find a Study Partner")

    with st.form("partner_form"):
        pname = st.text_input("Your Name *", key="pname")
        pgender = st.selectbox("Your Gender", ["Male", "Female", "Others"])
        if pgender == "Others":
            pgender_specify = st.text_input("Please specify your gender")

        education = st.selectbox("Your Education Level", ["UG", "PG", "PhD", "Others"])
        if education == "Others":
            education_other = st.text_input("Please specify education level")

        lang = st.selectbox("Preferred Study Language", ["English", "Hindi", "Other"])
        if lang == "Other":
            lang_specify = st.text_input("Please specify language")

        study_type = st.selectbox("Study Type", ["Crash Revision", "Detailed Preparation", "Exam Tomorrow"])

        subject = st.selectbox("Subject", ["Math", "Science", "English", "History", "Other"])
        if subject == "Other":
            subject_specify = st.text_input("Please specify subject")

        level = st.selectbox("Knowledge Level", ["Beginner", "Intermediate", "Advanced"])
        pgender_pref = st.selectbox("Preferred Partner Gender", ["No Preference", "Male", "Female", "Others"])

        timezone = st.selectbox("Partner Time Zone", ["IST", "UTC", "EST", "PST", "Others"])
        if timezone == "Others":
            tz_specify = st.text_input("Please specify partner's time zone")

        mode = st.multiselect("Preferred Mode", ["Video 🎥", "Audio 🎧", "Notes 📄", "Chat 💬"])

        goal = st.selectbox("Study Goal", ["Crash Course", "Detailed Preparation", "Exam Tomorrow", "Competitive Exam", "Others"])
        if goal == "Others":
            goal_other = st.text_input("Please specify goal")

        info = st.text_area("Additional Info (Optional)")

        submit_partner = st.form_submit_button("Save Partner Preferences")

        if submit_partner:
            new_row = pd.DataFrame([{
                "Name": pname,
                "Gender": pgender,
                "Education Level": education,
                "Preferred Study Language": lang,
                "Study Type": study_type,
                "Subject": subject,
                "Knowledge Level": level,
                "Partner Gender Preference": pgender_pref,
                "Time Zone": timezone,
                "Preferred Mode": ", ".join(mode),
                "Goal": goal,
                "Additional Info": info
            }])
            st.session_state.partner_data = pd.concat([st.session_state.partner_data, new_row], ignore_index=True)
            st.success("✅ Partner preferences saved!")

    st.subheader("📋 Matching Partners")
    st.dataframe(st.session_state.partner_data)

# ---- TEACHER ASSISTANT ----
elif menu_option == "Teacher Assistant":
    st.header("👩‍🏫 Teacher Registration")
    with st.form("teacher_form"):
        tname = st.text_input("Your Name *")
        subject = st.selectbox("Subject Expertise", ["Math", "Science", "English", "Others"])
        if subject == "Others":
            subject_other = st.text_input("Please specify subject")
        fee = st.selectbox("Teaching Fee Per Hour", ["Free", "$5", "$10", "$20+", "Others"])
        if fee == "Others":
            fee_other = st.text_input("Please specify fee")
        duration = st.selectbox("Available Duration", ["1 hour", "2 hours", "3+ hours"])
        university = st.text_input("University")
        current_status = st.selectbox("Current Status", ["Student", "Professional", "Others"])
        if current_status == "Others":
            status_other = st.text_input("Please specify current status")
        id_upload = st.file_uploader("Upload Your Teacher ID")

        submit_teacher = st.form_submit_button("Register as Teacher")

        if submit_teacher:
            st.success(f"🎉 {tname}, you have registered as a teacher!")
            st.markdown("### 🧑‍🎓 Students Available to Teach")
            st.dataframe(st.session_state.partner_data)

# ---- SUBSCRIPTION ----
elif menu_option == "Subscription":
    st.header("💼 Subscription Plans")
    st.info("Basic is Free. Upgrade for more features.")

    plan = st.radio("Choose Your Plan:", ["Basic", "Premium", "Elite", "Elite+"])

    if plan == "Basic":
        st.success("🎉 You're on the Basic Plan.")
        st.markdown("""
        - 👥 Limited Partner Matching  
        - ❌ No Teacher Support  
        - ❌ No Priority Access  
        - ❌ Limited Devices  
        """)
    elif plan == "Premium":
        st.warning("💳 Premium Plan Benefits:")
        st.markdown("""
        - ✅ Partner Priority Matching  
        - ✅ Teacher Assistance  
        - ✅ Use Across Devices  
        - ✅ Register for Your Children  
        - ✅ Block Distractions with Study Mode  
        """)
    elif plan == "Elite":
        st.info("💎 Elite Plan Includes All Premium Features Plus:")
        st.markdown("""
        - 🔒 Verified Teacher Sessions  
        - 🎯 Dedicated Study Mentors  
        - 🧾 Detailed Progress Reports  
        - 💼 Job Prep & Support  
        """)
    elif plan == "Elite+":
        st.success("🚀 Elite+ Plan Includes Everything + More:")
        st.markdown("""
        - 🌐 International Collaboration  
        - 🧠 AI-Based Study Plans  
        - 📞 24x7 Personal Coach  
        - 🛡️ Secure Encrypted Study Rooms  
        """)

    if plan != "Basic":
        payment_mode = st.selectbox("Payment Mode", ["UPI", "Net Banking", "Credit/Debit Card", "Bank Transfer"])
        st.button("Proceed to Pay")

# ---- FEEDBACK ----
elif menu_option == "Feedback":
    st.header("🗣️ We Value Your Feedback")
    feedback = st.text_area("How can we improve StudySync?")
    rating = st.slider("Rate Your Experience", 1, 5, 3)
    if st.button("Submit Feedback"):
        st.success("✅ Thank you for your feedback!")
