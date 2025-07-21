streamlit run study_sync_app.py
import streamlit as st
import pandas as pd
from PIL import Image
from datetime import datetime

# -------------------- Sample College Data --------------------
colleges = {
    "IIT Delhi": 15,
    "IIT Bombay": 20,
    "IIM Bangalore": 10,
    "DU (Delhi University)": 5,
    "JNU": 5,
    "BITS Pilani": 20,
    "Others": 0
}

# -------------------- Page Configuration --------------------
st.set_page_config(page_title="StudySync - Study Partner App", layout="centered")

# -------------------- Sidebar Menu --------------------
menu = [
    "Home", 
    "Register", 
    "Login", 
    "Find Study Partner", 
    "Subscription", 
    "College Onboarding"
]
choice = st.sidebar.selectbox("📋 Menu", menu)

# -------------------- Home --------------------
if choice == "Home":
    st.title("🎓 StudySync - Connect. Study. Succeed.")
    st.subheader("🌍 Find study partners or groups worldwide.")
    st.markdown("Built for students who struggle to find serious study buddies.")
    st.image("https://cdn.pixabay.com/photo/2020/03/31/16/16/online-4983591_1280.jpg", use_column_width=True)
    st.info("💡 Free for 1 year • Upgrade to get teacher assistance, job placement support & more!")

# -------------------- Registration --------------------
elif choice == "Register":
    st.header("🔐 Student Registration")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    college = st.selectbox("Select Your College", list(colleges.keys()))
    education = st.selectbox("Current Education Level", ["UG", "PG", "PhD", "Others"])
    discipline = st.selectbox("Discipline", ["Engineering", "Science", "Arts", "Commerce", "Law", "Medical", "Other"])
    id_card = st.file_uploader("Upload Student ID (JPEG/PNG/PDF)")
    password = st.text_input("Create Password", type='password')
    register_btn = st.button("Register")

    if register_btn:
        if name and email and id_card:
            st.success(f"🎉 Welcome {name}! You have successfully registered.")
        else:
            st.warning("⚠️ Please fill all required fields!")

# -------------------- Login --------------------
elif choice == "Login":
    st.header("🔑 Login to StudySync")
    email = st.text_input("Email")
    password = st.text_input("Password", type='password')
    login_btn = st.button("Login")

    if login_btn:
        if email and password:
            st.success(f"Welcome back! You're now logged in.")
        else:
            st.warning("⚠️ Please enter email and password.")

# -------------------- Find Study Partner --------------------
elif choice == "Find Study Partner":
    st.header("👥 Match With Study Partner or Join Group")
    discipline = st.selectbox("Discipline", ["Engineering", "Science", "Arts", "Commerce", "Law", "Medical", "Other"])
    subject = st.selectbox("Preferred Subject", ["Math", "AI/ML", "Finance", "Python", "Marketing", "Other"])
    time_slot = st.time_input("Preferred Study Time")
    mode = st.radio("Study Mode", ["1-on-1 Partner", "Group Study"])
    ready_status = st.checkbox("✅ Ready to Study Now")

    if ready_status:
        st.success("You're now visible to others as 'Ready to Study'!")

    if st.button("Search Partner/Group"):
        st.success(f"🔍 Matching {discipline} students for {mode} in {subject} at {time_slot.strftime('%H:%M')}...")

        # Simulated Partner Matching
        st.markdown("**Suggested Partner**: Ankit Sharma")
        st.markdown("Discipline: Engineering | Subject: Python | Time: 10:30 AM")
        st.button("Connect with Ankit")

    st.markdown("---")
    st.subheader("📅 Mark Today’s Session")
    if st.button("✅ I Studied with My Partner Today"):
        st.success("Logged your study session successfully!")
        feedback = st.text_area("📝 Feedback (Optional): How was your session?")
        if st.button("Submit Feedback"):
            st.success("Thanks! Your feedback helps us improve partner matching.")

    st.markdown("---")
    st.subheader("🎯 Suggest Your Ideal Partner/Group")
    suggestion = st.text_area("Tell us what kind of partner or group you'd like to study with.")
    if st.button("Submit Suggestion"):
        st.success("Your suggestion has been submitted. We'll match you better next time!")

# -------------------- Subscription --------------------
elif choice == "Subscription":
    st.header("💼 Upgrade to Premium Plan")
    plan = st.selectbox("Choose Plan", ["Free - 1 Year", "Premium - ₹999/year"])
    uploaded_id = st.file_uploader("Upload Valid Student ID for Verification")

    if plan == "Premium - ₹999/year":
        st.markdown("### 🔥 Premium Benefits")
        st.markdown("- Teacher Assistance 👩‍🏫")
        st.markdown("- Verified Partner Matching ✅")
        st.markdown("- Job / Placement Support 💼")
        st.markdown("- Discounts Based on College 🎓")
        if uploaded_id:
            st.success("ID Verified. Payment pending.")
        st.button("Proceed to Payment")

# -------------------- College Onboarding --------------------
elif choice == "College Onboarding":
    st.header("🏫 Register Your College")
    cname = st.text_input("College Name")
    cemail = st.text_input("College Contact Email")
    discount = st.slider("Set Student Discount (%)", 0, 50, 10)
    doc = st.file_uploader("Upload College Affiliation Proof")

    if st.button("Submit College Request"):
        if cname and doc:
            st.success(f"{cname} submitted for onboarding. We will verify soon.")
        else:
            st.warning("⚠️ Please upload document and fill all required fields.")

# -------------------- Footer --------------------
st.markdown("---")
st.caption("🔒 Your data is secure with StudySync. | © 2025 StudySync")

