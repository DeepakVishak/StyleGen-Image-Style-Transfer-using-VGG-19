import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Contact:

    def __init__(self):
        pass


    def contact_display(self):

        # Set page configuration
        """
        st.set_page_config(
            page_title="Contact Us",
            page_icon=":email:"
            #layout="wide"
        )
        """
        # Add header
        st.title("Contact Us")

        # Add contact form
        with st.form("contact_form"):
            st.write("Please fill out the form below and we'll get back to you as soon as possible.")
            st.write("")

            # Add form fields
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Name", max_chars=50)
                email = st.text_input("Email", max_chars=50)
            with col2:
                subject = st.text_input("Subject", max_chars=50)
                message = st.text_area("Message", max_chars=500)

            # Add submit button
            submit_button = st.form_submit_button(label="Submit")

        # Define email sender and receiver
        sender_email = "gamerdexter974@gmail.com"
        receiver_email = "deepakvishak24@gmail.com"

        # Define email message
        email_subject = subject
        email_body = f"Name: {name}\nEmail: {email}\n\n{message}"
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = email_subject
        msg.attach(MIMEText(email_body, "plain"))

        # Send email when form is submitted
        if submit_button and name and email and subject and message:
            try:
                with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                    smtp.starttls()
                    # Replace "your_app_password" with your actual app-specific password
                    smtp.login(sender_email, "lrglxvsyxtrvcmjz")
                    smtp.sendmail(sender_email, receiver_email, msg.as_string())
                    st.success('Your message has been sent!')
            except smtplib.SMTPAuthenticationError as e:
                st.error("There was an error sending your message. Please try again later.")

        # Add footer
        st.write("Thank you for contacting us. We'll be in touch soon!")
