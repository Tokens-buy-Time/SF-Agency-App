import streamlit as st
# Function to set the page configuration
def configure_page():
    st.set_page_config(
        page_title="Virtual Aerospace Agency",
        page_icon="✈️",
        layout="wide"
    )

# Function to add CSS for custom styling
def add_custom_styles():
    st.markdown(
        """
        <style>
        .main { background-color: #f0f0f0; }
        h1 { color: #1f4e79; }
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to create sidebar navigation
def create_sidebar():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Welcome", "Mission Planner", "Settings"])
    return page

# Function for welcome page
def show_welcome():
    st.title("Welcome to the Virtual Aerospace Agency")
    st.write("Explore aerospace missions and manage settings from the sidebar.")

# Function for mission planner
def mission_planner():
    st.header("Mission Planner")
    st.write("Plan and simulate aerospace missions.")
    
    mission_name = st.text_input("Mission Name")
    mission_type = st.selectbox("Mission Type", ["Reconnaissance", "Exploration", "Research", "Defense"])
    launch_date = st.date_input("Launch Date")
    
    if st.button("Start Mission"):
        st.success(f"Mission '{mission_name}' of type '{mission_type}' scheduled for {launch_date}!")

# Function for settings page
def settings():
    st.header("Settings")
    st.write("Adjust app settings here.")
    
    dark_mode = st.checkbox("Dark Mode")
    
    if dark_mode:
        st.write("Dark Mode is enabled!")
    else:
        st.write("Dark Mode is disabled.")

# Main function to control app flow
def main():
    configure_page()
    add_custom_styles()
    
    page = create_sidebar()
    
    if page == "Welcome":
        show_welcome()
    elif page == "Mission Planner":
        mission_planner()
    elif page == "Settings":
        settings()

if __name__ == "__main__":
    main()
