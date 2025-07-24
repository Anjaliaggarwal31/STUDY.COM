import streamlit as st
import pandas as pd
import random
import time

st.set_page_config(page_title="StudySync App", layout="wide")

# Initialize session state
def init_session():
    st.session_state.setdefault("registered", False)
    st.session_state.setdefault("matched", False)
    st.session_state.setdefault("partners", [])
    st.session_state.setdefault("menu", "🏠 Home")
    st.session_state.setdefault("partner_filters", {})
    st.session_state.setdefault("selected_plan", None)
    st.session_state.setdefault("user_details", {})
    st.session_state.setdefault("feedbacks", [])
    st.session_state.setdefault("messages", [])
init_session()

# Animated intro
if st.session_state.menu == "🏠 Home":
    with st.empty():
        for i in range(1, 101, 20):
            st.markdown(f"### ⏳ Loading StudySync... {i}%")
            time.sleep(0.1)
    st.empty()

# Header and Navigation
st.markdown("<h1 style='text-align: center;'>🚀 StudySync</h1>", unsafe_allow_html=True)

menu = st.sidebar.radio("📌 Navigation",
    ["🏠 Home", "📝 Register", "🤝 Find a Partner", "💬 Messages", "📤 Export Feedback", "📚 Teacher Dashboard"],
    index=["🏠 Home", "📝 Register", "🤝 Find a Partner", "💬 Messages", "📤 Export Feedback", "📚 Teacher Dashboard"].index(st.session_state.menu))
st.session_state.menu = menu

quotes = {
    "🏠 Home": "“Learning becomes joyful when shared with a friend.”",
    "📝 Register": "“Your journey to better learning begins with a simple registration.”",
    "🤝 Find a Partner": "“A study partner turns the impossible into achievable.”",
    "💬 Messages": "“Good communication is key to collaboration.”",
    "📤 Export Feedback": "“Feedback helps us grow — let's share it!”",
    "📚 Teacher Dashboard": "“Empower educators to lead learning.”"
}

st.markdown(f"<h5 style='text-align: center; color: gray;'>{quotes[menu]}</h5>", unsafe_allow_html=True)

# Distraction Blocker
if st.sidebar.toggle("🛑 Enable Distraction Blocker"):
    st.markdown("<style>div[data-testid='stSidebar'] {visibility: hidden;} body {background: #000; color: white;}</style>", unsafe_allow_html=True)
    st.warning("🔒 Distraction Blocker Activated — Focus Mode Enabled")

# Dummy Data Generator
def generate_dummy_partners():
    names = ["Disha", "Kartik", "Harsh", "Mehak"]
    return pd.DataFrame([{"Name": random.choice(names), "Gender": "Female", "Knowledge": "Intermediate",
                          "Subject": "Maths", "Language": "English", "TimeZone": "IST"} for _ in range(5)])

# Registration Page
if menu == "📝 Register":
    with st.form("reg_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email")
        role = st.radio("Role", ["Student", "Teacher"])
        subject = st.text_input("Subject Interested/Expertise")
        submit = st.form_submit_button("Register")
        if submit and name and email and subject:
            st.session_state.registered = True
            st.session_state.user_details = {"name": name, "email": email, "subject": subject, "role": role}
            st.success(f"Registered as {role}. Welcome, {name}!")

# Partner Matching Page
if menu == "🤝 Find a Partner":
    if not st.session_state.registered:
        st.warning("Please register first.")
    else:
        with st.form("match_form"):
            subject = st.text_input("Enter subject to find partner")
            submit = st.form_submit_button("Find Matches")
            if submit and subject:
                st.session_state.partners = generate_dummy_partners().to_dict("records")
                st.success("Found matching partners!")

        if st.session_state.partners:
            st.subheader("🎯 Matched Partners")
            st.table(pd.DataFrame(st.session_state.partners))

# Messaging Window
if menu == "💬 Messages":
    st.subheader("💬 Partner Messaging")
    with st.form("chat_form"):
        message = st.text_input("Type a message")
        if st.form_submit_button("Send") and message:
            st.session_state.messages.append(message)
    st.write("---")
    for msg in st.session_state.messages[::-1]:
        st.success(f"🗨️ {msg}")

# Export Feedback Page
if menu == "📤 Export Feedback":
    st.subheader("📤 Export Feedback")
    if st.button("Download as Excel"):
        df = pd.DataFrame(st.session_state.feedbacks)
        df.to_excel("feedbacks.xlsx", index=False)
        st.success("Excel downloaded. (Check working dir)")

    if st.button("Download as PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for fb in st.session_state.feedbacks:
            for k, v in fb.items():
                pdf.cell(200, 10, txt=f"{k}: {v}", ln=True)
            pdf.cell(200, 10, txt="---", ln=True)
        pdf.output("feedbacks.pdf")
        st.success("PDF downloaded. (Check working dir)")

# Teacher Dashboard
if menu == "📚 Teacher Dashboard":
    st.subheader("📚 Teacher Dashboard")
    if st.session_state.user_details.get("role") == "Teacher":
        st.write(f"👋 Hello, {st.session_state.user_details['name']}")
        st.write(f"📧 {st.session_state.user_details['email']}")
        st.write(f"📘 Subject: {st.session_state.user_details['subject']}")
        st.info("You have 4 students interested in your subject!")
    else:
        st.warning("Only teachers can access this dashboard.")
