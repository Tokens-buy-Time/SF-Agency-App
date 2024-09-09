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
    launch_date = st.date_input("Launch Date")
    
    if st.button("Start Mission"):
        st.success(f"Mission '{mission_name}' of type '{mission_type}' scheduled for {launch_date}!")

# Settings Page
elif page == "Settings":
    st.title("Settings")
    dark_mode = st.checkbox("Enable Dark Mode")
    
    if dark_mode:
        st.write("Dark Mode is enabled.")
    else:
        st.write("Dark Mode is disabled.")
