import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="StudySync", layout="wide")

# Initial welcome screen
if "registered" not in st.session_state:
    st.session_state.registered = False
if "show_partner_form" not in st.session_state:
    st.session_state.show_partner_form = False
if "partner_data" not in st.session_state:
    st.session_state.partner_data = pd.DataFrame(columns=[
        "Name", "Gender", "Education Level", "Preferred Study Language", "Study Type",
        "Subject", "Knowledge Level", "Partner Gender Preference", "Time Zone",
        "Preferred Mode", "Goal", "Additional Info"
    ])

# ---------- WELCOME SCREEN ---------- #
if not st.session_state.registered:
    st.markdown("""
        <div style='text-align: center; padding-top: 50px;'>
            <h1 style='font-size: 60px; color: #4CAF50;'>📚 StudySync</h1>
            <h3><i>Study Together, Proceed Together, Succeed Together!</i></h3>
            <br><br>
            <a href="#register">
                <button style='font-size:20px;padding:10px 25px;background-color:#2196F3;border:none;color:white;border-radius:10px;'>🚀 Register Now</button>
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div id='register'></div>", unsafe_allow_html=True)

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
            study_goal_other = st.text_input("Please specify your goal")
        mode_pref = st.multiselect("Preferred Study Mode", ["Video 🎥", "Audio 🎧", "Notes 📄", "Chat 💬"])
        uploaded_id = st.file_uploader("Upload Your ID")
        submitted = st.form_submit_button("Submit")

        if submitted:
            if name.strip() == "":
                st.error("Please fill in your name")
                st.markdown("""
                    <style>
                        input[aria-label='Full Name *'] {
                            border: 2px solid red !important;
                        }
                    </style>
                """, unsafe_allow_html=True)
            else:
                st.success(f"✅ {name}, you have registered successfully!")
                st.balloons()
                st.session_state.registered = True
                st.session_state.show_partner_form = True

# ---------- PARTNER MATCHING ---------- #
if st.session_state.registered and st.session_state.show_partner_form:
    st.sidebar.title("📌 Menu")
    menu_option = st.sidebar.radio("Select an option:", ["Find a Study Partner", "Teacher Assistant", "Subscription", "Feedback"])

    if menu_option == "Find a Study Partner":
        st.header("🤝 Looking for a Partner to Study With")
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

        if not st.session_state.partner_data.empty:
            st.subheader("📋 Matching Partners (AliceBob's Table)")
            if subject == "Math":
                filtered = st.session_state.partner_data[st.session_state.partner_data["Subject"] == "Math"]
                st.dataframe(filtered)
            else:
                st.dataframe(st.session_state.partner_data)

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

    elif menu_option == "Subscription":
        st.header("💼 Subscription Plans")
        st.info("Basic Plan is FREE. Premium & Elite require payment.")

        plan = st.radio("Choose Your Plan:", ["Basic", "Premium", "Elite"])

        if plan == "Basic":
            st.success("🎉 You are subscribed to the Basic Plan (Free)")
        else:
            st.warning("💳 Please choose a payment option below")
            payment_mode = st.selectbox("Payment Mode", ["UPI", "Net Banking", "Bank Transfer"])
            st.button("Proceed to Pay")

    elif menu_option == "Feedback":
        st.header("🗣️ Share Your Feedback")
        feedback = st.text_area("How can we improve StudySync?")
        if st.button("Submit Feedback"):
            st.success("✅ Thanks for your feedback!")
