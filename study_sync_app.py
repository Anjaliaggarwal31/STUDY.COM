import streamlit as st
import pandas as pd
import random
import os
import ast

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

subjects = ["Maths", "Science", "English", "CS", "Economics", "Accounts", "Others"]
languages = ["English", "Hindi", "Others"]
timezones = ["IST", "UTC", "EST", "PST", "Others"]
genders = ["Select an option", "Male", "Female", "Others"]

# Quotes
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

# Sidebar Menu
menu_items = ["🏠 Home"]
if st.session_state.registered:
    menu_items += ["👤 Profile"]
else:
    menu_items += ["📝 Register"]
menu_items += ["🤝 Find a Partner", "💼 Subscription Plans", "🎯 Matched Partners", "💬 Feedback"]

menu = st.sidebar.radio("📌 Navigation", menu_items, index=menu_items.index(st.session_state.menu))
st.session_state.menu = menu

# Logout Button
if st.session_state.registered:
    if st.sidebar.button("🚪 Logout"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# Quote
st.markdown(f"<h5 style='text-align: center; color: gray;'>{quotes[menu]}</h5>", unsafe_allow_html=True)

# --- 🏠 HOME ---
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

# --- 📝 REGISTER ---
if menu == "📝 Register":
    tab1, tab2 = st.tabs(["👨‍🎓 Register as Student", "👩‍🏫 Register as Teacher"])

    # --- Student ---
    with tab1:
        with st.form("student_register_form"):
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

            submitted = st.form_submit_button("Register as Student")
            if submitted:
                required_fields = [name, email, final_gender, final_university, final_course, final_timezone, final_language]
                if (gender == "Others" and not gender_other) or \
                   (university == "Others" and not university_other) or \
                   (course == "Others" and not course_other) or \
                   (timezone == "Others" and not timezone_other) or \
                   (language == "Others" and not language_other) or \
                   ("Others" in study_goal and not custom_goal):
                    st.error("⚠️ Please specify all 'Others' values.")
                elif all(required_fields):
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
                        "ID_uploaded": uploaded_id.name if uploaded_id else "Not Provided",
                        "ProfilePic": "Not Provided",
                        "UserType": "Student"
                    }
                    st.session_state.user_email = email
                    st.session_state.registered = True

                    if os.path.exists("registered_users.csv"):
                        df = pd.read_csv("registered_users.csv")
                        df = pd.concat([df, pd.DataFrame([st.session_state.user_details])], ignore_index=True)
                    else:
                        df = pd.DataFrame([st.session_state.user_details])
                    df.to_csv("registered_users.csv", index=False)

                    st.success(f"🎉 Thank you for registering with us, **{name}**!")
                    st.balloons()
                    st.session_state.menu = "👤 Profile"
                    st.rerun()
                else:
                    st.error("⚠️ Please fill all required fields marked with *")

    # --- Teacher ---
    with tab2:
        with st.form("teacher_register_form"):
            tname = st.text_input("Full Name *")
            temail = st.text_input("Email *")

            course_expertise = st.selectbox("Course Expertise *", ["Select an option"] + top_courses)
            course_other = st.text_input("Please specify course *") if course_expertise == "Others" else ""
            final_course = course_other if course_expertise == "Others" else course_expertise

            subject = st.selectbox("Subject Expertise *", ["Select an option"] + subjects)
            subject_other = st.text_input("Please specify subject *") if subject == "Others" else ""
            final_subject = subject_other if subject == "Others" else subject

            fee = st.selectbox("Hourly Teaching Fee", ["₹200", "₹500", "₹1000", "$10", "$20"])
            duration = st.selectbox("Available Duration", ["1 hour", "2–3 hours", "Flexible"])

            university = st.selectbox("University *", ["Select an option"] + top_universities)
            university_other = st.text_input("Specify university *") if university == "Others" else ""
            final_university = university_other if university == "Others" else university

            status = st.radio("Current Status", ["Professor", "Faculty", "Other"])
            status_other = st.text_input("Specify status *") if status == "Other" else ""
            final_status = status_other if status == "Other" else status

            t_id = st.file_uploader("Upload your ID (Optional)")
            t_submit = st.form_submit_button("Register as Teacher")

            if t_submit:
                if (course_expertise == "Others" and not course_other) or \
                   (subject == "Others" and not subject_other) or \
                   (university == "Others" and not university_other) or \
                   (status == "Other" and not status_other):
                    st.error("⚠️ Please specify all 'Others' values.")
                elif tname and temail and final_subject != "Select an option" and final_course != "Select an option":
                    teacher_details = {
                        "Name": tname,
                        "Email": temail,
                        "Course": final_course,
                        "Subject": final_subject,
                        "Fee": fee,
                        "Duration": duration,
                        "University": final_university,
                        "Status": final_status,
                        "ID_uploaded": t_id.name if t_id else "Not Provided",
                        "ProfilePic": "Not Provided",
                        "UserType": "Teacher"
                    }
                    st.session_state.user_details = teacher_details
                    st.session_state.user_email = temail
                    st.session_state.registered = True

                    if os.path.exists("registered_users.csv"):
                        df = pd.read_csv("registered_users.csv")
                        df = pd.concat([df, pd.DataFrame([teacher_details])], ignore_index=True)
                    else:
                        df = pd.DataFrame([teacher_details])
                    df.to_csv("registered_users.csv", index=False)

                    st.success(f"✅ Thank you {tname} for registering as a teacher!")
                    st.session_state.menu = "👤 Profile"
                    st.rerun()
                else:
                    st.error("⚠️ Please fill all required fields.")
# --- 👤 Profile ---
if menu == "👤 Profile" and st.session_state.registered:
    st.markdown("### 👤 Your Profile")
    details = st.session_state.user_details

    with st.form("profile_form"):
        name = st.text_input("Full Name *", value=details.get("Name", ""))
        email = st.text_input("Email", value=details.get("Email", ""), disabled=True)

        if details.get("UserType") == "Student":
            gender = st.selectbox("Gender *", genders, index=genders.index(details.get("Gender", "Select an option")) if details.get("Gender") in genders else 0)
            gender_other = st.text_input("Please specify your gender *") if gender == "Others" else ""
            final_gender = gender_other if gender == "Others" else gender

            university = st.selectbox("University *", ["Select an option"] + top_universities,
                index=(["Select an option"] + top_universities).index(details.get("University", "Select an option")) if details.get("University") in (["Select an option"] + top_universities) else 0)
            university_other = st.text_input("Please specify your university *") if university == "Others" else ""
            final_university = university_other if university == "Others" else university

            course = st.selectbox("Course *", ["Select an option"] + top_courses,
                index=(["Select an option"] + top_courses).index(details.get("Course", "Select an option")) if details.get("Course") in (["Select an option"] + top_courses) else 0)
            course_other = st.text_input("Please specify your course *") if course == "Others" else ""
            final_course = course_other if course == "Others" else course

            timezone = st.selectbox("Time Zone *", ["Select an option"] + timezones,
                index=(["Select an option"] + timezones).index(details.get("Timezone", "Select an option")) if details.get("Timezone") in (["Select an option"] + timezones) else 0)
            timezone_other = st.text_input("Please specify your time zone *") if timezone == "Others" else ""
            final_timezone = timezone_other if timezone == "Others" else timezone

            language = st.selectbox("Preferred Language *", ["Select an option"] + languages,
                index=(["Select an option"] + languages).index(details.get("Language", "Select an option")) if details.get("Language") in (["Select an option"] + languages) else 0)
            language_other = st.text_input("Please specify your language *") if language == "Others" else ""
            final_language = language_other if language == "Others" else language

            predefined_goals = ["Crash Course", "Detailed Preparation", "Exam Tomorrow", "Professional Exam", "Competitive Exam", "Others"]
            current_goals = details.get("Goal", [])
            if isinstance(current_goals, str):
                try:
                    current_goals = ast.literal_eval(current_goals)
                except:
                    current_goals = [current_goals]
            goal = st.multiselect("Study Goal *", predefined_goals, default=current_goals)
            custom_goal = st.text_input("Please specify your goal *") if "Others" in goal else ""

            predefined_modes = ["Video 🎥", "Audio 🎧", "Notes 📄", "Chat 💬"]
            current_modes = details.get("Mode", [])
            if isinstance(current_modes, str):
                try:
                    current_modes = ast.literal_eval(current_modes)
                except:
                    current_modes = [current_modes]
            mode = st.multiselect("Study Mode", predefined_modes, default=current_modes)

        else:  # Teacher
            course = st.text_input("Course Expertise", value=details.get("Course", ""))
            subject = st.text_input("Subject Expertise", value=details.get("Subject", ""))
            fee = st.text_input("Fee", value=details.get("Fee", ""))
            duration = st.text_input("Available Duration", value=details.get("Duration", ""))
            university = st.text_input("University", value=details.get("University", ""))
            status = st.text_input("Status", value=details.get("Status", ""))

        st.markdown(f"**Previously Uploaded ID:** {details.get('ID_uploaded', 'Not Provided')}")
        uploaded_id = st.file_uploader("Update ID (Optional)", type=["png", "jpg", "jpeg", "pdf"])
        profile_pic = st.file_uploader("Update Profile Picture (Optional)", type=["png", "jpg", "jpeg"])

        if st.form_submit_button("Update"):
            if details.get("UserType") == "Student" and (
                (gender == "Others" and not gender_other) or
                (university == "Others" and not university_other) or
                (course == "Others" and not course_other) or
                (timezone == "Others" and not timezone_other) or
                (language == "Others" and not language_other) or
                ("Others" in goal and not custom_goal)
            ):
                st.error("⚠️ Please specify all 'Others' values before updating.")
            else:
                updated = {
                    "Name": name,
                    "Email": email,
                    "ID_uploaded": uploaded_id.name if uploaded_id else details.get("ID_uploaded", "Not Provided"),
                    "ProfilePic": profile_pic.name if profile_pic else details.get("ProfilePic", "Not Provided"),
                    "UserType": details.get("UserType", "")
                }

                if details["UserType"] == "Student":
                    updated.update({
                        "Gender": final_gender,
                        "University": final_university,
                        "Course": final_course,
                        "Timezone": final_timezone,
                        "Goal": goal + ([custom_goal] if custom_goal else []),
                        "Language": final_language,
                        "Mode": mode
                    })
                else:
                    updated.update({
                        "Course": course,
                        "Subject": subject,
                        "Fee": fee,
                        "Duration": duration,
                        "University": university,
                        "Status": status
                    })

                st.session_state.user_details = updated
                df = pd.read_csv("registered_users.csv")
                df.loc[df["Email"] == email] = pd.Series(updated)
                df.to_csv("registered_users.csv", index=False)
                st.success("✅ Profile updated successfully!")

# --- 🤝 Find a Partner ---
def generate_dummy_partners():
    names = ["Ankit", "Sneha", "Ravi", "Fatima", "Zhang", "Elena", "John", "Mei", "Ali", "Sara"]
    return pd.DataFrame([{ 
        "Name": random.choice(names),
        "Gender": random.choice(["Male", "Female"]),
        "Knowledge": random.choice(["Beginner", "Intermediate", "Advanced"]),
        "Subject": random.choice(subjects),
        "Language": random.choice(["English", "Hindi"]),
        "TimeZone": random.choice(timezones),
        "Hours": random.choice(["1 hour", "2 hours", "3–5 hours", "6+ hours"])
    } for _ in range(10)])

if menu == "🤝 Find a Partner":
    if not st.session_state.registered:
        st.warning("Please register first to find a partner.")
    else:
        with st.form("partner_form"):
            gender = st.selectbox("Preferred Partner Gender *", ["Select an option", "Any", "Male", "Female", "Others"])
            gender_other = st.text_input("Specify partner gender *") if gender == "Others" else ""
            final_gender = gender_other if gender == "Others" else gender

            knowledge = st.selectbox("Partner's Knowledge Level *", ["Select an option", "Beginner", "Intermediate", "Advanced"])
            subject = st.selectbox("Subject to Study *", ["Select an option"] + subjects)
            subject_other = st.text_input("Please specify subject *") if subject == "Others" else ""
            final_subject = subject_other if subject == "Others" else subject

            language = st.selectbox("Partner's Language *", ["Select an option"] + languages)
            language_other = st.text_input("Specify partner language *") if language == "Others" else ""
            final_language = language_other if language == "Others" else language

            timezone = st.selectbox("Partner's Time Zone *", ["Select an option"] + timezones)
            timezone_other = st.text_input("Specify partner time zone *") if timezone == "Others" else ""
            final_timezone = timezone_other if timezone == "Others" else timezone

            hours = st.selectbox("Preferred Study Hours *", ["Select an option", "Any", "1 hour", "2 hours", "3–5 hours", "6+ hours"])

            search = st.form_submit_button("Find Matches")
            if search:
                if (gender == "Others" and not gender_other) or \
                   (subject == "Others" and not subject_other) or \
                   (language == "Others" and not language_other) or \
                   (timezone == "Others" and not timezone_other):
                    st.error("⚠️ Please specify all 'Others' values.")
                elif "Select an option" in [gender, knowledge, subject, language, timezone, hours]:
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

                    filtered["MatchedBy"] = st.session_state.user_email
                    if os.path.exists("matched_partners.csv"):
                        filtered.to_csv("matched_partners.csv", mode="a", index=False, header=False)
                    else:
                        filtered.to_csv("matched_partners.csv", index=False)

                    st.subheader("🎯 Your Matched Study Partners")
                    display_cols = ["Name"] + [k for k, v in st.session_state.partner_filters.items() if v]
                    st.table(filtered[display_cols])

# --- 🎯 Matched Partners ---
if menu == "🎯 Matched Partners":
    if st.session_state.partners:
        st.subheader("🎯 Your Matched Study Partners")
        df = pd.DataFrame(st.session_state.partners)
        filters = st.session_state.partner_filters
        show_cols = ["Name"] + [col for col, val in filters.items() if val]
        st.table(df[show_cols])
    else:
        st.info("No matches found yet. Try 'Find a Partner'.")

# --- 💼 Subscription Plans ---
if menu == "💼 Subscription Plans":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🟢 Basic — ₹0")
        st.markdown("- ✅ Limited Partner Matching\n- 📄 Chat Mode Only\n- ⏰ 1 Hour/Day Limit\n- 🚫 No Teacher Access")
        if st.button("Choose Basic Plan"):
            st.session_state.selected_plan = "Basic"
    with col2:
        st.markdown("### 🔵 Premium — ₹499")
        st.markdown("- ✅ Unlimited Matching\n- 🎥 Video & Audio Rooms\n- 📩 Reminders & Planners\n- 👨‍🏫 Teacher Access\n- 📚 Notes Downloads")
        if st.button("Choose Premium Plan"):
            st.session_state.selected_plan = "Premium"
    with col3:
        st.markdown("### 🔴 Elite — ₹999")
        st.markdown("- 🏆 All Premium Features\n- 💼 Mentorship Access\n- 🎯 Job/Internship Help\n- 🧑‍🏫 Free Teacher Sessions\n- 🛡️ Distraction Blocker")
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

# --- 💬 Feedback ---
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
