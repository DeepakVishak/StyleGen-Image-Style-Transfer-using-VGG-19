import streamlit as st


def main():
    st.sidebar.title("Multipage Menu")

    # Create a list of options for the top-level menu
    menu_options = ["StyleGen", "Profile"]

    # Add the top-level menu options to the sidebar
    choice = st.sidebar.selectbox("Select an option", menu_options)

    # If the user selects "StyleGen"
    if choice == "StyleGen":
        st.title("StyleGen")
        # Add your StyleGen code here

    # If the user selects "Profile"
    elif choice == "Profile":
        # Create a list of options for the sub-menu
        sub_menu_options = ["Dashboard", "Edit Profile"]
        # Add the sub-menu options to the sidebar
        sub_choice = st.sidebar.selectbox("Select an option", sub_menu_options)

        # If the user selects "Dashboard"
        if sub_choice == "Dashboard":
            st.title("Dashboard")
            # Add your Dashboard code here

        # If the user selects "Edit Profile"
        elif sub_choice == "Edit Profile":
            st.title("Edit Profile")
            # Add your Edit Profile code here

    # Add the "Log Out" button to the bottom of the sidebar
    if st.sidebar.button("Log Out"):
        # Add your logout code here
        st.stop()


if __name__ == "__main__":
    main()
