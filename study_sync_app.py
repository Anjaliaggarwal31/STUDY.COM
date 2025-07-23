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
    partner_timezone = st.selectbox("Partner Time Zone", timezones)
    if partner_timezone == "Other":
        partner_timezone = st.text_input("Please specify your Partner's Time Zone")
    partner_language = st.selectbox("Partner Preferred Language", ["English", "Hindi", "French", "Spanish", "Other"])
    if partner_language == "Other":
        partner_language = st.text_input("Please specify Partner Language")

    if st.button("🔍 Match Partner"):
        st.success("🎉 Partner matched successfully!")
        st.session_state.partner_matched = True

        st.markdown("### 👥 Matched Partner List")
        st.table([
            {"Name": "Aarav", "Subject": subject, "Level": knowledge_level, "Type": study_type, "Language": partner_language, "Time Zone": partner_timezone},
            {"Name": "Sarah", "Subject": subject, "Level": knowledge_level, "Type": study_type, "Language": partner_language, "Time Zone": partner_timezone},
            {"Name": "Takeshi", "Subject": subject, "Level": knowledge_level, "Type": study_type, "Language": partner_language, "Time Zone": partner_timezone},
        ])

# -------- Subscription Plans --------
def subscription_plans():
    st.title("💎 Subscription Plans (INR)")

    st.markdown("#### 📘 Basic Plan - ₹199/month")
    st.markdown("- Group study only\n- 1 partner/week")

    st.markdown("#### 🥈 Premium Plan - ₹499/month")
    st.markdown("- Unlimited partner matching\n- Group + 1-on-1")

    st.markdown("#### 👑 Elite Plan - ₹999/month")
    st.markdown("- All Premium features\n- Job Placement Help\n- Teacher Access\n- Webinars & Notes")

    plan = st.radio("Choose Your Plan", ["Basic", "Premium", "Elite"])
    if plan == "Elite":
        st.selectbox("Select Payment Method", ["UPI", "Credit Card", "Net Banking"])

    if st.button("📥 Subscribe"):
        st.session_state.subscribed = True
        st.success(f"✅ Subscribed to {plan} plan!")

# -------- Teacher Registration --------
def teacher_registration():
    st.title("🧑‍🏫 Teacher Registration")

    t_name = st.text_input("Full Name")
    t_email = st.text_input("Email")
    t_university = st.selectbox("University", ["IIT", "IIM", "DERI", "International University", "Other"])
    if t_university == "Other":
        t_university = st.text_input("Please specify your University")

    t_subject = st.text_input("Subjects You Teach")
    t_duration = st.selectbox("Available Teaching Duration (hours)", ["1", "2", "3", "4+"])
    t_currency = st.selectbox("Preferred Currency", ["INR", "USD", "EUR", "GBP"])
    t_fee = st.number_input(f"Fee per Hour ({t_currency})", min_value=0.0)
    t_working = st.radio("Currently Working?", ["Yes", "No"])
    t_id = st.file_uploader("Upload ID Proof", type=["png", "jpg", "pdf"])

    if st.button("📨 Submit Teacher Registration"):
        if t_name and t_email and t_subject and t_fee and t_id:
            st.success("✅ Teacher profile submitted!")
        else:
            st.error("❌ Please fill all fields and upload your ID.")

# -------- Main UI Logic --------
if "page" not in st.session_state:
    st.session_state.page = "intro"

if st.session_state.page == "intro":
    show_intro()

elif st.session_state.page == "register":
    student_registration()

elif st.session_state.page == "partner" and st.session_state.registered:
    partner_matching()

# -------- Expandable Sections (Main Interface) --------
if st.session_state.registered:
    with st.expander("📦 View & Subscribe to Plans"):
        subscription_plans()

    with st.expander("📚 Teacher Registration"):
        teacher_registration()
