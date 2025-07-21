import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime

# Initialize session state
if 'points' not in st.session_state:
    st.session_state.points = 0
if 'subscribed' not in st.session_state:
    st.session_state.subscribed = False

# Page Config
st.set_page_config(page_title="Study Sync", layout="wide")
st.markdown("""
    <style>
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

# Header
st.markdown("<h1 style='text-align: center; color: #1565c0;'>📘 Study Sync</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Smarter learning through peer and teacher collaboration.</p>", unsafe_allow_html=True)

# Sidebar menu
with st.sidebar:
    choice = option_menu("Menu", ["Home", "Register", "Find Partner", "Subscriptions", "Feedback"],
                         icons=["house", "person", "people", "gem", "chat"], menu_icon="cast", default_index=0)

# Home Page
if choice == "Home":
    st.image("https://cdn.pixabay.com/photo/2016/11/29/05/08/adult-1868750_1280.jpg", use_container_width=True)
    st.subheader("📈 Progress Dashboard")
    st.success(f"Total Points: {st.session_state.points}")
    st.info("📢 Earn more points by participating. A year of activity unlocks full platform features!")

# Registration Page
elif choice == "Register":
    st.header("🎓 Student Registration")
    with st.form("registration_form"):
        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input("Full Name")
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            language = st.selectbox("Preferred Study Language", ["English", "Hindi", "Spanish", "French", "Other"])
            knowledge = st.selectbox("Your Knowledge Level", ["Basic", "Intermediate", "Advanced"])
            goal = st.selectbox("Study Goal", ["Crash Revision", "Detailed Prep", "Exam Tomorrow", "Concept Clarity"])
            duration = st.slider("Daily Study Duration (hrs)", 1, 10, 2)
        with col2:
            category = st.radio("Your Category", ["University Student", "Professional Course"])
            if category == "University Student":
                university = st.selectbox("Select University", ["IIT Delhi", "DU", "NSUT", "IIITD", "Oxford", "Harvard", "MIT", "Other"])
                if university == "Other":
                    university = st.text_input("Enter University Name")
            else:
                university = st.selectbox("Select Institute", ["ICAI", "ACCA", "CMA", "CFA", "Other"])
                if university == "Other":
                    university = st.text_input("Enter Institute Name")
            timezone = st.selectbox("Your Time Zone", [
                "IST (Indian Standard Time)",
                "EST (Eastern Standard Time)",
                "PST (Pacific Time)",
                "CET (Central European Time)",
                "GMT (Greenwich Mean Time)",
                "AEST (Australian Eastern Standard Time)"
            ])
            id_upload = st.file_uploader("Upload Student ID / Proof (PDF, JPG, PNG)")

        reg_submit = st.form_submit_button("Register")
        if reg_submit:
            st.success("✅ Registration Complete! Go to 'Find Partner' to proceed.")
            st.session_state.points += 10

# Find Partner Page
elif choice == "Find Partner":
    st.header("🤝 Match With a Study Partner")
    with st.form("match_form"):
        col1, col2 = st.columns(2)
        with col1:
            pref_gender = st.selectbox("Preferred Partner Gender", ["Any", "Male", "Female"])
            pref_language = st.selectbox("Partner Language", ["English", "Hindi", "Spanish", "French", "Other"])
            pref_level = st.selectbox("Knowledge Level", ["Any", "Basic", "Intermediate", "Advanced"])
            study_mode = st.radio("Preferred Mode", ["One-to-One", "Group Study"])
        with col2:
            partner_timezone = st.selectbox("Partner Time Zone", [
                "IST", "EST", "PST", "CET", "GMT", "AEST"
            ])
            interaction_mode = st.radio("Interaction Type", ["Video", "Audio", "Chat", "Recording Exchange"])
            focus_area = st.text_input("Subject Focus")

        match_submit = st.form_submit_button("Find Partner")
        if match_submit:
            st.success("🎯 Partner(s) matched successfully!")
            st.session_state.points += 20

# Subscriptions and Teacher Options
elif choice == "Subscriptions":
    st.header("💼 Subscription Plans")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Free")
        st.write("✔ Partner Matching\n✔ Study Tips\n❌ Teacher Access")
    with col2:
        st.subheader("Pro ₹499/month")
        st.write("✔ All Free Features\n✔ Teacher Access\n✔ AI Study Plans")
    with col3:
        st.subheader("Premium ₹4999/year")
        st.write("✔ All Pro Features\n✔ Job Placement\n✔ Priority Support")

    if st.button("Subscribe Now"):
        st.session_state.subscribed = True
        st.success("✅ Subscription Activated!")
        st.session_state.points += 30

    # Teacher Feature (only for subscribers)
    if st.session_state.subscribed:
        st.markdown("### 👩‍🏫 Teacher Registration (for Subscribers Only)")
        with st.form("teacher_form"):
            t_name = st.text_input("Your Name")
            t_university = st.text_input("Your University/Institute")
            t_subjects = st.text_area("Subjects You Can Teach")
            t_experience = st.text_input("Brief Teaching Experience or Area of Study")
            is_free = st.radio("Teaching Type", ["Free", "Paid"])
            fee = 0
            if is_free == "Paid":
                fee = st.number_input("Monthly Fee (in ₹)", min_value=0, step=100)
            available = st.checkbox("I am currently available to take students")

            t_submit = st.form_submit_button("Register as Teacher")
            if t_submit:
                st.success("🎓 Registered as Teacher Successfully!")
                st.session_state.points += 25

# Feedback Page
elif choice == "Feedback":
    st.header("📢 Feedback")
    with st.form("feedback_form"):
        rating = st.slider("Rate Study Sync", 1, 5, 4)
        feedback = st.text_area("Your Suggestions / Experience")
        fb_submit = st.form_submit_button("Submit Feedback")
        if fb_submit:
            st.success("🙌 Thanks for your feedback!")
            st.session_state.points += 5

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #607d8b;'>📚 A year of learning = teacher access + job support + growth. Study with purpose!</p>", unsafe_allow_html=True)
