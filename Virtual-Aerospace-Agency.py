import streamlit as st

# Basic Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Mission Planner", "Settings"])

# Home Page
if page == "Home":
    st.title("Welcome to the Virtual Aerospace Agency")
    st.write("This is the home page.")

# Mission Planner Page
elif page == "Mission Planner":
    st.title("Mission Planner")
    st.write("Plan your aerospace missions here.")
    
    mission_name = st.text_input("Mission Name")
    mission_type = st.selectbox("Mission Type", ["Reconnaissance", "Exploration", "Research", "Defense"])
    mission_objectives = st.text_area("Mission Objectives")
    mission_location = st.text_input("Mission Location")
    team_members = st.text_input("Team Members")
    launch_date = st.date_input("Launch Date")
    
    if st.button("Start Mission"):
​⬤
