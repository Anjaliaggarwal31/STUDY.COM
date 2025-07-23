import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="StudySync", layout="wide")

# Session initialization
if "page" not in st.session_state:
    st.session_state.page = "home"
if "students" not in st.session_state:
    st.session_state.students = []
if "teachers" not in st.session_state:
    st.session_state.teachers = []
if "partners" not in st.session_state:
    st.session_state.partners = []

# 🎯 Motivational Messages
motivational_quotes = [
    "📚 Study Together, 🌱 Grow Together, 🚀 Succeed Together!",
    "💡 One step at a time is progress.",
    "🔥 Stay focused and never give up!",
]

# ⏩ Navigation control
def change_page(page_name):
    st.session_state.page = page_name

# 🎬 Welcome Screen
def home_screen():
    st.markdown(
        "<h1 style='text-align: center; color: #4CAF50;'>📘 StudySync</h1>",
        unsafe_allow_html=True)
    st.markdown(
        f"<h4 style='text-align: center;'>{motivational_quotes[0]}</h4>",
        unsafe_allow_html=True)
    st.markdown("### ")
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button("🚀 Register Now", use_container_width=True):
        change_page("register")
    st.markdown("</div>", unsafe_allow_html=True)

# 📥 Registration Form
def register_screen():
    st.title("👩‍🎓 Student Registration")
    with st.form("register_form"):
        name = st.text_input("👤 Name*", placeholder="Enter your full name")
        email = st.text_input("📧 Email")
        gender = st.selectbox("⚧️ Gender", ["Male", "Female", "Other"])
        if gender == "Other":
            specify_gender = st.text_input("Please Specify Gender")
        timezone = st.selectbox("🌐 Time Zone", ["IST", "EST", "PST", "Other"])
        if timezone == "Other":
            specify_timezone = st.text_input("Please Specify Time Zone")

        university = st.selectbox("🎓 University", ["IIT", "IIM", "DERI", "Other"])
        if university == "Other":
            specify_univ = st.text_input("Please Specify University")

        course = st.selectbox("📘 Course Type", ["UG", "PG", "PhD", "Professional", "Other"])
        if course == "Other":
            specify_course = st.text_input("Please Specify Course")

        subject = st.selectbox("📖 Subject", ["Math", "Physics", "Chemistry", "CS", "Other"])
        if subject == "Other":
            specify_subject = st.text_input("Please Specify Subject")

        goal = st.selectbox("🎯 Study Goal", ["Crash Course", "Detailed Prep", "Exam Tomorrow", "Competitive Exam", "Professional Exam", "Other"])
        if goal == "Other":
            specify_goal = st.text_input("Please Specify Study Goal")

        study_mode = st.multiselect("💻 Preferred Study Mode", ["Video", "Audio", "Notes", "Chat"])

        study_type = st.selectbox("🤝 Looking for", ["One-to-One Partner", "Group Study"])
        id_upload = st.file_uploader("🪪 Upload Student ID", type=["jpg", "png", "pdf"])

        submitted = st.form_submit_button("✅ Register")
        if submitted:
            if name.strip() == "":
                st.error("❌ Name is a required field!")
                st.markdown("<style>input:focus {border-color: red;}</style>", unsafe_allow_html=True)
            else:
                st.success(f"🎉 {name}, you have registered successfully!")
                st.session_state.students.append({
                    "Name": name,
                    "Subject": subject,
                    "Mode": study_mode,
                    "Study Type": study_type
                })
                time.sleep(2)
                change_page("partner")

# 🤝 Partner Matching Page
def partner_screen():
    st.title("🤝 Looking for a Partner to Study With")
    subject_interest = st.selectbox("📚 What subject do you want to study?", ["Math", "Physics", "CS", "Other"])
    if subject_interest == "Other":
        st.text_input("Please Specify Subject")

    filtered = [s for s in st.session_state.students if s["Subject"] == subject_interest]
    if filtered:
        st.markdown("### 📋 Available Study Partners:")
        df = pd.DataFrame(filtered)
        df["Partner Name"] = ["Alice", "Bob", "Charlie", "Dev", "Eva"][:len(df)]
        st.dataframe(df[["Partner Name", "Subject", "Study Type", "Mode"]])
    else:
        st.info("🔍 No matching partners found right now.")

# 👨‍🏫 Teacher Assistant Page
def teacher_screen():
    st.title("📚 Teacher Assistant Registration")
    with st.form("teacher_form"):
        name = st.text_input("👩‍🏫 Full Name")
        university = st.selectbox("🏫 University", ["IIT", "IIM", "DERI", "Other"])
        if university == "Other":
            st.text_input("Please Specify University")

        subject = st.selectbox("📘 Subject Expertise", ["Math", "Physics", "CS", "Other"])
        if subject == "Other":
            st.text_input("Please Specify Subject")

        duration = st.selectbox("⏱️ Teaching Duration", ["1 hour", "2-3 hours", "3+ hours"])
        fee = st.selectbox("💰 Hourly Fee", ["Free", "₹100", "₹200", "$5", "$10"])
        current_status = st.radio("🎓 Are you currently working?", ["Yes", "No"])
        id_upload = st.file_uploader("🪪 Upload ID", type=["jpg", "png", "pdf"])
        submitted = st.form_submit_button("📩 Submit")

        if submitted and name:
            st.success(f"🙌 {name}, you're registered as a teacher!")
            st.balloons()
            st.session_state.teachers.append({"Name": name, "Subject": subject})
            st.markdown("### 👨‍🎓 Students Looking for Teachers")
            student_df = pd.DataFrame(st.session_state.students)
            st.dataframe(student_df[["Name", "Subject", "Study Type"]])

# 💳 Subscription Plans
def subscription_screen():
    st.title("🎫 Subscription Plans")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("🆓 Basic (Free)")
        st.markdown("- Access to study partners\n- Use of study tools\n- Community access")
        st.success("Included for all users!")
    with col2:
        st.header("💎 Premium")
        st.markdown("- All Basic features\n- Access to Teacher Assistants\n- Study Resources")
        if st.button("Upgrade to Premium"):
            st.info("💳 Choose payment method: UPI / Net Banking / Card")

    with col3:
        st.header("👑 Elite")
        st.markdown("- All Premium features\n- Job Placement Support\n- Mock Interviews\n- Priority Support")
        if st.button("Upgrade to Elite"):
            st.warning("💳 Payment required: ₹999 or $15")

# ✍️ Feedback Section
def feedback_screen():
    st.title("🗣️ Give Your Feedback")
    feedback = st.text_area("✍️ Share your experience or suggestions...")
    if st.button("📬 Submit Feedback"):
        st.success("Thanks for your feedback! 💖")

# 🚀 Sidebar Navigation
if st.session_state.page != "home":
    menu = st.sidebar.radio("📂 Menu", ["Partners", "Teacher Assistant", "Subscription", "Feedback"])
    if menu == "Partners":
        partner_screen()
    elif menu == "Teacher Assistant":
        teacher_screen()
    elif menu == "Subscription":
        subscription_screen()
    elif menu == "Feedback":
        feedback_screen()
elif st.session_state.page == "home":
    home_screen()
elif st.session_state.page == "register":
    register_screen()
