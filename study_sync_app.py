import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="StudySync", layout="wide")

# Session states
if 'registered' not in st.session_state:
    st.session_state.registered = False
if 'student_name' not in st.session_state:
    st.session_state.student_name = ""

# Helper
def required_field(val, field_label):
    if not val:
        st.markdown(f"<span style='color:red'>* {field_label} is required</span>", unsafe_allow_html=True)
        return False
    return True

# 🎬 Welcome Page
def landing_page():
    st.markdown("<h1 style='text-align: center; color: #2E8B57;'>📚 StudySync</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Study Together, Proceed Together, Succeed Together!</h4>", unsafe_allow_html=True)
    if st.button("🚀 Register Now", use_container_width=True):
        st.session_state.page = "register"

# 🧾 Registration
def student_registration():
    st.title("🎓 Student Registration")
    with st.form("register_form", clear_on_submit=False):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Full Name *", key="name")
            email = st.text_input("Email *")
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            if gender == "Other":
                gender_specify = st.text_input("Please specify gender")

            course = st.selectbox("Course", ["UG", "PG", "PhD", "Professional", "Other"])
            if course == "Other":
                course_specify = st.text_input("Please specify course")

            university = st.selectbox("University", ["IIT", "IIM", "DERI", "International", "Other"])
            if university == "Other":
                uni_specify = st.text_input("Please specify university")

        with col2:
            location = st.text_input("Location")
            timezone = st.selectbox("Time Zone", ["IST", "GMT", "EST", "PST"])
            study_goal = st.selectbox("Study Goal", ["Crash Course", "Exam Tomorrow", "Detailed Prep", "Competitive Exam", "Other"])
            if study_goal == "Other":
                goal_specify = st.text_input("Please specify goal")

            language = st.selectbox("Preferred Language", ["English", "Hindi", "Other"])
            if language == "Other":
                lang_specify = st.text_input("Please specify language")

            study_type = st.multiselect("Study Mode", ["Video", "Audio", "Notes", "Live Chat"])
            id_upload = st.file_uploader("Upload Your ID")

        submitted = st.form_submit_button("✅ Register")

        if submitted:
            if not name or not email:
                required_field(name, "Name")
                required_field(email, "Email")
            else:
                st.session_state.registered = True
                st.session_state.student_name = name
                st.balloons()
                st.success(f"🎉 {name}, you have registered successfully!")
                time.sleep(1)
                st.session_state.page = "partners"

# 🧑‍🤝‍🧑 Partner Matching
def partner_matching():
    st.subheader("🧑‍🤝‍🧑 Find Your Study Partner")
    subject = st.selectbox("Select Subject", ["Math", "Science", "English", "Other"])
    if subject == "Other":
        subject_specify = st.text_input("Please specify subject")

    # Simulated partner data
    partner_df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Chloe", "David", "Esha", "Farhan"],
        "Subject": ["Math", "Math", "Science", "English", "Math", "English"],
        "Study Type": ["Video", "Audio", "Notes", "Live Chat", "Video", "Audio"],
        "Time Zone": ["IST", "EST", "IST", "GMT", "IST", "PST"]
    })

    filtered = partner_df[partner_df["Subject"].str.lower() == subject.lower()]
    st.dataframe(filtered if not filtered.empty else partner_df)

# 👩‍🏫 Teacher Assistant
def teacher_assistant():
    st.subheader("👩‍🏫 Become a Teacher")
    with st.form("teacher_form"):
        name = st.text_input("Full Name *")
        subject = st.selectbox("Subject Expertise", ["Math", "Science", "English", "Other"])
        if subject == "Other":
            subject_other = st.text_input("Please specify subject")

        hourly_fee = st.selectbox("Fee per Hour", ["₹200", "₹500", "₹1000"])
        available_hours = st.selectbox("Available Duration", ["1 Hour", "2 Hours", "3 Hours", "Other"])
        if available_hours == "Other":
            dur = st.text_input("Please specify duration")

        university = st.selectbox("University", ["IIT", "IIM", "Other"])
        if university == "Other":
            university_other = st.text_input("Please specify university")

        working_status = st.radio("Are you currently working?", ["Yes", "No"])
        id_upload = st.file_uploader("Upload Your ID")

        submitted = st.form_submit_button("✅ Submit")

        if submitted:
            if not name:
                required_field(name, "Name")
            else:
                st.success(f"👍 {name}, you're now registered as a teacher!")
                st.info("👨‍🎓 These students are looking for a teacher:")
                students = pd.DataFrame({
                    "Name": ["Arjun", "Bina", "Carlos"],
                    "Subject Needed": ["Math", "Science", "Math"],
                    "Preferred Mode": ["Video", "Audio", "Live Chat"]
                })
                st.table(students)

# 💎 Subscription Plans
def subscription():
    st.subheader("💎 Choose Your Plan")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🟢 Basic (Free)")
        st.markdown("- Access Study Partners\n- Chat Support\n- Notes Sharing")
        st.button("Get Basic")

    with col2:
        st.markdown("### 🔵 Premium ₹499")
        st.markdown("- Teacher Assistant\n- Live Support\n- Video Access")
        if st.button("Get Premium"):
            st.info("💳 Choose Payment Method")
            st.radio("Payment Mode", ["UPI", "Bank Transfer", "Net Banking"])

    with col3:
        st.markdown("### 🟣 Elite ₹999")
        st.markdown("- All Premium Features\n- Job Assistance\n- Certificate Access")
        if st.button("Get Elite"):
            st.info("💳 Choose Payment Mode")
            st.radio("Payment Mode", ["UPI", "Bank Transfer", "Net Banking"])

# ✍️ Feedback
def feedback():
    st.subheader("✍️ Share Your Experience")
    name = st.text_input("Your Name")
    experience = st.selectbox("Overall Experience", ["Excellent", "Good", "Average", "Poor"])
    comments = st.text_area("Any suggestions?")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")

# Main Control
if 'page' not in st.session_state:
    st.session_state.page = "landing"

if st.session_state.page == "landing":
    landing_page()
elif st.session_state.page == "register":
    student_registration()
else:
    with st.sidebar:
        st.markdown("## 📋 Menu")
        menu_choice = st.radio("Go to:", ["🧑‍🤝‍🧑 Partners", "👩‍🏫 Teacher Assistant", "💎 Subscription", "✍️ Feedback"])
    if menu_choice == "🧑‍🤝‍🧑 Partners":
        partner_matching()
    elif menu_choice == "👩‍🏫 Teacher Assistant":
        teacher_assistant()
    elif menu_choice == "💎 Subscription":
        subscription()
    elif menu_choice == "✍️ Feedback":
        feedback()
