import streamlit as st
import pandas as pd
import random
import os

st.set_page_config(page_title="StudySync App", layout="wide")

# ------------------------ Session State Initialization ------------------------ #
def init_session():
    session_defaults = {
        "registered": False,
        "matched": False,
        "teacher_registered": False,
        "user_data": {},
        "teacher_data": {},
        "partners": []
    }
    for key, val in session_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

init_session()

# ------------------------ Helper for 'Others' Handling ------------------------ #
def handle_others(label, options):
    selected = st.selectbox(label, options)
    if selected == "Others":
        specified = st.text_input(f"Please specify your {label.lower()}", key=label)
        if not specified:
            st.warning(f"Please specify your {label.lower()} for 'Others' selection.")
        return specified if specified else None
    return selected

# ------------------------ Welcome Screen ------------------------ #
def welcome_screen():
    st.title("📚 StudySync")
    st.markdown("#### *“Study smarter, not harder – with the right partner!”*")
    st.markdown("---")

# ------------------------ Student Registration ------------------------ #
def student_registration():
    st.subheader("🎓 Student Registration")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])
    location = st.text_input("Location")
    timezone = st.selectbox("Time Zone", ["Select", "IST", "EST", "PST", "CET", "Others"])
    if timezone == "Others":
        timezone = st.text_input("Please specify your Time Zone")
    
    university = handle_others("University", ["Select", "IIT", "IIM", "DERI", "Oxford", "Harvard", "MIT", "Others"])
    course = handle_others("Course", ["Select", "UG", "PG", "PhD", "Professional", "Others"])
    language = handle_others("Preferred Language", ["Select", "English", "Hindi", "Spanish", "French", "Others"])
    study_goal = st.selectbox("Study Goal", ["Select", "Crash Course", "Detailed Preparation", "Exam Revision", "Others"])
    if study_goal == "Others":
        study_goal = st.text_input("Please specify your Study Goal")
    study_mode = st.selectbox("Study Mode", ["Select", "Video", "Audio", "Chat", "Others"])
    if study_mode == "Others":
        study_mode = st.text_input("Please specify your Study Mode")
    id_proof = st.file_uploader("Upload Student ID (PDF/Image)")

    if st.button("Register"):
        mandatory_fields = [name, email, gender, location, timezone, university, course, language, study_goal, study_mode]
        if all(mandatory_fields) and id_proof:
            st.session_state.registered = True
            st.session_state.user_data = {
                "Name": name,
                "Email": email,
                "Gender": gender,
                "Location": location,
                "Time Zone": timezone,
                "University": university,
                "Course": course,
                "Preferred Language": language,
                "Study Goal": study_goal,
                "Study Mode": study_mode,
                "Student ID": id_proof.name
            }
            st.success("Student registered successfully!")
            st.switch_page("Profile")
        else:
            st.error("Please complete all required fields including uploading your ID.")

# ------------------------ Partner Matching ------------------------ #
def find_study_partner():
    st.subheader("🔍 Find a Study Partner")

    study_type = st.selectbox("Study Type", ["Select", "Crash Revision", "Detailed Prep", "Doubt Solving", "Others"])
    if study_type == "Others":
        study_type = st.text_input("Please specify your Study Type")
    
    partner_gender = st.selectbox("Preferred Partner Gender", ["Select", "Any", "Male", "Female", "Other"])
    knowledge_level = st.selectbox("Preferred Partner Level", ["Select", "Beginner", "Intermediate", "Advanced", "Others"])
    if knowledge_level == "Others":
        knowledge_level = st.text_input("Please specify Partner Level")
    
    subject = handle_others("Subject to Study", ["Select", "Math", "Science", "English", "Programming", "Others"])
    language = handle_others("Preferred Study Language", ["Select", "English", "Hindi", "Spanish", "Others"])
    partner_timezone = st.selectbox("Partner Time Zone", ["Select", "IST", "EST", "PST", "CET", "Others"])
    if partner_timezone == "Others":
        partner_timezone = st.text_input("Please specify Partner Time Zone")
    study_hours = st.selectbox("Preferred Study Hours", ["Select", "1-2 hrs", "2-3 hrs", "3-4 hrs", "Others"])
    if study_hours == "Others":
        study_hours = st.text_input("Please specify Study Hours")

    if st.button("Find Partner"):
        if all([study_type, partner_gender, knowledge_level, subject, language, partner_timezone, study_hours]):
            # Generate mock partners
            partners = []
            for i in range(3):
                partners.append({
                    "Name": f"Partner {i+1}",
                    "Gender": partner_gender,
                    "Knowledge Level": knowledge_level,
                    "Subject": subject,
                    "Language": language,
                    "Time Zone": partner_timezone,
                    "Study Hours": study_hours
                })
            st.session_state.matched = True
            st.session_state.partners = partners
            st.success("Partners matched successfully!")
        else:
            st.error("Please complete all partner preference fields.")

# ------------------------ Teacher Registration ------------------------ #
def teacher_registration():
    st.subheader("👩‍🏫 Teacher Registration")

    name = st.text_input("Full Name", key="teacher_name")
    email = st.text_input("Email", key="teacher_email")
    subject = handle_others("Subject Expertise", ["Select", "Math", "Science", "English", "Programming", "Others"])
    course = handle_others("Course Expertise", ["Select", "UG", "PG", "PhD", "Professional", "Others"])
    fee = st.selectbox("Teaching Fee (per hour)", ["Select", "$10", "$20", "$30", "₹500", "₹1000", "Others"])
    if fee == "Others":
        fee = st.text_input("Please specify your Teaching Fee")
    availability = st.selectbox("Availability", ["Select", "1-2 hrs", "2-4 hrs", "4+ hrs", "Others"])
    if availability == "Others":
        availability = st.text_input("Please specify your Availability")
    university = handle_others("University", ["Select", "IIT", "IIM", "DERI", "Oxford", "Harvard", "Others"])
    currently_working = st.selectbox("Are you currently working?", ["Select", "Yes", "No"])
    id_proof = st.file_uploader("Upload Teacher ID (PDF/Image)")

    if st.button("Register as Teacher"):
        mandatory = [name, email, subject, course, fee, availability, university, currently_working, id_proof]
        if all(mandatory):
            st.session_state.teacher_registered = True
            st.session_state.teacher_data = {
                "Name": name,
                "Email": email,
                "Subject Expertise": subject,
                "Course Expertise": course,
                "Fee": fee,
                "Availability": availability,
                "University": university,
                "Currently Working": currently_working,
                "ID": id_proof.name
            }
            st.success("Teacher registered successfully!")
            st.switch_page("Profile")
        else:
            st.error("Please complete all required fields and upload your ID.")

# ------------------------ Subscription Plans ------------------------ #
def subscription_section():
    st.subheader("💎 Subscription Plans")

    plans = {
        "Basic": ["Partner Matching", "Limited Study Hours"],
        "Premium": ["Everything in Basic", "Access to Teachers", "Extended Study Hours"],
        "Elite": ["Everything in Premium", "Job Placement Help", "Priority Matching"]
    }

    for plan, benefits in plans.items():
        st.markdown(f"#### {plan} Plan")
        st.markdown("- " + "\n- ".join(benefits))
        if st.button(f"Subscribe to {plan} Plan"):
            st.success(f"You've subscribed to the {plan} Plan!")

# ------------------------ Profile ------------------------ #
def profile_section():
    st.subheader("👤 Profile")

    if st.session_state.registered:
        st.markdown("### Student Profile")
        for key, val in st.session_state.user_data.items():
            st.write(f"**{key}:** {val}")

    if st.session_state.teacher_registered:
        st.markdown("### Teacher Profile")
        for key, val in st.session_state.teacher_data.items():
            st.write(f"**{key}:** {val}")

    if st.session_state.matched and st.session_state.partners:
        st.markdown("### Matched Partners")
        for p in st.session_state.partners:
            st.markdown("---")
            for key, val in p.items():
                st.write(f"**{key}:** {val}")

# ------------------------ Navigation ------------------------ #
st.sidebar.title("📌 Navigate")
page = st.sidebar.radio("Go to", ["Welcome", "Register", "Find a Partner", "Teacher Section", "Subscription", "Profile"])

if page == "Welcome":
    welcome_screen()
elif page == "Register":
    student_registration()
elif page == "Find a Partner":
    find_study_partner()
elif page == "Teacher Section":
    teacher_registration()
elif page == "Subscription":
    subscription_section()
elif page == "Profile":
    profile_section()
