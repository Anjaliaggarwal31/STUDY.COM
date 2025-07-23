import streamlit as st

# ---------- Timezones ----------
timezones = [
    "IST (Indian Standard Time)",
    "GMT (Greenwich Mean Time)",
    "EST (Eastern Standard Time)",
    "PST (Pacific Standard Time)",
    "CST (Central Standard Time)",
    "JST (Japan Standard Time)",
    "AEST (Australian Eastern Standard Time)",
    "CET (Central European Time)",
    "Other"
]

# -------- Session State --------
for key in ["registered", "subscribed", "partner_matched", "show_subscribe", "show_teacher"]:
    if key not in st.session_state:
        st.session_state[key] = False

# -------- Welcome Screen --------
def show_intro():
    st.markdown("<h1 style='text-align:center;'>📚 StudySync</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center;'>“Study together. Grow together. Succeed together.”</h4>", unsafe_allow_html=True)
    st.markdown("---")
    if st.button("🔐 Register Now"):
        st.session_state.page = "register"

# -------- Student Registration --------
def student_registration():
    st.title("🎓 Student Registration")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    timezone = st.selectbox("Time Zone", timezones)
    if timezone == "Other":
        timezone = st.text_input("Please specify your Time Zone")

    languages = ["English", "Hindi", "French", "Spanish", "Other"]
    preferred_language = st.selectbox("Preferred Language", languages)
    if preferred_language == "Other":
        preferred_language = st.text_input("Please specify your Language")

    universities = ["IIT", "IIM", "DERI", "International University", "Other"]
    university = st.selectbox("University", universities)
    if university == "Other":
        university = st.text_input("Please specify your University")

    courses = ["UG", "PG", "PhD", "Professional (CA/ACCA/CFA/CMA)", "Other"]
    course = st.selectbox("Course Level", courses)
    if course == "Other":
        course = st.text_input("Please specify your Course")

    study_goal = st.radio("Study Goal", ["Crash Course", "Detailed Preparation"])
    block_distractions = st.checkbox("🛡️ Block distractions with warning if switching apps")

    id_upload = st.file_uploader("Upload Student ID (Optional)", type=["png", "jpg", "pdf"])
    if not id_upload:
        skip_id = st.checkbox("Skip for now")

    if st.button("✅ Complete Registration"):
        if name and email and (id_upload or skip_id):
            st.success("🎉 Registered successfully!")
            st.session_state.registered = True
            st.session_state.page = "partner"
        else:
            st.error("❌ Please fill all fields or skip ID upload.")

# -------- Partner Matching --------
def partner_matching():
    st.title("🤝 Find a Study Partner")

    study_type = st.radio("Preferred Study Type", ["1-on-1", "Group"])
    preferred_gender = st.selectbox("Preferred Partner Gender", ["Any", "Male", "Female", "Other"])
    knowledge_level = st.selectbox("Preferred Knowledge Level", ["Beginner", "Intermediate", "Advanced"])
    subject = st.text_input("Preferred Subject")
    tz = st.selectbox("Partner Time Zone", timezones)
    if tz == "Other":
        tz =
