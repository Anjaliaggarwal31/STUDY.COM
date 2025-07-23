import streamlit as st
import pandas as pd

st.set_page_config(page_title="Study Sync", layout="wide")

# Session init
if 'points' not in st.session_state:
    st.session_state.points = 0
if 'partners' not in st.session_state:
    st.session_state.partners = []

# Style and Banner
st.markdown("""
    <style>
    .reportview-container {
        background: #f5f7fa;
        color: #333;
    }
    .main {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 2rem;
    }
    .stButton>button {
        background-color: #2e7d32;
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.image("https://cdn.pixabay.com/photo/2016/03/26/13/09/student-1284258_1280.jpg", use_container_width=True)
st.title("🎓 Study Sync – Collaborate. Learn. Grow.")

menu = st.sidebar.radio("Go to", ["🏠 Home", "📝 Register", "🤝 Find Partner", "🎓 Teacher Corner", "💎 Subscriptions", "📋 Feedback"])

# Home
if menu == "🏠 Home":
    st.subheader("Welcome Back to Study Sync!")
    st.success(f"⭐ You have {st.session_state.points} points.")
    st.info("🧠 Tip: Complete consistent weekly study to unlock job placement support.")
    st.checkbox("Block Background Distractions")

# Register
elif menu == "📝 Register":
    st.header("📌 Student Registration Form")
    with st.form("register"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name")
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            edu_type = st.selectbox("Education Type", ["UG", "PG", "Professional Course"])
            if edu_type == "Professional Course":
                profession = st.selectbox("Select Course", ["CA", "CMA", "ACCA", "CFA", "Other"])
            college = st.text_input("Institute / University Name")
            degree = st.text_input("Degree / Course")
            timezone = st.selectbox("Timezone", [
                "IST (Indian Standard Time)", "EST", "PST", "CET", "GMT", "AEST", "JST", "Others"
            ])
        with col2:
            language = st.selectbox("Preferred Language", ["English", "Hindi", "French", "Spanish", "German", "Other"])
            study_goal = st.selectbox("Study Goal", ["Crash Revision", "Detailed Preparation", "Concept Clarity", "Exam Tomorrow"])
            mode = st.radio("Study Preference", ["1:1 Partner", "Group Study"])
            duration = st.slider("Preferred Study Duration (in hours)", 1, 12, 2)
            id_doc = st.file_uploader("Upload College ID / Proof", type=["png", "jpg", "pdf"])
        submitted = st.form_submit_button("Register")
        if submitted:
            st.success("🎉 Registered Successfully! You're ready to study.")
            st.session_state.points += 10

# Find Study Partner
elif menu == "🤝 Find Partner":
    st.header("🔍 Match with Study Partners")
    with st.form("partner_form"):
        col1, col2 = st.columns(2)
        with col1:
            topic = st.text_input("Study Subject")
            level = st.selectbox("Your Knowledge Level", ["Basic", "Intermediate", "Advanced"])
            preferred_gender = st.selectbox("Preferred Partner Gender", ["Any", "Male", "Female"])
        with col2:
            time_zone = st.selectbox("Preferred Partner Timezone", [
                "IST (Indian Standard Time)", "EST", "PST", "CET", "GMT", "AEST", "JST", "Others"
            ])
            study_mode = st.radio("Mode of Study", ["Audio", "Video", "Chat", "Recording Upload"])
            match_type = st.radio("Do you want 1:1 or Group?", ["1:1", "Group"])
        find = st.form_submit_button("🔍 Search")
        if find:
            partner = {
                "Subject": topic,
                "Level": level,
                "Gender": preferred_gender,
                "Mode": study_mode,
                "Timezone": time_zone
            }
            st.session_state.partners.append(partner)
            st.success("✅ Partner(s) found! Connect securely to start learning.")
            st.balloons()
            st.session_state.points += 20
            st.write("📜 Partner List:")
            st.dataframe(pd.DataFrame(st.session_state.partners))

# Teacher Corner
elif menu == "🎓 Teacher Corner":
    st.header("👩‍🏫 Teacher Registration & Offering")
    with st.form("teacher_form"):
        col1, col2 = st.columns(2)
        with col1:
            teacher_name = st.text_input("Your Name")
            teacher_univ = st.text_input("University / Institution")
            subject = st.text_input("Subjects You Want to Teach")
        with col2:
            available = st.selectbox("Are You Currently Available?", ["Yes", "No"])
            experience = st.slider("Years of Teaching Experience", 0, 20, 2)
            fee = st.number_input("Monthly Fee Expected (INR)", min_value=0)
        submitted = st.form_submit_button("Register as Teacher")
        if submitted:
            if fee > 0:
                st.success(f"🎉 Registered as Teacher! Students can now view you as a premium mentor. Expected Fee: ₹{fee}/month")
                st.session_state.points += 30
            else:
                st.warning("💡 Please set a valid teaching fee.")

# Subscriptions
elif menu == "💎 Subscriptions":
    st.header("📦 Subscription Plans")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("🆓 Free Plan")
        st.write("- Basic Partner Matching")
        st.write("- Weekly Tips & Motivation")
    with col2:
        st.subheader("✨ Pro Plan ₹499/month")
        st.write("- Access to Registered Teachers")
        st.write("- Audio/Video Collaboration")
        st.write("- Personalized Feedback")
    with col3:
        st.subheader("🏅 Premium Yearly ₹4999")
        st.write("- All Pro Features")
        st.write("- Job Placement Assistance")
        st.write("- Monthly Review Reports")
    if st.button("🔓 Subscribe Now"):
        st.success("🎊 Subscribed Successfully! Unlocking Pro Features.")
        st.session_state.points += 50
    else:
        st.warning("❌ Subscription Failed. Please check payment.")

# Feedback
elif menu == "📋 Feedback":
    st.header("📣 Share Feedback on Sessions")
    with st.form("feedback_form"):
        rating = st.slider("Rate Your Session", 1, 5, 3)
        comment = st.text_area("Any Comments or Suggestions?")
        submit = st.form_submit_button("Submit")
        if submit:
            st.success("🙏 Thank you for your valuable feedback.")
            st.session_state.points += 5

# Footer
st.markdown("---")
st.markdown("<center>📘 Powered by Study Sync | Consistency Unlocks Your Future 🚀</center>", unsafe_allow_html=True)
