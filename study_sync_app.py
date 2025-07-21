import streamlit as st
from PIL import Image
from datetime import datetime
import pytz

# App config
st.set_page_config(page_title="Study Sync", page_icon="📚", layout="wide")

# Custom CSS for pastel theme
st.markdown("""
    <style>
        body {
            background-color: #fefaff;
        }
        .title-text {
            color: #7b4397;
            font-size: 40px;
            font-weight: bold;
        }
        .motivation {
            font-size: 18px;
            color: #ff5f6d;
        }
        .section-header {
            font-size: 22px;
            color: #6a11cb;
            font-weight: 600;
        }
        .stButton>button {
            background-color: #f093fb;
            color: white;
            font-weight: bold;
            border-radius: 12px;
        }
    </style>
""", unsafe_allow_html=True)

# Load images
trophy_img = Image.open("assets/trophy.png")
banner_img = Image.open("assets/study_banner.jpg")

# Splash and introduction screens
with st.container():
    st.image(banner_img, use_container_width=True)
    st.markdown('<div class="title-text">Welcome to Study Sync 📚</div>', unsafe_allow_html=True)
    st.markdown('<div class="motivation">Your partner in collaborative and fun studying!</div>', unsafe_allow_html=True)
    st.markdown("---")

# Main form
st.markdown('<div class="section-header">🔐 Register to Find a Study Partner</div>', unsafe_allow_html=True)

with st.form("registration_form", clear_on_submit=False):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 Your Name")
        gender = st.selectbox("🚻 Gender", ["Prefer not to say", "Female", "Male", "Non-binary"])
        language = st.selectbox("🗣 Preferred Language", ["English", "Hindi", "Spanish", "French", "Mandarin", "Other"])
        level = st.selectbox("🎓 Your Knowledge Level", ["Basic", "Intermediate", "Advanced"])
        goal = st.selectbox("🎯 Goal", ["Quick Revision", "In-depth Study", "Competitive Exam Prep"])
    with col2:
        subjects = st.multiselect("📘 Subjects You Want to Study", ["Math", "Science", "History", "Accounts", "Economics", "Coding", "Marketing"])
        timezone = st.selectbox("🌐 Select Your TimeZone", pytz.all_timezones)
        duration = st.slider("⏱ Preferred Study Duration (in hours)", 1, 6, 2)
        visibility = st.radio("🎥 Visibility Preference", ["Audio Only", "Video Allowed", "Share Recorded Clips", "No Sharing"])

    college = st.selectbox("🏫 Your College or Exam", [
        "Delhi University", "IIT Delhi", "Jamia Millia", "AIIMS Delhi", 
        "Harvard", "MIT", "Oxford", "University of Toronto", "Other"
    ])

    submit_btn = st.form_submit_button("🔍 Find Study Partner")

    if submit_btn:
        st.success(f"✨ Hey {name}, you're all set!")
        st.markdown(f"""
        - 🌍 **TimeZone:** {timezone}  
        - 📚 **Subjects:** {', '.join(subjects)}  
        - 🧑‍🤝‍🧑 Gender preference: **{gender}**  
        - 🌐 Language: **{language}**  
        - 🎓 Level: **{level}**  
        - 🎯 Goal: **{goal}**  
        - ⏱ Duration: **{duration} hour(s)**  
        - 🔐 College/Exam: **{college}**  
        - 🎥 Visibility: **{visibility}**  
        """)
        st.balloons()
        st.image(trophy_img, caption="You just earned 100 points 🏆", use_column_width=True)
        st.markdown("<div class='motivation'>Well done! You've just started your study journey! Enjoy studying with your partner. 🚀</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<div style='text-align:center'>Use your mind. Stay curious. Keep going! 🌟</div>", unsafe_allow_html=True)
