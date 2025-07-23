import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="StudySync", layout="centered")

# --- Utility State Variables ---
if "page" not in st.session_state:
    st.session_state.page = "landing"

if "name" not in st.session_state:
    st.session_state.name = ""

# --- Main Navigation Function ---
def navigate_to(page):
    st.session_state.page = page

# --- Landing Page ---
if st.session_state.page == "landing":
    st.markdown("""
        <h1 style='text-align: center; color: #4B9CD3;'>📘 StudySync</h1>
        <h3 style='text-align: center; font-style: italic;'>“Study Together, Proceed Together, Succeed Together.”</h3>
    """, unsafe_allow_html=True)
    if st.button("🚀 Register Now", use_container_width=True):
        navigate_to("register")

# --- Registration Page ---
elif st.session_state.page == "register":
    st.markdown("### 📝 Student Registration")
    with st.form("register_form", clear_on_submit=False):
        name = st.text_input("Full Name *", key="reg_name")
        email = st.text_input("Email Address *")
        gender = st.radio("Gender", ["Male", "Female", "Other"])
        if gender == "Other":
            gender_specify = st.text_input("Please specify gender")

        university = st.selectbox("University", ["IIT", "IIM", "DERI", "International", "Other"])
        if university == "Other":
            univ_other = st.text_input("Please specify university")

        course = st.selectbox("Course", ["UG", "PG", "PhD", "Professional", "Other"])
        if course == "Other":
            course_other = st.text_input("Please specify course")

        timezone = st.selectbox("Your Time Zone", ["IST", "EST", "GMT", "CET", "Other"])
        language = st.selectbox("Preferred Language", ["English", "Hindi", "Other"])
        if language == "Other":
            lang_other = st.text_input("Please specify language")

        goal = st.selectbox("Study Goal", ["Crash Course", "Exam Tomorrow", "Detailed Prep", "Competitive Exam", "Other"])
        if goal == "Other":
            goal_other = st.text_input("Please specify goal")

        id_proof = st.file_uploader("Upload Student ID (PDF or Image)")

        submitted = st.form_submit_button("✅ Submit & Proceed")
        if submitted:
            if not name:
                st.error("Please enter your name to continue.")
                st.markdown(
                    "<style>input#reg_name {border: 2px solid red;}</style>", unsafe_allow_html=True)
            else:
                st.session_state.name = name
                st.success(f"🎉 {name}, you have registered successfully!")
                st.balloons()
                navigate_to("partner")

# --- Sidebar Navigation After Registration ---
else:
    st.sidebar.title("📚 StudySync Menu")
    menu = st.sidebar.radio("Go to", ["🤝 Looking for Partner", "📘 Teacher Assistant", "💎 Subscription Plans", "📬 Feedback"])

    # --- Partner Matching Page ---
    if menu == "🤝 Looking for Partner":
        st.markdown("### 🔍 Looking for a Study Partner")

        study_type = st.radio("Type of Study", ["One-to-One", "Group Study"])
        subject = st.selectbox("Subject", ["Math", "Science", "History", "Economics", "Other"])
        if subject == "Other":
            other_subj = st.text_input("Please specify subject")

        pref_gender = st.selectbox("Preferred Partner Gender", ["Any", "Male", "Female"])
        knowledge_level = st.selectbox("Partner's Knowledge Level", ["Beginner", "Intermediate", "Advanced"])
        lang_pref = st.selectbox("Preferred Language", ["English", "Hindi", "Other"])
        if lang_pref == "Other":
            other_lang = st.text_input("Please specify language")

        tz = st.selectbox("Preferred Time Zone", ["IST", "EST", "CET", "GMT", "Other"])

        modes = st.multiselect("Preferred Study Mode", ["🎥 Video", "🎧 Audio", "📝 Notes", "💬 Chat"])

        st.markdown("#### 🧑‍🤝‍🧑 Matching Partners for Your Subject")
        if subject == "Math":
            partners = pd.DataFrame({
                "Name": ["Alice", "Bob", "Ria", "Kunal"],
                "Gender": ["Female", "Male", "Female", "Male"],
                "Knowledge Level": ["Intermediate", "Advanced", "Beginner", "Advanced"],
                "Preferred Mode": ["Video", "Audio", "Notes", "Chat"],
                "Language": ["English", "Hindi", "English", "Hindi"]
            })
            st.dataframe(partners, use_container_width=True)

    # --- Teacher Assistant Page ---
    elif menu == "📘 Teacher Assistant":
        st.markdown("### 🧑‍🏫 Become a Teacher Assistant")
        with st.form("teacher_form"):
            tname = st.text_input("Your Name *")
            tsubject = st.text_input("Subject You Can Teach *")
            tfee = st.selectbox("Hourly Fee", ["Free", "₹100/hr", "₹250/hr", "₹500/hr"])
            thours = st.selectbox("Teaching Hours Available", ["1–2 hours", "2–3 hours", "3+ hours"])
            tuniversity = st.text_input("Your University")
            tstatus = st.selectbox("Are you currently working/studying?", ["Yes", "No"])
            tid_upload = st.file_uploader("Upload Teacher ID (if available)")
            tsubmit = st.form_submit_button("Register as Teacher")
            if tsubmit:
                if not tname:
                    st.error("Please provide your name.")
                else:
                    st.success(f"✅ {tname}, you've successfully registered as a teacher!")
                    st.markdown("#### Students Looking for Help in Your Subject:")
                    st.info("• Anjali (Math, Needs Detailed Prep)\n• Rahul (Math, Crash Course)\n• Fatima (Math, Exam Tomorrow)")

    # --- Subscription Page ---
    elif menu == "💎 Subscription Plans":
        st.markdown("### 💳 Choose a Subscription Plan")
        st.markdown("""
        | Plan | Price | Benefits |
        |------|-------|----------|
        | 🟢 **Basic** | Free | 1 Study Partner, Notes Access |
        | 🔵 **Premium** | ₹499/month | 3 Partners, Video Sessions, Teacher Access |
        | 🔴 **Elite** | ₹999/month | All Features + Job Placement + Unlimited Teachers |
        """, unsafe_allow_html=True)

        plan = st.radio("Choose your plan", ["Basic", "Premium", "Elite"])
        if plan == "Basic":
            st.success("✅ You’ve subscribed to the Basic Plan for Free!")
        else:
            st.warning(f"💰 {plan} Plan requires payment.")
            st.selectbox("Choose Payment Method", ["UPI", "Net Banking", "Credit Card", "Other"])

    # --- Feedback Page ---
    elif menu == "📬 Feedback":
        st.markdown("### ✍️ Share Your Feedback")
        st.text_area("💬 What did you like or want us to improve?")
        if st.button("📨 Submit Feedback"):
            st.success("Thank you for your feedback! 💙 Keep Studying Strong!")

