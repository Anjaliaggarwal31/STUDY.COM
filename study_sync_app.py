import streamlit as st
import pandas as pd
import random
import os

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
    if "user_email" not in st.session_state:
        st.session_state.user_email = None
    if "profile_pic" not in st.session_state:
        st.session_state.profile_pic = None

    if os.path.exists("registered_users.csv") and st.session_state.user_email:
        df = pd.read_csv("registered_users.csv")
        if st.session_state.user_email in df["Email"].values:
            user_row = df[df["Email"] == st.session_state.user_email].iloc[0]
            st.session_state.user_details = user_row.to_dict()
            st.session_state.registered = True

init_session()

# Dropdown Options
top_universities = ["Harvard University", "Stanford University", "MIT", "University of Cambridge", "University of Oxford",
                    "California Institute of Technology", "ETH Zurich", "University of Chicago", "Princeton University",
                    "National University of Singapore (NUS)", "Tsinghua University", "IIT", "IIM", "NIT", "DERI",
                    "International", "Others"]

top_courses = ["Computer Science", "Engineering", "Economics", "Law", "Business Administration", "Psychology",
               "Political Science", "Physics", "Mathematics", "Biology", "UG", "PG", "Professional", "PhD", "Others"]

languages = ["English", "Hindi", "Others"]
timezones = ["IST", "UTC", "EST", "PST", "Others"]
genders = ["Select an option", "Male", "Female", "Others"]

# Motivational Quotes
quotes = {
    "🏠 Home": "“Learning becomes joyful when shared with a friend.”",
    "📝 Register": "“Your journey to better learning begins with a simple registration.”",
    "👤 Profile": "“Your profile, your progress.”",
    "🤝 Find a Partner": "“A study partner turns the impossible into achievable.”",
    "💼 Subscription Plans": "“Invest in learning — it pays the best interest.”",
    "🎯 Matched Partners": "“Two minds studying together go further than one.”",
    "💬 Feedback": "“Your voice helps us shape a smarter StudySync.”"
}

# Header
st.markdown("<h1 style='text-align: center;'>🚀 StudySync</h1>", unsafe_allow_html=True)

# Sidebar
menu_items = ["🏠 Home"]
if st.session_state.registered:
    menu_items += ["👤 Profile"]
else:
    menu_items += ["📝 Register"]
menu_items += ["🤝 Find a Partner", "💼 Subscription Plans", "🎯 Matched Partners", "💬 Feedback"]
menu = st.sidebar.radio("📌 Navigation", menu_items, index=menu_items.index(st.session_state.menu))
st.session_state.menu = menu

# Logout
if st.session_state.registered:
    if st.sidebar.button("🚪 Logout"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# Quote
st.markdown(f"<h5 style='text-align: center; color: gray;'>{quotes[menu]}</h5>", unsafe_allow_html=True)

# Sample Partner Generator
def generate_dummy_partners():
    names = ["Disha", "Kartik", "Harsh", "Mehak", "Aarav", "Anaya", "Ishaan", "Riya", "Kabir", "Tanvi"]
    genders = ["Male", "Female"]
    knowledge_levels = ["Beginner", "Intermediate", "Advanced"]
    subjects = ["Maths", "Science", "English", "CS", "Economics", "Accounts"]
    languages = ["English", "Hindi"]
    timezones = ["IST", "UTC", "EST", "PST"]
    hours = ["1 hour", "2 hours", "3–5 hours"]
    return pd.DataFrame([{
        "Name": random.choice(names),
        "Gender": random.choice(genders),
        "Knowledge": random.choice(knowledge_levels),
        "Subject": random.choice(subjects),
        "Language": random.choice(languages),
        "TimeZone": random.choice(timezones),
        "Hours": random.choice(hours)
    } for _ in range(50)])

# 🏠 Home
if menu == "🏠 Home":
    st.success("Welcome to StudySync — your personalized study buddy matcher! 🎓")
    if not st.session_state.registered:
        email_input = st.text_input("🔐 Already Registered? Enter your Email:")
        if email_input:
            if os.path.exists("registered_users.csv"):
                df = pd.read_csv("registered_users.csv")
                if email_input in df["Email"].values:
                    st.session_state.user_email = email_input
                    st.rerun()
                else:
                    st.warning("Email not found. Please register first.")

# 📝 Register
if menu == "📝 Register" and not st.session_state.registered:
    st.markdown("### 👤 Student Registration")
    with st.form("register_form"):
        name = st.text_input("Full Name *")
        email = st.text_input("Email *")

        gender = st.selectbox("Gender *", genders)
        gender_other = st.text_input("Please specify your gender *") if gender == "Others" else ""
        final_gender = gender_other if gender == "Others" else gender

        university = st.selectbox("University *", ["Select an option"] + top_universities)
        university_other = st.text_input("Please specify your university *") if university == "Others" else ""
        final_university = university_other if university == "Others" else university

        course = st.selectbox("Course *", ["Select an option"] + top_courses)
        course_other = st.text_input("Please specify your course *") if course == "Others" else ""
        final_course = course_other if course == "Others" else course

        timezone = st.selectbox("Time Zone *", ["Select an option"] + timezones)
        timezone_other = st.text_input("Please specify your time zone *") if timezone == "Others" else ""
        final_timezone = timezone_other if timezone == "Others" else timezone

        study_goal = st.multiselect("Your Study Goal *", ["Crash Course", "Detailed Preparation", "Exam Tomorrow", "Professional Exam", "Competitive Exam", "Others"])
        custom_goal = st.text_input("Please specify your goal *") if "Others" in study_goal else ""

        language = st.selectbox("Preferred Language *", ["Select an option"] + languages)
        language_other = st.text_input("Please specify your language *") if language == "Others" else ""
        final_language = language_other if language == "Others" else language

        mode = st.multiselect("Preferred Study Mode", ["Video 🎥", "Audio 🎧", "Notes 📄", "Chat 💬"])
        uploaded_id = st.file_uploader("Upload Your ID (Optional)")
        profile_pic = st.file_uploader("Upload Your Profile Picture (Optional)", type=["png", "jpg", "jpeg"])

        submitted = st.form_submit_button("Submit")

        if submitted:
            required = all([
                name, email,
                final_gender not in ["", "Select an option"],
                final_university not in ["", "Select an option"],
                final_course not in ["", "Select an option"],
                final_timezone not in ["", "Select an option"],
                final_language not in ["", "Select an option"]
            ])
            if required:
                user_data = {
                    "Name": name, "Email": email, "Gender": final_gender, "University": final_university,
                    "Course": final_course, "Timezone": final_timezone,
                    "Goal": "|".join(study_goal + ([custom_goal] if custom_goal else [])),
                    "Language": final_language, "Mode": "|".join(mode),
                    "ID_uploaded": uploaded_id.name if uploaded_id else "Not Provided",
                    "ProfilePic": profile_pic.name if profile_pic else "Not Provided"
                }
                st.session_state.user_details = user_data
                st.session_state.user_email = email
                st.session_state.registered = True
                if os.path.exists("registered_users.csv"):
                    df = pd.read_csv("registered_users.csv")
                    if email not in df["Email"].values:
                        df = pd.concat([df, pd.DataFrame([user_data])], ignore_index=True)
                        df.to_csv("registered_users.csv", index=False)
                else:
                    pd.DataFrame([user_data]).to_csv("registered_users.csv", index=False)
                st.success(f"🎉 Thanks for registering, {name}!")
                st.session_state.menu = "🤝 Find a Partner"
                st.rerun()
            else:
                st.error("⚠️ Please fill all required fields")

# 👤 Profile
if menu == "👤 Profile" and st.session_state.registered:
    st.markdown("### 👤 Your Profile")
    details = st.session_state.user_details

    with st.form("profile_form"):
        name = st.text_input("Full Name *", value=details.get("Name", ""))
        email = st.text_input("Email", value=details.get("Email", ""), disabled=True)

        gender = st.selectbox("Gender *", genders, index=genders.index(details.get("Gender", "Select an option")) if details.get("Gender", "Select an option") in genders else 0)
        gender_other = st.text_input("Please specify your gender *") if gender == "Others" else ""
        final_gender = gender_other if gender == "Others" else gender

        university = st.selectbox("University *", ["Select an option"] + top_universities, index=(["Select an option"] + top_universities).index(details.get("University", "Select an option")) if details.get("University", "Select an option") in (["Select an option"] + top_universities) else 0)
        university_other = st.text_input("Please specify your university *") if university == "Others" else ""
        final_university = university_other if university == "Others" else university

        course = st.selectbox("Course *", ["Select an option"] + top_courses, index=(["Select an option"] + top_courses).index(details.get("Course", "Select an option")) if details.get("Course", "Select an option") in (["Select an option"] + top_courses) else 0)
        course_other = st.text_input("Please specify your course *") if course == "Others" else ""
        final_course = course_other if course == "Others" else course

        timezone = st.selectbox("Time Zone *", ["Select an option"] + timezones, index=(["Select an option"] + timezones).index(details.get("Timezone", "Select an option")) if details.get("Timezone", "Select an option") in (["Select an option"] + timezones) else 0)
        language = st.selectbox("Preferred Language *", ["Select an option"] + languages, index=(["Select an option"] + languages).index(details.get("Language", "Select an option")) if details.get("Language", "Select an option") in (["Select an option"] + languages) else 0)

        goal = st.text_input("Study Goal *", value=details.get("Goal", ""))
        mode = st.text_input("Study Mode", value=details.get("Mode", ""))
        st.markdown(f"**Uploaded ID:** {details.get('ID_uploaded', 'Not Provided')}")
        profile_pic = st.file_uploader("Update Profile Picture (Optional)", type=["png", "jpg", "jpeg"])

        if st.form_submit_button("Update"):
            updated = {
                "Name": name, "Email": email, "Gender": final_gender, "University": final_university,
                "Course": final_course, "Timezone": timezone, "Goal": goal, "Language": language,
                "Mode": mode, "ID_uploaded": details.get("ID_uploaded", "Not Provided"),
                "ProfilePic": profile_pic.name if profile_pic else details.get("ProfilePic", "Not Provided")
            }
            st.session_state.user_details = updated
            df = pd.read_csv("registered_users.csv")
            df.loc[df["Email"] == email] = updated
            df.to_csv("registered_users.csv", index=False)
            st.success("✅ Profile updated successfully!")
# 🤝 Find a Partner
if menu == "🤝 Find a Partner":
    if not st.session_state.registered:
        st.warning("Please register first to find a partner.")
    else:
        with st.form("partner_form"):
            gender = st.selectbox("Preferred Partner Gender *", ["Select an option", "Any", "Male", "Female", "Others"])
            gender_other = st.text_input("Specify partner gender *") if gender == "Others" else ""
            final_gender = gender_other if gender == "Others" else gender

            knowledge = st.selectbox("Partner's Knowledge Level *", ["Select an option", "Beginner", "Intermediate", "Advanced"])
            subject = st.selectbox("Subject to Study *", ["Select an option", "Maths", "Science", "English", "CS", "Economics", "Accounts", "Others"])
            subject_other = st.text_input("Please specify subject *") if subject == "Others" else ""
            final_subject = subject_other if subject == "Others" else subject

            language = st.selectbox("Partner's Language *", ["Select an option", "English", "Hindi", "Others"])
            language_other = st.text_input("Specify partner language *") if language == "Others" else ""
            final_language = language_other if language == "Others" else language

            timezone = st.selectbox("Partner's Time Zone *", ["Select an option"] + timezones)
            timezone_other = st.text_input("Specify partner time zone *") if timezone == "Others" else ""
            final_timezone = timezone_other if timezone == "Others" else timezone

            hours = st.selectbox("Preferred Study Hours *", ["Select an option", "Any", "1 hour", "2 hours", "3–5 hours", "6+ hours"])

            search = st.form_submit_button("Find Matches")

            if search:
                required = [gender, knowledge, subject, language, timezone, hours]
                if "Select an option" in required:
                    st.error("⚠️ Please select valid options for all fields.")
                else:
                    df = generate_dummy_partners()
                    filtered = df[
                        ((df["Gender"] == final_gender) | (final_gender == "Any")) &
                        (df["Knowledge"] == knowledge) &
                        (df["Subject"].str.lower() == final_subject.lower()) &
                        (df["Language"] == final_language) &
                        (df["TimeZone"] == final_timezone) &
                        ((df["Hours"] == hours) | (hours == "Any"))
                    ]
                    if not filtered.empty:
                        st.success(f"✅ Found {len(filtered)} matching partner(s)!")
                    else:
                        st.warning("😕 No exact match found. Showing similar partners by knowledge.")
                        filtered = df[df["Knowledge"] == knowledge]

                    st.session_state.partners = filtered.to_dict("records")
                    st.session_state.partner_filters = {
                        "Gender": None if final_gender == "Any" else final_gender,
                        "Knowledge": knowledge,
                        "Subject": final_subject,
                        "Language": final_language,
                        "TimeZone": final_timezone,
                        "Hours": None if hours == "Any" else hours
                    }
                    st.session_state.matched = True

                    # Save matches
                    filtered["MatchedBy"] = st.session_state.user_email
                    if os.path.exists("matched_partners.csv"):
                        filtered.to_csv("matched_partners.csv", mode="a", index=False, header=False)
                    else:
                        filtered.to_csv("matched_partners.csv", index=False)

                    st.subheader("🎯 Your Matched Study Partners")
                    display_cols = ["Name"] + [k for k, v in st.session_state.partner_filters.items() if v]
                    st.table(filtered[display_cols])

# 🎯 Matched Partners
if menu == "🎯 Matched Partners":
    if st.session_state.partners:
        st.subheader("🎯 Your Matched Study Partners")
        df = pd.DataFrame(st.session_state.partners)
        filters = st.session_state.partner_filters
        show_cols = ["Name"] + [col for col, val in filters.items() if val]
        st.table(df[show_cols])
    else:
        st.info("No matches found yet. Try 'Find a Partner'.")

# 💼 Subscription Plans
if menu == "💼 Subscription Plans":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🟢 Basic — ₹0")
        st.markdown("""
        - ✅ Limited Partner Matching  
        - 📄 Chat Mode Only  
        - ⏰ 1 Hour/Day Limit  
        - 🚫 No Teacher Access  
        """)
        if st.button("Choose Basic Plan"):
            st.session_state.selected_plan = "Basic"
    with col2:
        st.markdown("### 🔵 Premium — ₹499")
        st.markdown("""
        - ✅ Unlimited Matching  
        - 🎥 Video & Audio Rooms  
        - 📩 Reminders & Planners  
        - 👨‍🏫 Teacher Access  
        - 📚 Notes Downloads  
        """)
        if st.button("Choose Premium Plan"):
            st.session_state.selected_plan = "Premium"
    with col3:
        st.markdown("### 🔴 Elite — ₹999")
        st.markdown("""
        - 🏆 All Premium Features  
        - 💼 Mentorship Access  
        - 🎯 Job/Internship Help  
        - 🧑‍🏫 Free Teacher Sessions  
        - 🛡️ Distraction Blocker  
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
