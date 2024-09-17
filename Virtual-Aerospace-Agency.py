import streamlit as st

st.title("Welcome to the Virtual Aerospace Agency")
#st.image("Virtual-Agency.gif", caption="Virtual Aerospace Agency constitutes instant access to on the fly expertise", use_column_width=True)
st.write(" ")
st.write("Spin up expert, experienced, insightful, IPDT teams, to tackle difficult, short duration - less than 3 month long projects - and disnand them on completion of their assignments.")
st.write(" ")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Job Postings", "Search Jobs", "AI Compliance Assistant", "Markup Calculator", "Settings"])

# Home Page
if page == "Home":
    st.title("Welcome to the Virtual Aerospace Agency")
    st.write("This platform connects aerospace employers with top-tier contractors.")

# Job Postings (Employer)
elif page == "Job Postings":
    st.title("Create a Job Posting")
    
    job_title = st.text_input("Job Title")
    job_description = st.text_area("Job Description")
    job_location = st.text_input("Location")
    job_salary = st.number_input("Salary", min_value=0)
    
    if st.button("Post Job"):
        st.success(f"Job '{job_title}' posted successfully!")
        # In a full app, here you'd save this job posting to a database.

# Search Jobs (Contractor)
elif page == "Search Jobs":
    st.title("Search for Jobs")
    
    # Placeholder jobs for demonstration
    jobs = [
        {"title": "Aerospace Engineer", "location": "USA", "salary": 120000},
        {"title": "Technician", "location": "Canada", "salary": 80000},
    ]
    
    search_query = st.text_input("Search by Job Title")
    
    for job in jobs:
        if search_query.lower() in job["title"].lower():
            st.write(f"**{job['title']}**")
            st.write(f"Location: {job['location']}")
            st.write(f"Salary: ${job['salary']} per year")
            st.button("Apply", key=job["title"])

# AI Compliance Assistant
elif page == "AI Compliance Assistant":
    st.title("AI Compliance Assistant")
    
    country = st.selectbox("Select Country", ["USA", "Canada", "Europe"])
    if country == "USA":
        st.write("USA compliance requirements: ...")
    elif country == "Canada":
        st.write("Canada compliance requirements: ...")
    elif country == "Europe":
        st.write("Europe compliance requirements: ...")

# Markup Calculator
elif page == "Markup Calculator":
    st.title("Markup Rate Calculator")
    
    base_rate = st.number_input("Base Pay Rate", min_value=0.0)
    markup_percentage = st.number_input("Markup Percentage", min_value=0.0)
    
    final_rate = base_rate + (base_rate * (markup_percentage / 100))
    st.write(f"Final Rate: ${final_rate:.2f}")

# Settings Page
elif page == "Settings":
    st.title("Settings")
    dark_mode = st.checkbox("Enable Dark Mode")
    
    if dark_mode:
        st.write("Dark Mode is enabled.")
    else:
        st.write("Dark Mode is disabled.")
