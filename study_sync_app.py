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
            background-color: #fce4ec;
            color: #880e4f;
        }
        .main, .block-container {
            background-color: #fff0f5;
            border-radius: 10px;
            padding: 2rem;
        }
        .big-font {
            font-size: 24px !important;
            font-weight: bold;
            color: #ad1457;
        }
    </style>
""", unsafe_allow_html=True)

# Banner
st.markdown("<h1 style='text-align: center; color: #e91e63;'>🎓 Welcome to Study Sync 🎓</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Collaborative study. Consistency. Success. 🚀</p>", unsafe_allow_html=True)

# Sidebar menu
with st.sidebar:
    choice = option_menu("Navigation", ["Home", "Register", "Find Study Partner", "Subscriptions", "Feedback"],
                         icons=['house', 'person', 'people', 'gem', 'chat'], menu_icon="cast", default_index=0)

# Home Page
if choice == "Home":
    st.image("https://cdn.pixabay.com/photo/2015/01/08/18/29/student-593333_1280.jpg", use_column_width=True)
    st.subheader("🏆 Your Study Points")
    st.success(f"You've earned {st.session_state.points} points.")
    st.markdown("**Tip:** Study consistently every week for 1 year to unlock job placement & teacher support.")

# Registration Page
elif choice == "Register":
    st.header("📝 Student Registration")
    with st.form("register_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name")
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            language = st.selectbox("Preferred Language", ["English", "Hindi", "Spanish", "French", "German", "Other"])
            level = st.selectbox("Knowledge Level", ["Basic", "Intermediate", "Advanced"])
            goal = st.selectbox("Study Goal", ["Crash Revision", "Detailed Preparation", "Exam Tomorrow", "Concept Clarity"])
        with col2:
            college_list = ["IIT Delhi", "DU", "NSUT", "IIIT-Delhi", "Oxford", "Harvard", "MIT", "Other"]
            selected_college = st.selectbox("University", college_list)
            if selected_college == "Other":
                college = st.text_input("Enter your University")
            else:
                college = selected_college
            timezone = st.selectbox("Time Zone", [
                "IST (Indian Standard Time)",
                "EST (Eastern Time - US)",
                "PST (Pacific Time - US)",
                "CET (Central European Time)",
                "AEST (Australian Eastern Time)",
                "GMT (Greenwich Mean Time)"
            ])
            duration = st.slider("Preferred Daily Study Duration (hrs)", 1, 12, 2)
            subject_focus = st.text_input("Subjects you want to focus on")
            id_upload = st.file_uploader("Upload College ID or Verification Document")
        submitted = st.form_submit_button("Register")
        if submitted:
            st.success("✅ Registered Successfully! Go to 'Find Study Partner' to continue.")
            st.session_state.points += 10

# Match Partner
elif choice == "Find Study Partner":
    st.header("🤝 Find Your Study Partner")
    with st.form("partner_form"):
        col1, col2 = st.columns(2)
        with col1:
            preferred_gender = st.selectbox("Preferred Partner Gender", ["Any", "Male", "Female"])
            partner_language = st.selectbox("Preferred Language for Partner", ["English", "Hindi", "Spanish", "Other"])
            match_level = st.selectbox("Partner Knowledge Level", ["Any", "Basic", "Intermediate", "Advanced"])
        with col2:
            study_subject = st.text_input("Study Subject")
            mode = st.radio("Study Mode", ["Audio", "Video", "Chat Only", "Recording Upload"])
            partner_timezone = st.selectbox("Partner Timezone", [
                "IST", "EST", "PST", "CET", "AEST", "GMT"
            ])
        match_btn = st.form_submit_button("🔍 Find Partner")
        if match_btn:
            st.success("🎉 Partner found based on preferences! Connect and start learning.")
            st.session_state.points += 20

# Subscription Plans + Teacher Registration
elif choice == "Subscriptions":
    st.header("💎 Subscription Plans")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Free")
        st.write("✔ Basic Partner Match")
        st.write("✔ Weekly Study Tips")
    with col2:
        st.subheader("Pro - ₹499/month")
        st.write("✔ All Free Features")
        st.write("✔ Access to Teachers")
        st.write("✔ Mock Tests & Guidance")
    with col3:
        st.subheader("Premium Yearly - ₹4999")
        st.write("✔ All Pro Features")
        st.write("✔ Job Placement Support")
        st.write("✔ Personalized Reports & AI Suggestions")
    
    if st.button("🚀 Subscribe"):
        st.session_state.subscribed = True
        st.success("🎉 Subscribed! Teacher access and placement unlocked.")
        st.session_state.points += 50

    if st.session_state.subscribed:
        st.markdown("### 🧑‍🏫 Teacher Registration (Available only with Subscription)")
        with st.form("teacher_form"):
            teacher_name = st.text_input("Your Name")
            teach_college = st.text_input("University/Institute")
            subject = st.text_input("Subject You Can Teach")
            fee = st.number_input("Expected Fee (₹/month)", min_value=0)
            is_available = st.checkbox("Available for this SPAC/Class/Subject")
            submit_teacher = st.form_submit_button("Register as Teacher")
            if submit_teacher:
                st.success("✅ You’re now listed as a teacher! Students can now find you.")

# Feedback
elif choice == "Feedback":
    st.header("🗣 Feedback After Study Session")
    with st.form("feedback_form"):
        session_rating = st.slider("Rate Your Study Session", 1, 5, 3)
        feedback = st.text_area("Comments or Suggestions")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("🙌 Thanks for your feedback! You've earned more points.")
            st.session_state.points += 5

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #6a1b9a;'>Keep going! You’re building a habit. Study one week straight to unlock mentorship. 💡</p>", unsafe_allow_html=True)
