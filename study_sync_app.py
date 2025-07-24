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
            required_fields_filled = all([
                name.strip(), email.strip(),
                final_gender != "Select an option",
                final_university != "Select an option",
                final_course != "Select an option",
                final_timezone != "Select an option",
                final_language != "Select an option",
                uploaded_id
            ])

            if required_fields_filled:
                st.session_state.user_details = {
                    "Name": name,
                    "Email": email,
                    "Gender": final_gender,
                    "University": final_university,
                    "Course": final_course,
                    "Timezone": final_timezone,
                    "Study Goals": study_goal + ([custom_goal] if custom_goal else []),
                    "Language": final_language,
                    "Preferred Mode": mode,
                    "ID File": uploaded_id.name
                }

                st.session_state.registered = True
                st.success(f"🎉 Congratulations **{name}**, you have successfully registered!")
                st.balloons()

                # OPTIONAL: Save to CSV (uncomment if needed)
                # import os
                # user_df = pd.DataFrame([st.session_state.user_details])
                # file_exists = os.path.exists("registered_users.csv")
                # user_df.to_csv("registered_users.csv", mode='a', header=not file_exists, index=False)

                # Redirect to Find a Partner page
                st.session_state.menu = "🤝 Find a Partner"
                st.rerun()

            else:
                st.error("⚠️ Please fill all required fields marked with *.")
