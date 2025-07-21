import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# -------------------- Page Config --------------------
st.set_page_config(page_title="StudySync", layout="wide")

# -------------------- App Styling --------------------
st.markdown("""
    <style>
        body {
            background-color: #f0f4f8;
        }
        .main {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .css-1d391kg, .css-18e3th9 {
            background-color: #f0f4f8;
        }
        h1, h3, h4 {
            color: #5f27cd;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------- Sidebar Menu --------------------
with st.sidebar:
    selected = option_menu(
        menu_title="Navigate",
        options=["Dashboard", "Register", "Study Partners", "About"],
        icons=["house", "person-add", "people", "info-circle"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#ffeef2"},
            "icon": {"color": "#5f27cd", "font-size": "18px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "5px",
                "--hover-color": "#f1f3f5"
            },
            "nav-link-selected": {"background-color": "#e8f0ff"},
        }
    )

# -------------------- Dashboard --------------------
if selected == "Dashboard":
    st.markdown("<h1 style='text-align: center;'>🎓 StudySync</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Find Study Buddies, Track Progress & Crush Exams Together!</h3>", unsafe_allow_html=True)

    st.markdown("---")
    st.success("💡 Tip: Stay consistent and track your weekly study goals!")
    st.info("📌 This app helps you find partners based on preferred time, subject, language, goals, and even comfort level.")

# -------------------- Registration Page --------------------
elif selected == "Register":
    st.header("👤 Register to Find Study Buddies")

    with st.form("register_form", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Full Name")
            age = st.number_input("Age", min_value=12, max_value=60)
            gender = st.selectbox("Gender", ["Prefer not to say", "Female", "Male", "Other"])
            language = st.multiselect("Languages You Speak", ["English", "Hindi", "Spanish", "French", "Chinese", "Other"])
            timezone = st.selectbox("Select Your Time Zone", [
                "IST (UTC+5:30)", "EST (UTC-5)", "PST (UTC-8)", "CET (UTC+1)", "GMT (UTC+0)", "JST (UTC+9)"
            ])

        with col2:
            subject = st.text_input("Subject or Topic of Interest")
            knowledge_level = st.radio("Your Knowledge Level", ["Beginner", "Intermediate", "Advanced"])
            goal = st.selectbox("Your Study Goal", [
                "Preparing for competitive exam",
                "Revising for college exam",
                "Quick 1-day crash revision",
                "General learning"
            ])
            duration = st.slider("How many hours do you plan to study daily?", 0.5, 8.0, step=0.5)

        st.markdown("### 🔊 Visibility Preferences")
        video_pref = st.checkbox("Allow video-based study")
        audio_pref = st.checkbox("Allow voice/audio interaction")
        upload_recordings = st.file_uploader("Upload Sample Study Recording (optional)", type=["mp3", "mp4", "wav", "mov"])

        submitted = st.form_submit_button("📥 Submit")
        if submitted:
            st.success("🎉 Registration complete! We'll match you with a compatible study buddy soon.")

# -------------------- Study Partner List (Mock UI) --------------------
elif selected == "Study Partners":
    st.header("📚 Suggested Study Buddies")
    sample_data = {
        "Name": ["Aman Sharma", "Lina Zhang", "Carlos Perez", "Fatima Noor"],
        "Subject": ["Maths", "Data Science", "French Grammar", "History"],
        "Level": ["Intermediate", "Advanced", "Beginner", "Intermediate"],
        "Time Zone": ["IST", "JST", "CET", "GMT"],
        "Language": ["English, Hindi", "Chinese", "Spanish", "English, Arabic"]
    }
    df = pd.DataFrame(sample_data)
    st.table(df)

# -------------------- About --------------------
elif selected == "About":
    st.subheader("📌 About StudySync")
    st.write("""
    StudySync is a collaborative study app built for learners across the globe to connect based on comfort, subject expertise, language, and time preference.

    **Features:**
    - Match with partners based on gender, time zone, goals & subject
    - Choose between video/audio/text study sessions
    - Upload recordings and track goals
    - Clean UI inspired by real learning apps like WiFiStudy

    🛠 Built with Python, Streamlit & ❤️ for learners everywhere!
    """)

