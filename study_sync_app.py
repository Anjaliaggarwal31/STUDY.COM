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

# App Header
st.markdown("""
    <h1 style='text-align: center;'>🚀 StudySync</h1>
    <h4 style='text-align: center; color: gray;'>"Study alone if you must, but find your tribe and learn faster."</h4>
""", unsafe_allow_html=True)

# Sidebar Menu
menu = st.sidebar.radio("📌 Navigation", 
    ["🏠 Home", "📝 Register", "🤝 Find a Partner", "💼 Subscription Plans", "👩‍🏫 Teacher Registration", "🎯 Matched Partners", "💬 Feedback"],
    index=["🏠 Home", "📝 Register", "🤝 Find a Partner", "💼 Subscription Plans", "👩‍🏫 Teacher Registration", "🎯 Matched Partners", "💬 Feedback"].index(st.session_state.menu)
)
st.session_state.menu = menu

# Dummy Partner Generator
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

# 🏠 Home
if menu == "🏠 Home":
    st.success("Welcome to StudySync — your personalized study buddy matcher! 🎓")
    st.info("Use the sidebar to register, find a study partner, or explore subscriptions.")

# 📝 Register
if menu == "📝 Register":
    with st.form("register_form"):
        name = st.text_input("Full Name *")
        email = st.text_input("Email *")
        gender = st.selectbox("Gender *", ["Select an option", "Male", "Female", "Others"])
        gender_other = st.text_input("Please specify your gender *") if gender == "Others" else ""
        final_gender = gender_other if gender == "Others" else gender
        university = st.selectbox("University *", ["Select an option", "IIT", "IIM", "NIT", "DERI", "International", "Others"])
        university_other = st.text_input("Please specify your university *") if university == "Others" else ""
        final_university = university_other if university == "Others" else university
        course = st.selectbox("Course *", ["Select an option", "UG", "PG", "Professional", "PhD", "Others"])
        course_other = st.text_input("Please specify your course *") if course == "Others" else ""
        final_course = course_other if course == "Others" else course
        timezone = st.selectbox("Time Zone *", ["Select an option", "IST", "UTC", "EST", "PST", "Others"])
        timezone_other = st.text_input("Please specify your time zone *") if timezone == "Others" else ""
        final_timezone = timezone_other if timezone == "Others" else timezone
        study_goal = st.multiselect("Your Study Goal *", ["Crash Course", "Detailed Preparation", "Exam Tomorrow", "Professional Exam", "Competitive Exam", "Others"])
        custom_goal = st.text_input("Please specify your goal *") if "Others" in study_goal else ""
        language = st.selectbox("Preferred Language *", ["Select an option", "English", "Hindi", "Other"])
        language_other = st.text_input("Please specify your language *") if language == "Other" else ""
        final_language = language_other if language == "Other" else language
        mode = st.multiselect("Preferred Study Mode", ["Video 🎥", "Audio 🎧", "Notes 📄", "Chat 💬"])
        uploaded_id = st.file_uploader("Upload Your ID *")
        submitted = st.form_submit_button("Submit")
        if submitted:
            if name and email and final_gender != "Select an option" and final_university != "Select an option" and final_course != "Select an option" and final_timezone != "Select an option" and final_language != "Select an option" and uploaded_id:
                st.session_state.user_details = {
                    "Name": name,
                    "Email": email,
                    "Gender": final_gender,
                    "University": final_university,
                    "Course": final_course,
                    "Timezone": final_timezone,
                    "Goal": study_goal + ([custom_goal] if custom_goal else []),
                    "Language": final_language,
                    "Mode": mode,
                    "ID_uploaded": uploaded_id.name
                }
                st.session_state.registered = True
                st.success(f"🎉 Thank you for registering with us, **{name}**!")
                st.balloons()
                st.session_state.menu = "🤝 Find a Partner"
                st.rerun()
            else:
                st.error("⚠️ Please fill all required fields marked with *")

# 🤝 Find a Partner
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
            subject_other = st.text_input("Please specify subject *") if subject == "Others" else ""
            final_subject = subject_other if subject == "Others" else subject
            language = st.selectbox("Partner's Language", ["English", "Hindi", "Other"])
            language_other = st.text_input("Specify partner language *") if language == "Other" else ""
            final_language = language_other if language == "Other" else language
            timezone = st.selectbox("Partner's Time Zone", ["IST", "UTC", "EST", "PST", "Others"])
            timezone_other = st.text_input("Specify partner time zone *") if timezone == "Others" else ""
            final_timezone = timezone_other if timezone == "Others" else timezone
            search = st.form_submit_button("Find Matches")
            if search:
                df = generate_dummy_partners()
                filtered = df[
                    ((df["Gender"] == final_gender) | (final_gender == "Any")) &
                    (df["Knowledge"] == knowledge) &
                    (df["Subject"].str.lower() == final_subject.lower()) &
                    (df["Language"] == final_language) &
                    (df["TimeZone"] == final_timezone)  # Strict TimeZone match
                ]
                st.session_state.partners = filtered.to_dict("records")
                st.session_state.partner_filters = {
                    "Gender": None if final_gender == "Any" else final_gender,
                    "Knowledge": knowledge,
                    "Subject": final_subject,
                    "Language": final_language,
                    "TimeZone": final_timezone
                }
                st.session_state.matched = True
                st.success(f"✅ Found {len(filtered)} partner(s) matching your preference!")
                if not filtered.empty:
                    st.subheader("🎯 Your Matched Study Partners")
                    show_cols = ["Name"] + [col for col, val in st.session_state.partner_filters.items() if val and val != "Others"]
                    st.table(filtered[show_cols])
                else:
                    st.warning("No matches found for the selected criteria.")

# 🎯 Matched Partners
if menu == "🎯 Matched Partners":
    if st.session_state.partners:
        st.subheader("🎯 Your Matched Study Partners")
        df = pd.DataFrame(st.session_state.partners)
        filters = st.session_state.partner_filters
        show_cols = ["Name"] + [col for col, val in filters.items() if val and val != "Others"]
        st.table(df[show_cols])
    else:
        st.info("You don't have any matches yet. Go to 'Find a Partner' to search.")

# 💼 Subscription Plans
if menu == "💼 Subscription Plans":
    st.subheader("💼 Subscription Tiers")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🟢 Basic — ₹0")
        st.markdown("""
        - ✅ Limited Partner Matching  
        - 📄 Access to Chat Mode Only  
        - ⏰ 1 Hour/Day Session Limit  
        - 🚫 No Teacher Access  
        """)
        if st.button("Choose Basic Plan"):
            st.session_state.selected_plan = "Basic"
    with col2:
        st.markdown("### 🔵 Premium — ₹499")
        st.markdown("""
        - ✅ Unlimited Matching  
        - 🎥 Video & Audio Study Rooms  
        - 📩 Daily Reminder & Planner  
        - 👨‍🏫 Access to Verified Teachers  
        - 📚 Notes Download Access  
        """)
        if st.button("Choose Premium Plan"):
            st.session_state.selected_plan = "Premium"
    with col3:
        st.markdown("### 🔴 Elite — ₹999")
        st.markdown("""
        - 🏆 All Premium Features  
        - 💼 1:1 Mentorship Access  
        - 🎯 Job/Internship Placement Help  
        - 🧑‍🏫 Free Elite Teacher Sessions  
        - 🛡️ Study Distraction Blocker  
        """)
        if st.button("Choose Elite Plan"):
            st.session_state.selected_plan = "Elite"
    if st.session_state.selected_plan:
        st.markdown(f"### Proceed to Payment for **{st.session_state.selected_plan}** Plan")
        method = st.radio("Choose Payment Method", ["UPI", "Credit/Debit Card", "PayPal"])
        if method == "UPI":
            st.text_input("Enter UPI ID")
        elif method == "Credit/Debit Card":
            st.text_input("Card Number")
            st.text_input("Card Holder Name")
            st.text_input("Expiry Date (MM/YY)")
            st.text_input("CVV")
        elif method == "PayPal":
            st.text_input("PayPal Email")
        if st.button("Pay Now"):
            st.success(f"✅ Payment successful for {st.session_state.selected_plan} Plan!")

# 👩‍🏫 Teacher Registration
if menu == "👩‍🏫 Teacher Registration":
    with st.form("teacher_form"):
        tname = st.text_input("Full Name *")
        subject = st.text_input("Subject Expertise *")
        fee = st.selectbox("Hourly Teaching Fee", ["₹200", "₹500", "₹1000", "$10", "$20"])
        duration = st.selectbox("Available Duration", ["1 hour", "2–3 hours", "Flexible"])
        university = st.selectbox("University *", ["IIT", "IIM", "Other"])
        university_other = st.text_input("Specify university *") if university == "Other" else ""
        final_university = university_other if university == "Other" else university
        status = st.radio("Current Status", ["Student", "Faculty", "Other"])
        status_other = st.text_input("Specify status *") if status == "Other" else ""
        final_status = status_other if status == "Other" else status
        t_id = st.file_uploader("Upload your ID *")
        t_submit = st.form_submit_button("Register as Teacher")
        if t_submit:
            if tname and subject and t_id:
                st.success(f"✅ Thank you {tname} for registering as a teacher! We’ll reach out to you soon.")
            else:
                st.error("Please fill all required fields.")

# 💬 Feedback
if menu == "💬 Feedback":
    st.subheader("💬 Share Your Feedback")
    with st.form("feedback_form"):
        fname = st.text_input("Your Name")
        femail = st.text_input("Email")
        rating = st.slider("Rate your experience", 1, 5)
        suggestions = st.text_area("Any suggestions or feedback?")
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
