import streamlit as st

# Title of the App
st.title("Virtual Aerospace Agency")

# Introduction
st.write("""
Welcome to the Virtual Aerospace Agency App! This tool is designed to help users explore various aerospace projects, 
access key information, and perform relevant calculations related to aerospace missions.
""")

# Basic Form Example: Gathering Mission Data
st.header("Mission Data Input")
with st.form(key='mission_data_form'):
    mission_name = st.text_input("Mission Name")
    launch_date = st.date_input("Launch Date")
    mission_objective = st.text_area("Mission Objective")
    
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.write(f"Mission Name: {mission_name}")
    st.write(f"Launch Date: {launch_date}")
    st.write(f"Mission Objective: {mission_objective}")
    st.success("Mission Data Submitted Successfully!")

# Placeholder for additional features
st.header("More Features Coming Soon!")
st.write("Stay tuned as we continue to develop this app with more aerospace-related tools and resources.")
