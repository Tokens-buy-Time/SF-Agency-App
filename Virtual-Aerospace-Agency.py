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
        if mission_name and launch_date:
            st.success(f"Mission '{mission_name}' of type '{mission_type}' scheduled for {launch_date} at {mission_location} with objectives: {mission_objectives}.")
        else:
            st.error("Please fill in all required fields (Mission Name and Launch Date).")

# Settings Page
elif page == "Settings":
    st.title("Settings")
    dark_mode = st.checkbox("Enable Dark Mode")
    
    notifications = st.checkbox("Enable Notifications")
    user_profile = st.text_input("User Profile Name")
    
    if dark_mode:
        st.write("Dark Mode is enabled.")
    else:
        st.write("Dark Mode is disabled.")
    
    if notifications:
        st.write("Notifications are enabled.")
    else:
        st.write("Notifications are disabled.")
    
    st.write(f"Profile: {user_profile}")
