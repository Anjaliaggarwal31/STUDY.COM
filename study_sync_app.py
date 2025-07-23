import streamlit as st

# -------- Timezone options --------
timezones = [
    "IST (Indian Standard Time)", "GMT", "EST", "PST", "CST", 
    "JST", "AEST", "CET", "Other"
]

# -------- Session setup --------
for key in ["registered", "subscribed", "partner_matched", "page", "username"]:
    if key not in st.session_state:
        st.session_state[key] = False if key != "page" else "intro"

# -------- Welcome Page --------
def show_intro():
    st.markdown("<h1 style='text-align:center;'>📚 StudySync</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center;'>“Study together. Grow together. Succeed together.”</h4>", unsafe_allow_html=True)
    st.markdown("###")
    st.markdown("<div style='display:flex; justify-content:center;'>"
                "<button onclick='document.querySelector(\"button[kind=primary]\").click();' "
                "style='font-size:18px; padding:10px 30px; background-color:#4CAF50; color:white; "
                "border:none; border-radius:8px;'>🔐 Register Now</button></div>", unsafe_allow_html=True)
    if st.button("🔐"):
        st.session_state.page = "register"

# -------- Student Registration --------
def student_registration():
    st.title("🎓 Student Registration")

    name = st.text_input("Full Name")
    st.session_state.username = name
    email = st.text_input("Email")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    timezone = st.selectbox("Time Zone", timezones)
    if timezone == "Other":
        timezone = st.text_input("Specify Time Zone")

    languages = ["English", "Hindi", "French", "Spanish", "Other"]
    preferred_language = st.selectbox("Preferred Language", languages)
    if preferred_language == "Other":
        preferred_language = st.text_input("Specify Language")

    universities = ["IIT", "IIM", "DERI", "International University", "Other"]
    university = st.selectbox("University", universities)
    if university == "Other":
        university = st.text_input("Specify University")

    courses = ["UG", "PG", "PhD", "Professional (CA/CFA/CMA)", "Other"]
    course = st.selectbox("Course", courses)
    if course == "Other":
        course = st.text_input("Specify Course")

    study_goal = st.radio("Study Goal", ["Crash Course", "Detailed Preparation"])
    block_distractions = st.checkbox("🛡️ Block distractions when switching apps")
    id_upload = st.file_uploader("Upload Student ID", type=["png", "jpg", "pdf"])
    skip_id = st.checkbox("Skip ID Upload")

    if st.button("✅ Complete Registration"):
        if name and email and (id_upload or skip_id):
            st.session_state.registered = True
            st.session_state.page = "partner"
            st.success(f"🎉 {name}, you have registered successfully!")
        else:
            st.error("❌ Fill all required fields or check skip ID upload.")

# -------- Partner Matching --------
def partner_matching():
    st.title("🤝 Match a Study Partner")

    study_type = st.radio("Study Preference", ["1-on-1", "Group"])
    preferred_gender = st.selectbox("Preferred Partner Gender", ["Any", "Male", "Female", "Other"])
    knowledge_level = st.selectbox("Knowledge Level", ["Beginner", "Intermediate", "Advanced"])
    subject = st.text_input("Subject to Study")
    tz = st.selectbox("Partner's Time Zone", timezones)
    if tz == "Other":
        tz = st.text_input("Specify Partner Time Zone")

    lang = st.selectbox("Partner's Language", ["English", "Hindi", "French", "Spanish", "Other"])
    if lang == "Other":
        lang = st.text_input("Specify Language")

    if st.button("🔍 Match Partner"):
        st.success("🎯 Partner matched successfully!")
        st.session_state.partner_matched = True
        st.markdown("### 👥 Your Matched Partners")
        st.table([
            {"Name": "Aarav", "Subject": subject, "Level": knowledge_level, "Type": study_type, "Language": lang, "Time Zone": tz},
            {"Name": "Sarah", "Subject": subject, "Level": knowledge_level, "Type": study_type, "Language": lang, "Time Zone": tz}
        ])

# -------- Subscription Plans --------
def subscription_plans():
    st.title("💎 Subscription Plans")

    st.subheader("📘 Basic Plan - ₹0/month (Free)")
    st.markdown("- Access group study sessions\n- 1 partner/week")

    st.subheader("🥈 Premium Plan - ₹499/month")
    st.markdown("- Unlimited matching\n- Group + 1-on-1\n- Resources access")

    st.subheader("👑 Elite Plan - ₹999/month")
    st.markdown("- All Premium features\n- Job help\n- Direct teacher access")

    plan = st.radio("Choose Plan", ["Basic (Free)", "Premium", "Elite"])

    if plan == "Basic (Free)":
        if st.button("✅ Activate Free Plan"):
            st.success("🎉 You are now on the Basic (Free) Plan!")
            st.session_state.subscribed = True

    else:
        st.markdown("### 💰 Payment Required")
        method = st.selectbox("Payment Method", ["UPI", "Credit Card", "Net Banking"])
        if st.button("💳 Pay & Subscribe"):
            st.success(f"✅ Subscribed to {plan} plan using {method}!")

# -------- Teacher Registration --------
def teacher_registration():
    st.title("🧑‍🏫 Teacher Registration")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    university = st.selectbox("University", ["IIT", "IIM", "DERI", "Other"])
    if university == "Other":
        university = st.text_input("Specify University")

    subject = st.text_input("Subjects You Can Teach")
    duration = st.selectbox("Available Duration (hrs)", ["1", "2", "3", "4+"])
    currency = st.selectbox("Currency", ["INR", "USD", "EUR", "GBP"])
    fee = st.number_input(f"Fee per Hour ({currency})", min_value=0.0)
    working = st.radio("Currently Working?", ["Yes", "No"])
    t_id = st.file_uploader("Upload ID", type=["png", "jpg", "pdf"])

    if st.button("📨 Submit Profile"):
        if name and subject and fee and t_id:
            st.success(f"✅ Thank you {name}, your teaching profile is submitted!")
        else:
            st.error("❌ Please complete all fields and upload ID.")

# -------- Main App Routing --------
if st.session_state.page == "intro":
    show_intro()

elif st.session_state.page == "register":
    student_registration()

elif st.session_state.page == "partner" and st.session_state.registered:
    partner_matching()

# -------- Expandable Sections --------
if st.session_state.registered:
    with st.expander("📦 Subscription Plans"):
        subscription_plans()

    with st.expander("📚 Register as a Teacher"):
        teacher_registration()
