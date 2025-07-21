pip install streamlit streamlit-option-menu pandas Pillow
streamlit run study_sync_app.py
import streamlit as st
from PIL import Image
import pandas as pd
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
st.set_page_config(page_title="StudySync - Student Study Partner App", layout="centered")

# -------------------- Sidebar Menu --------------------
menu = ["Home", "Register", "Login", "Find Study Partner", "Subscription", "College Onboarding"]
choice = st.sidebar.selectbox("Menu", menu)

# -------------------- Home --------------------
if choice == "Home":
    st.title("🎓 StudySync - Connect. Study. Succeed.")
    st.subheader("Your Global Study Partner Matchmaking App")
    st.markdown("Designed for students who struggle to find motivated study buddies.")
    st.image("https://cdn.pixabay.com/photo/2020/03/31/16/16/online-4983591_1280.jpg", use_column_width=True)
    st.info("💡 Free for 1 year • Premium includes teacher assistance, placement support & more!")

# -------------------- Registration --------------------
elif choice == "Register":
    st.header("🔐 Student Registration")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    college = st.selectbox("Select Your College", list(colleges.keys()))
    id_card = st.file_uploader("Upload Student ID (JPEG/PNG/PDF)")
    education = st.selectbox("Current Education Level", ["UG", "PG", "PhD", "Others"])
    password = st.text_input("Create Password", type='password')
    register_btn = st.button("Register")

    if register_btn:
        if name and email and id_card:
            st.success(f"🎉 Welcome {name}! You have successfully registered.")
        else:
            st.warning("Please fill all required fields!")

# -------------------- Login --------------------
elif choice == "Login":
    st.header("🔑 Login to StudySync")
    email = st.text_input("Email")
    password = st.text_input("Password", type='password')
    login_btn = st.button("Login")

    if login_btn:
        st.success(f"Welcome back! Explore your study groups now.")

# -------------------- Find Study Partner --------------------
elif choice == "Find Study Partner":
    st.header("👥 Match With Study Partner or Join Group")
    subject = st.selectbox("Preferred Subject", ["Math", "AI/ML", "Finance", "Python", "Marketing", "Other"])
    time_slot = st.time_input("Preferred Study Time")
    mode = st.radio("Study Mode", ["1-on-1 Partner", "Group Study"])
    search_btn = st.button("Search Partner/Group")

    if search_btn:
        st.success(f"🔍 Found suitable {mode} options for {subject} at {time_slot.strftime('%H:%M')}!")

# -------------------- Subscription --------------------
elif choice == "Subscription":
    st.header("💼 Upgrade to Premium Plan")
    plan = st.selectbox("Choose Plan", ["Free - 1 Year", "Premium - ₹999/year"])
    uploaded_id = st.file_uploader("Upload Valid Student ID for Verification")
    
    if plan == "Premium - ₹999/year":
        st.markdown("**Benefits:**")
        st.markdown("- ✅ Teacher Assistance")
        st.markdown("- 🎯 Placement Support")
        st.markdown("- 🧑‍🤝‍🧑 Verified Study Partners")
        st.markdown("- 💸 Discount Based on College")
        if uploaded_id:
            st.success("ID Verified. Payment pending.")
        st.button("Proceed to Payment")

# -------------------- College Onboarding --------------------
elif choice == "College Onboarding":
    st.header("🏛️ Register Your College on StudySync")
    cname = st.text_input("College Name")
    cemail = st.text_input("College Email")
    discount = st.slider("Set Student Discount (%)", 0, 50, 10)
    doc = st.file_uploader("Upload College Affiliation Document")

    if st.button("Submit Request"):
        if cname and doc:
            st.success(f"{cname} is successfully submitted for review.")
        else:
            st.warning("Please upload all documents and fill details.")

# -------------------- Footer --------------------
st.markdown("---")
st.caption("🔒 Your data is secure. StudySync © 2025")
elif choice == "Find Study Partner":
    st.header("👥 Match With Study Partner or Join Group")
    discipline = st.selectbox("Discipline", ["Engineering", "Science", "Arts", "Commerce", "Law", "Medical", "Other"])
    subject = st.selectbox("Preferred Subject", ["Math", "AI/ML", "Finance", "Python", "Marketing", "Other"])
    time_slot = st.time_input("Preferred Study Time")
    mode = st.radio("Study Mode", ["1-on-1 Partner", "Group Study"])
    ready_status = st.checkbox("✅ Ready to Study Now")

    if ready_status:
        st.success("You're now visible to others as 'Ready to Study'!")

    search_btn = st.button("Search Partner/Group")

    if search_btn:
        st.success(f"🔍 Matching {discipline} students for {mode} sessions at {time_slot.strftime('%H:%M')}.")

    # Simulated Partner Matching Display
    st.subheader("🔗 Suggested Study Partner:")
    st.markdown("**Name**: Ankit Sharma\n**Discipline**: Engineering\n**Subject**: Python\n**Time**: 10:30 AM")
    st.button("Connect with Ankit")

    # Log Study Session
    st.markdown("---")
    st.subheader("📅 Mark Today’s Session")
    studied_today = st.button("✅ I Studied with My Partner Today")

    if studied_today:
        st.success("Nice! Your study session is logged.")
        st.markdown("📝 **Feedback (Optional):**")
        feedback = st.text_area("How was your session today?")
        st.button("Submit Feedback")
    # Suggest Other Partners
    st.markdown("---")
    st.subheader("🎯 Suggest Improvements or Partners")
    suggest_text = st.text_area("What kind of partner or study group would you prefer in the future?")
    if st.button("Submit Suggestion"):
        st.success("Thanks for your suggestion! Our AI will use it to recommend better partners.")
