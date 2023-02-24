import streamlit as st

# Define your pages as functions
def page_home():
    st.write("Welcome to the home page")
    if st.button("Go to About page"):
        st.session_state.current_page = "about"

def page_about():
    st.write("This is the about page")
    if st.button("Go to Home page"):
        st.session_state.current_page = "home"

# Initialize the session state
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# Display the current page
if st.session_state.current_page == "home":
    page_home()
elif st.session_state.current_page == "about":
    page_about()
