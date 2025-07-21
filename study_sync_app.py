import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime

# Initialize session state
if 'points' not in st.session_state:
    st.session_state.points = 0
if 'subscribed' not in st.session_state:
    st.session_state.subscribed = False

# Page config
st.set_page_config(page_title="Study Sync", layout="wide")
st.markdown("""
    <style>
        body {
            background-color: #f4f6f8;
        }
        .main, .block-container {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 2rem;
        }
        .big-font {
            font-size: 24px !important;
            font-weight: bold;
            color: #0d47a1;
        }
        .st-bb {
            background-color: #e3f2fd;
        }
    </style>
""", unsafe_allow_html=True)

# Banner
st.markdown("<h1 style='text-align: center; color: #1565c0;'>📘 Study Sync</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Study smarter, not harder. Collaborate with your ideal study partner across the globe.</p>", unsafe_allow_html=True)

# Sidebar menu
with st.sidebar:
    choice = option_menu("Menu", ["Home", "Register", "Find Partner", "Subscriptions", "Feedback"],
                         icons=["house", "person", "people", "gem", "chat"], menu_icon="cast", default_index=0)

# Home Page
if choice == "Home":
    st.image("https://cdn.pixabay.com/photo/2016/11/29/05/08/adult-1868750_1280.jpg", use_container_width=True)
    st.subheader("📈 Progress Dashboard")
    st.success(f"Total Points: {st.session_state.points}")
    st.info("Study consistently every week for a year to unlock job placement support, teacher access & more.")

# Registration
elif choice == "Register":
    st.header("🎓 Student Registration")
    with st.form("registration_form"):
        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input("Full Name")
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            language = st.selectbox("Preferred Study Language", ["English", "Hindi", "Spanish", "French", "German", "Other"])
            knowledge = st.selectbox("Your Current Knowledge Level", ["Basic", "Intermediate", "Advanced"])
            goal = st.selectbox("Study Goal", ["Crash Revision", "Detailed Preparation", "Exam Tomorrow", "Concept Clarity"])
            study_duration = st.slider("Preferred Daily Study Duration (in hours)", 1, 10, 2)
        with col2:
            student_type = st.radio("Are you a...", ["University Student", "Professional Course Student"])
            if student_type == "University Student":
                university = st.selectbox("Select Your University", ["IIT Delhi", "DU", "NSUT", "IIITD", "Oxford", "Harvard", "MIT", "Other"])
                if university == "Other":
                    university = st.text_input("Enter University Name")
            else:
                university = st.selectbox("Professional Course", ["ICAI", "ACCA", "CMA", "CFA", "Other"])
                if university == "Other":
                    university = st.text_input("Enter Institute Name")
            timezone = st.selectbox("Select Your Time Zone", [
                "IST (Indian Standard Time)",
                "EST (Eastern Standard Time)",
                "PST (Pacific Time)",
                "CET (Central European Time)",
                "GMT (Greenwich Mean Time)",
                "AEST (Australian Eastern Standard Time)"
            ])
            id_upload = st.file_uploader("Upload Student ID / Proof (PDF, JPG, PNG)")

        register_submit = st.form_submit_button("Register")
        if register_submit:
            st.success("✅ Registered Successfully! Go to 'Find Partner' to match.")
            st.session_state.points += 10

# Match Study Partner
elif choice == "Find Partner":
    st.header("🔍 Find Your Ideal Study Partner")
    with st.form("match_form"):
        col1, col2 = st.columns(2)
        with col1:
            partner_gender = st.selectbox("Preferred Gender", ["Any", "Male", "Female"])
            partner_language = st.selectbox("Preferred Language", ["English", "Hindi", "Spanish", "French", "Other"])
            partner_level = st.selectbox("Partner Knowledge Level", ["Any", "Basic", "Intermediate", "Advanced"])
        with col2:
            partner_timezone = st.selectbox("Preferred Partner Time Zone", [
                "IST", "EST", "PST", "CET", "GMT", "AEST"
            ])
            study_mode = st.radio("Study Mode", ["Video", "Audio", "Chat", "Recording Exchange"])
            subject_focus = st.text_input("Subject Focus")

        match_submit = st.form_submit_button("Find Partner")
        if match_submit:
            st.success("🎉 Partner matched successfully! Connect and start learning.")
            st.session_state.points += 20

# Subscription and Teacher Access
elif choice == "Subscriptions":
    st.header("💼 Subscriptions & Teacher Access")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Free Plan")
        st.write("- Partner Matching")
        st.write("- Weekly Study Tips")
    with col2:
        st.subheader("Pro ₹499/month")
        st.write("- Everything in Free Plan")
        st.write("- Access to Teachers")
        st.write("- Personalized Support")
    with col3:
        st.subheader("Premium ₹4999/year")
        st.write("- All Pro Features")
        st.write("- Job Placement Assistance")
        st.write("- AI-Powered Study Plans")

    if st.button("📥 Subscribe Now"):
        st.session_state.subscribed = True
        st.success("✅ Subscription Activated!")
        st.session_state.points += 30

    if st.session_state.subscribed:
        st.markdown("### 📘 Become a Teacher (Available only after Subscription)")
        with st.form("teacher_form"):
            t_name = st.text_input("Your Name")
            t_institute = st.text_input("Institute/University")
            t_subject = st.text_input("Subject You Can Teach")
            t_fee = st.number_input("Tuition Fee (₹ per month)", min_value=0, step=100)
            t_available = st.checkbox("I'm available for this SPAC/Session")

            submit_teacher = st.form_submit_button("Register as Teacher")
            if submit_teacher:
                st.success("✅ You are now registered as a teacher!")
                st.session_state.points += 20

# Feedback
elif choice == "Feedback":
    st.header("🗣 Share Your Feedback")
    with st.form("feedback_form"):
        session_rating = st.slider("Rate Your Session", 1, 5, 4)
        feedback_text = st.text_area("Suggestions / Comments")
        feed_submit = st.form_submit_button("Submit Feedback")
        if feed_submit:
            st.success("🎯 Thank you for your valuable feedback!")
            st.session_state.points += 5

# Footer Message
st.markdown("---")
st.markdown("<p style='text-align: center; color: #455a64;'>Study consistently for a week to earn bonus points. A year of effort leads to teacher guidance & job placement. 🚀</p>", unsafe_allow_html=True)
