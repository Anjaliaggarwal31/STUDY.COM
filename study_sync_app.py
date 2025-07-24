import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="StudySync App", layout="wide")

# Initialize session state
def init_session():
    if "registered" not in st.session_state:
        st.session_state.registered = False
    if "matched" not in st.session_state:
        st.session_state.matched = False
    if "partners" not in st.session_state:
        st.session_state.partners = []
    if "menu" not in st.session_state:
        st.session_state.menu = "🏠 Home"
    if "partner_filters" not in st.session_state:
        st.session_state.partner_filters = {}
    if "selected_plan" not in st.session_state:
        st.session_state.selected_plan = None
    if "user_details" not in st.session_state:
        st.session_state.user_details = {}
    if "feedbacks" not in st.session_state:
        st.session_state.feedbacks = []

init_session()

# Header and Navigation
st.markdown("<h1 style='text-align: center;'>🚀 StudySync</h1>", unsafe_allow_html=True)

menu = st.sidebar.radio("📌 Navigation",
    ["🏠 Home", "📝 Register", "🤝 Find a Partner", "💼 Subscription Plans", "🎯 Matched Partners", "💬 Feedback"],
    index=["🏠 Home", "📝 Register", "🤝 Find a Partner", "💼 Subscription Plans", "🎯 Matched Partners", "💬 Feedback"].index(st.session_state.menu))
st.session_state.menu = menu

# Quotes
quotes = {
    "🏠 Home": "“Learning becomes joyful when shared with a friend.”",
    "📝 Register": "“Your journey to better learning begins with a simple registration.”",
    "🤝 Find a Partner": "“A study partner turns the impossible into achievable.”",
    "💼 Subscription Plans": "“Invest in learning — it pays the best interest.”",
    "🎯 Matched Partners": "“Two minds studying together go further than one.”",
    "💬 Feedback": "“Your voice helps us shape a smarter StudySync.”"
}
st.markdown(f"<h5 style='text-align: center; color: gray;'>{quotes[menu]}</h5>", unsafe_allow_html=True)

# Home Page
if menu == "🏠 Home":
    st.success("Welcome to StudySync — your personalized study buddy matcher! 🎓")
    st.info("Use the sidebar to register, find a study partner, or explore subscriptions.")

# Helper Function
def check_required(val, label):
    if not val.strip():
        st.error(f"Please specify your {label}.")
        return False
    return True

# Dummy Data Generator
def generate_dummy_partners():
    names = ["Disha", "Kartik", "Harsh", "Mehak", "Aarav", "Anaya", "Ishaan", "Riya", "Kabir", "Tanvi", "Yash", "Sneha", "Ved", "Simran"]
    genders = ["Male", "Female"]
    knowledge_levels = ["Beginner", "Intermediate", "Advanced"]
    subjects = ["Maths", "Science", "English", "CS", "Economics", "Accounts"]
    languages = ["English", "Hindi"]
    timezones = ["IST", "UTC", "EST", "PST"]
    data = []
    for _ in range(50):
        data.append({
            "Name": random.choice(names),
            "Gender": random.choice(genders),
            "Knowledge": random.choice(knowledge_levels),
            "Subject": random.choice(subjects),
            "Language": random.choice(languages),
            "TimeZone": random.choice(timezones)
        })
    return pd.DataFrame(data)

# 📝 Registration Section
if menu == "📝 Register":
    reg_type = st.radio("Register as", ["Student", "Teacher"])

    if reg_type == "Student":
        with st.form("student_form"):
            name = st.text_input("Full Name *")
            email = st.text_input("Email *")

            gender = st.selectbox("Gender *", ["Male", "Female", "Others"])
            gender_other = st.text_input("Specify your gender *") if gender == "Others" else ""

            university = st.selectbox("University *", ["IIT", "IIM", "NIT", "DERI", "International", "Others"])
            university_other = st.text_input("Specify your university *") if university == "Others" else ""

            course = st.selectbox("Course *", ["UG", "PG", "Professional", "PhD", "Others"])
            course_other = st.text_input("Specify your course *") if course == "Others" else ""

            timezone = st.selectbox("Time Zone *", ["IST", "UTC", "EST", "PST", "Others"])
            timezone_other = st.text_input("Specify your time zone *") if timezone == "Others" else ""

            study_goal = st.multiselect("Your Study Goal *", ["Crash Course", "Detailed Preparation", "Exam Tomorrow", "Professional Exam", "Competitive Exam", "Others"])
            custom_goal = st.text_input("Specify your goal *") if "Others" in study_goal else ""

            language = st.selectbox("Preferred Language *", ["English", "Hindi", "Other"])
            language_other = st.text_input("Specify your language *") if language == "Other" else ""

            mode = st.multiselect("Preferred Study Mode", ["Video 🎥", "Audio 🎧", "Notes 📄", "Chat 💬"])
            uploaded_id = st.file_uploader("Upload Your ID (Optional)")

            submitted = st.form_submit_button("Submit")

            if submitted:
                required = all([
                    check_required(name, "name"),
                    check_required(email, "email"),
                    (gender != "Others" or check_required(gender_other, "gender")),
                    (university != "Others" or check_required(university_other, "university")),
                    (course != "Others" or check_required(course_other, "course")),
                    (timezone != "Others" or check_required(timezone_other, "time zone")),
                    (language != "Other" or check_required(language_other, "language")),
                    ("Others" not in study_goal or check_required(custom_goal, "goal"))
                ])
                if required:
                    st.session_state.user_details = {
                        "Name": name,
                        "Email": email,
                        "Gender": gender_other if gender == "Others" else gender,
                        "University": university_other if university == "Others" else university,
                        "Course": course_other if course == "Others" else course,
                        "Timezone": timezone_other if timezone == "Others" else timezone,
                        "Goal": study_goal + ([custom_goal] if custom_goal else []),
                        "Language": language_other if language == "Other" else language,
                        "Mode": mode,
                        "ID_uploaded": uploaded_id.name if uploaded_id else "Not Provided"
                    }
                    st.session_state.registered = True
                    st.success(f"🎉 Thank you for registering, {name}!")
                    st.balloons()
                    st.session_state.menu = "🤝 Find a Partner"
                    st.rerun()

    elif reg_type == "Teacher":
        with st.form("teacher_form"):
            tname = st.text_input("Full Name *")
            subject = st.text_input("Subject Expertise *")
            fee = st.selectbox("Hourly Teaching Fee", ["₹200", "₹500", "₹1000", "$10", "$20"])
            duration = st.selectbox("Available Duration", ["1 hour", "2–3 hours", "Flexible"])
            university = st.selectbox("University *", ["IIT", "IIM", "Other"])
            university_other = st.text_input("Specify university *") if university == "Other" else ""
            status = st.radio("Current Status", ["Student", "Faculty", "Other"])
            status_other = st.text_input("Specify status *") if status == "Other" else ""
            t_id = st.file_uploader("Upload your ID (Optional)")
            t_submit = st.form_submit_button("Register as Teacher")

            if t_submit:
                if not tname or not subject:
                    st.error("Please fill all required fields.")
                elif university == "Other" and not check_required(university_other, "university"):
                    pass
                elif status == "Other" and not check_required(status_other, "status"):
                    pass
                else:
                    st.success(f"✅ Thank you {tname} for registering as a teacher!")

# 🤝 Partner Matching
if menu == "🤝 Find a Partner":
    if not st.session_state.registered:
        st.warning("Please register first to find a partner.")
    else:
        with st.form("partner_form"):
            gender = st.selectbox("Preferred Partner Gender", ["Any", "Male", "Female", "Others"])
            gender_other = st.text_input("Specify partner gender *") if gender == "Others" else ""
            final_gender = gender_other if gender == "Others" else gender

            knowledge = st.selectbox("Partner's Knowledge Level", ["Beginner", "Intermediate", "Advanced"])

            subject = st.selectbox("Subject to Study *", ["Maths", "Science", "English", "CS", "Economics", "Accounts", "Others"])
            subject_other = st.text_input("Specify subject *") if subject == "Others" else ""
            final_subject = subject_other if subject == "Others" else subject

            language = st.selectbox("Partner's Language", ["English", "Hindi", "Other"])
            language_other = st.text_input("Specify partner language *") if language == "Other" else ""
            final_language = language_other if language == "Other" else language

            timezone = st.selectbox("Partner's Time Zone", ["IST", "UTC", "EST", "PST", "Others"])
            timezone_other = st.text_input("Specify partner time zone *") if timezone == "Others" else ""
            final_timezone = timezone_other if timezone == "Others" else timezone

            search = st.form_submit_button("Find Matches")

            if search:
                if gender == "Others" and not check_required(gender_other, "gender"):
                    pass
                elif subject == "Others" and not check_required(subject_other, "subject"):
                    pass
                elif language == "Other" and not check_required(language_other, "language"):
                    pass
                elif timezone == "Others" and not check_required(timezone_other, "time zone"):
                    pass
                else:
                    df = generate_dummy_partners()
                    exact = df[
                        ((df["Gender"] == final_gender) | (final_gender == "Any")) &
                        (df["Knowledge"] == knowledge) &
                        (df["Subject"].str.lower() == final_subject.lower()) &
                        (df["Language"] == final_language) &
                        (df["TimeZone"] == final_timezone)
                    ]
                    similar = df[
                        ((df["Gender"] == final_gender) | (final_gender == "Any")) &
                        (df["Knowledge"] == knowledge)
                    ]
                    matches = exact if not exact.empty else similar
                    st.session_state.partners = matches.to_dict("records")
                    st.session_state.partner_filters = {
                        "Gender": final_gender,
                        "Knowledge": knowledge,
                        "Subject": final_subject,
                        "Language": final_language,
                        "TimeZone": final_timezone
                    }
                    st.session_state.matched = True
                    if not matches.empty:
                        st.subheader("🎯 Your Matched Study Partners")
                        st.table(matches)
                    else:
                        st.error("No matches found. Try adjusting preferences.")

# 🎯 Matched Partners
if menu == "🎯 Matched Partners":
    if st.session_state.partners:
        st.subheader("🎯 Your Matched Study Partners")
        df = pd.DataFrame(st.session_state.partners)
        st.table(df)
    else:
        st.info("No partners matched yet. Please search under 'Find a Partner'.")

# 💼 Subscription Plans
if menu == "💼 Subscription Plans":
    st.subheader("💼 Subscription Tiers")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🟢 Basic — ₹0\n- Limited Matching\n- Chat Mode Only\n- 1 Hr/Day\n- No Teacher Access")
        if st.button("Choose Basic Plan"):
            st.session_state.selected_plan = "Basic"
    with col2:
        st.markdown("### 🔵 Premium — ₹499\n- Unlimited Matching\n- Video/Audio Rooms\n- Teacher Access\n- Daily Reminders\n- Notes Access")
        if st.button("Choose Premium Plan"):
            st.session_state.selected_plan = "Premium"
    with col3:
        st.markdown("### 🔴 Elite — ₹999\n- All Premium +\n- Mentorship\n- Job Support\n- Elite Teacher Sessions\n- Distraction Blocker")
        if st.button("Choose Elite Plan"):
            st.session_state.selected_plan = "Elite"
    if st.session_state.selected_plan:
        st.markdown(f"#### Proceed to Payment for **{st.session_state.selected_plan}** Plan")
        method = st.radio("Payment Method", ["UPI", "Card", "PayPal"])
        if method == "UPI":
            st.text_input("UPI ID")
        elif method == "Card":
            st.text_input("Card Number")
            st.text_input("Card Holder Name")
            st.text_input("Expiry Date (MM/YY)")
            st.text_input("CVV")
        elif method == "PayPal":
            st.text_input("PayPal Email")
        if st.button("Pay Now"):
            st.success(f"✅ Payment successful for {st.session_state.selected_plan} Plan!")

# 💬 Feedback
if menu == "💬 Feedback":
    st.subheader("💬 Share Your Feedback")
    with st.form("feedback_form"):
        fname = st.text_input("Your Name")
        femail = st.text_input("Email")
        rating = st.slider("Rate your experience", 1, 5)
        suggestions = st.text_area("Suggestions or Comments?")
        recommend = st.radio("Would you recommend StudySync?", ["Yes", "Maybe", "No"])
        fsubmit = st.form_submit_button("Submit Feedback")
        if fsubmit:
            st.session_state.feedbacks.append({
                "Name": fname,
                "Email": femail,
                "Rating": rating,
                "Suggestions": suggestions,
                "Recommend": recommend
            })
            st.success("🎉 Thank you for your feedback!")
