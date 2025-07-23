import streamlit as st
import pytz

st.set_page_config(page_title="StudySync", layout="centered")

# Session state initialization
for key in ["registered", "subscribed", "partner_matched"]:
    if key not in st.session_state:
        st.session_state[key] = False

# --- Welcome Screen ---
def show_intro():
    st.markdown("<h1 style='text-align:center;'>📚 StudySync</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center;'>“Study together. Grow together. Succeed together.”</h4>", unsafe_allow_html=True)
    st.markdown("---")
    if st.button("🔐 Register Now"):
        st.session_state.page = "register"

# --- Registration ---
def student_registration():
    st.title("🎓 Student Registration")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    location = st.text_input("Location")
    timezone = st.selectbox("Time Zone", pytz.all_timezones)
    preferred_language = st.selectbox("Preferred Language", ["English", "Hindi", "French", "Spanish", "Other"])

    universities = ["IIT", "IIM", "DERI", "International University", "Other"]
    university = st.selectbox("University", universities)
    if university == "Other":
        university = st.text_input("Please specify your University")

    courses = ["UG", "PG", "PhD", "Professional (CA/ACCA/CFA/CMA)", "Other"]
    course = st.selectbox("Course Level", courses)
    if course == "Other":
        course = st.text_input("Please specify your Course")

    study_goal = st.radio("Study Goal", ["Crash Course", "Detailed Preparation"])
    block_distractions = st.checkbox("🛡️ Block other apps during study (popup prompt will appear on switch attempt)")

    id_upload = st.file_uploader("Upload Student ID", type=["png", "jpg", "pdf"])

    if st.button("✅ Complete Registration"):
        if name and email and id_upload:
            st.success("🎉 Registered successfully!")
            st.session_state.registered = True
            st.session_state.page = "partner"
        else:
            st.error("❌ Please fill all required fields and upload your ID.")

# --- Partner Matching ---
def partner_matching():
    st.title("🤝 Find a Study Partner")

    study_type = st.radio("Preferred Study Type", ["1-on-1", "Group"])
    preferred_gender = st.selectbox("Preferred Partner Gender", ["Any", "Male", "Female", "Other"])
    partner_knowledge = st.selectbox("Preferred Knowledge Level", ["Beginner", "Intermediate", "Advanced"])
    partner_subject = st.text_input("Preferred Subject")
    partner_timezone = st.selectbox("Partner Time Zone", pytz.all_timezones)
    partner_language = st.selectbox("Partner Preferred Language", ["English", "Hindi", "French", "Spanish", "Other"])

    if st.button("🔍 Match Partner"):
        st.success("🎉 Partner matched successfully!")
        st.session_state.partner_matched = True
        st.write("👥 **Matched Partner Details:**")
        st.write(f"• Subject: {partner_subject}")
        st.write(f"• Knowledge Level: {partner_knowledge}")
        st.write(f"• Language: {partner_language}")
        st.write(f"• Time Zone: {partner_timezone}")

# --- Subscription Plans ---
def subscription_plans():
    st.title("💎 Subscription Plans (INR)")

    st.markdown("#### 📘 Basic Plan - ₹199/month")
    st.markdown("- Access to 1 partner/week")
    st.markdown("- Group study only")

    st.markdown("#### 🥈 Premium Plan - ₹499/month")
    st.markdown("- Unlimited partner matches")
    st.markdown("- 1-on-1 and group study access")

    st.markdown("#### 👑 Elite Plan - ₹999/month")
    st.markdown("- All Premium benefits")
    st.markdown("- Job placement support")
    st.markdown("- Access to top teachers (IIT/IIM/International)")
    st.markdown("- Exclusive webinars and notes")

    choice = st.radio("Select a Plan", ["Basic", "Premium", "Elite"])
    if choice == "Elite":
        st.selectbox("Choose Payment Method", ["UPI", "Credit Card", "Debit Card", "Net Banking"])

    if st.button("📥 Subscribe"):
        st.success(f"✅ Subscribed to {choice} plan successfully!")
        st.session_state.subscribed = True

# --- Teacher Registration ---
def teacher_registration():
    st.title("🧑‍🏫 Teacher Registration")

    t_name = st.text_input("Full Name (Teacher)")
    t_email = st.text_input("Email")
    t_university = st.selectbox("University", ["IIT", "IIM", "DERI", "International University", "Other"])
    if t_university == "Other":
        t_university = st.text_input("Please specify your University")

    t_subject = st.text_input("Subjects you teach")
    t_duration = st.selectbox("Preferred Teaching Duration (hrs)", ["1", "2", "3", "4"])
    t_currency = st.selectbox("Currency", ["INR", "USD", "EUR", "GBP"])
    t_fee = st.number_input(f"Teaching Fee per Hour ({t_currency})", min_value=0)
    currently_working = st.radio("Are you currently working?", ["Yes", "No"])
    t_id = st.file_uploader("Upload Teacher ID", type=["jpg", "png", "pdf"])

    if st.session_state.subscribed and st.button("📨 Submit Teacher Profile"):
        if t_name and t_email and t_subject and t_fee and t_id:
            st.success("✅ Teacher profile submitted successfully!")
        else:
            st.error("❌ Please fill all fields and upload your ID.")
    elif not st.session_state.subscribed:
        st.warning("⚠️ You need to subscribe to register as a teacher.")

# --- Page Navigation ---
if "page" not in st.session_state:
    st.session_state.page = "intro"

if st.session_state.page == "intro":
    show_intro()
elif st.session_state.page == "register":
    student_registration()
elif st.session_state.registered and st.session_state.page == "partner":
    partner_matching()

# Side Menu
with st.sidebar:
    st.header("📌 Navigation")
    if st.button("🔐 Register"):
        st.session_state.page = "register"
    if st.session_state.registered:
        if st.button("🤝 Find Partner"):
            st.session_state.page = "partner"
        if st.button("💎 Subscription Plans"):
            subscription_plans()
        if st.button("🧑‍🏫 Teacher Registration"):
            teacher_registration()
