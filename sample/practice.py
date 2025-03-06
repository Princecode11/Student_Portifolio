import streamlit as st
import time

# Set page configuration
st.set_page_config(page_title="My Digital Footprint", page_icon="🎓", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go To:", ["Home", "Projects", "Skills & Achievements", "Customize Profile","Testimonials", "Timeline", "Contact"])

# Home Section
if page == "Home":
    st.title("🎓 My Digital Footprint – Showcasing My Journey")

    uploaded_image = st.file_uploader("Upload Profile Picture", type=["jpg", "png"])
    if uploaded_image:
        st.image(uploaded_image, width=150, caption="Profile Picture")
    else:
        st.image("sample/Prince.jpg", width=150, caption="Default Profile")

    # Personal Details
    name = st.text_input("Full Name:", "NDUNGUTSE Prince")
    location = st.text_input("Location:", "Musanze, Rwanda")
    university = st.text_input("University:", "INES-Ruhengeri")
    field_of_study = st.text_input("Field of Study:", "BSc Computer Science, Year 3")

    st.write(f"📍 {location}")
    st.write(f"🏛 {university}")
    st.write(f"📚 {field_of_study}")

    # Resume Download
    with open("sample/Prince_Ndungutse_CV.pdf", "rb") as file:
        resume_bytes = file.read()
    st.download_button("📄 Download Resume", data=resume_bytes, file_name="Prince_Ndungutse_CV.pdf", mime="application/pdf")

    # About Me
    st.subheader("About Me")
    about_me = st.text_area("Short introduction:", "I am a passionate technologist!")
    st.write(about_me)

# Projects Section
elif page == "Projects":
    st.title("💻 My Projects")
    category = st.selectbox("Filter by:", ["All", "Year 1 Project", "Group Projects", "Dissertation"])

    projects = [
        {"title": "📊 Timetable", "type": "Year 1 Project",
         "description": "Timetable Generator.",
         "link": "https://github.com/Princecode11/Student_Portifolio/tree/main/sample/Individual"},
        {"title": "🦾 Personal Finance Manager", "type": "Group Projects",
         "description": "Developed a recording system storing students' information.",
         "link": "https://github.com/Princecode11/Student_Portifolio/tree/main/sample/Group"},
        {"title": "🌐 Website Development", "type": "Group Projects",
         "description": "Built a dynamic website.", "link": "https://github.com"},
        {"title": "📕 Final Year Dissertation", "type": "Dissertation",
         "description": "E-Pass System",
         "link": "https://github.com/Princecode11/Student_Portifolio/tree/main/sample/dissertation"}
    ]

    filtered_projects = [project for project in projects if category == "All" or project["type"] == category]

    for project in filtered_projects:
        with st.expander(project["title"]):
            st.write(f"**Project Type:** {project['type']}")
            st.write(project["description"])
            st.write(f"[🔗 GitHub]({project['link']})")

# Skills & Achievements Section
elif page == "Skills & Achievements":
    st.title("⚡ Skills & Achievements")

    st.subheader("Programming Skills")
    skills = {"Python": 90, "JavaScript": 80, "Machine Learning": 70, "Web Development": 85}
    for skill, level in skills.items():
        st.write(f"{skill}: {level}%")
        st.progress(level)

    st.subheader("Certifications & Achievements")
    achievements = [
        "✔ Google Data Analytics Certification",
        "✔ Hackathon Finalist at XYZ University",
        "✔ AI Research & Development Participant"
    ]
    for achievement in achievements:
        st.write(achievement)

# Customize Profile
elif page == "Customize Profile":
    st.title("🎨 Customize Your Profile")
    st.text_input("Edit Name")
    st.text_area("Edit About Me")
    st.file_uploader("Upload New Profile Picture", type=["jpg", "png"])

# Testimonials Section
elif page == "Testimonials":
    st.title("🗣️ Student Testimonials")
    testimonials = [
        "Prince is a dedicated programmer who always delivers high-quality code. – Prof. Kim",
        "Prince is a passionate Student. - Mate. Bruce"
    ]
    for testimonial in testimonials:
        st.write(f"💬 {testimonial}")
    new_testimonial = st.text_area("Leave a Testimonial")
    if st.button("Submit Testimonial"):
        st.success("✅ Testimonial submitted successfully!")

# Timeline Section
elif page == "Timeline":
    st.title("⏳ Timeline of Academic & Project Milestones")
    timeline = [
        "✅ Year 1: First project completed",
        "🏆 Year 2: Hackathon participation",
        "💼 Year 3: Internship experience",
        "📕 Year 4: Dissertation submission"
    ]
    for event in timeline:
        st.write(event)

# Contact Section
elif page == "Contact":
    st.title("📬 Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            with st.spinner("Sending..."):
                time.sleep(2)
                st.success("✅ Message sent successfully!")

    st.write("📧 Email: prince.rwanda11@gmail.com")
    st.write("[📂 GitHub](https://github.com)")



st.sidebar.write("---")
st.sidebar.write("🔹 Made with ❤ using my Head 😁")
