import streamlit as st
from streamlit_lottie import st_lottie
import json
from PIL import Image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class json_file:

    def __init__(self):
        pass

    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)


class Home(json_file):

    def __init__(self):
        pass

    def home_display(self):
        #st.set_page_config(layout="wide")
        left, right = st.columns(2)
        with left:
            st.markdown("""
    # StyleGen
    ## Image Style Transfer Using VGG-19 
    ### _Transform ordinary photos into extraordinary works of art._
            """)

        with right:
            file = json_file.load_lottiefile("f1.json")
            print(file)

            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality="high",  # medium ; high
                height=500,
                width=None,
                key=None,
            )

        st.write(
        """<style>
        [data-testid="stHorizontalBlock"] {
            align-items: center;
        }
        </style>
        """,
        unsafe_allow_html=True
        )



class WhatWeDo(json_file):

    def __init__(self):
        self.image = Image.open("image03.png")

    def whatwedo_display(self):
        #st.set_page_config(layout="wide")
        st.write("""""")
        st.write("""""")
        st.write("""""")
        st.write("""""")
        st.write("""""")
        st.title("What We Do!!!")
        left, right = st.columns(2)
        with right:
            resized_image = self.image.resize((1000, 500))
            st.image(resized_image)

        with left:
            file = json_file.load_lottiefile("f2.json")
            print(file)

            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality="high",  # medium ; high
                height=500,
                width=None,
                key=None,
            )

        st.write(
        """<style>
        [data-testid="stHorizontalBlock"] {
            align-items: center;
        }
        </style>
        """,
        unsafe_allow_html=True
        )

class HowToUse:

    def __init__(self):
        pass

    def howtouse_display(self):

        # step 1
        #st.set_page_config(layout="wide")
        st.write("""""")
        st.write("""""")
        st.write("""""")
        st.title("How to Use StyleGen")
        st.subheader("Follow these simple steps to generate stylish images:")

        # step 2
        col1, col2 = st.columns(2)
        col1.markdown("1. Click the **Multipage Options** menu on the top left corner of the app.")
        col2.image("image03.png", width=500)

        # step 3
        col1, col2 = st.columns(2)
        col1.markdown("2. Select the **Try StyleGen** option from the dropdown menu.")
        col2.image("image03.png", width=500)

        # step 4
        col1, col2 = st.columns(2)
        col1.markdown("3. Upload your content image and style image in JPG/PNG/JPEG format.")
        col2.image("image03.png", width=500)

        # step 5
        col1, col2 = st.columns(2)
        col1.markdown("4. Choose the number of epochs to scale the model. More epochs mean better results but longer processing time.")
        col2.image("image03.png", width=500)

        # step 6
        col1, col2 = st.columns(2)
        col1.markdown("5. The inputs are fed into the VGG-19 model for processing. This may take some time, so please be patient.")
        col2.image("image03.png", width=500)

        # step 7
        col1, col2 = st.columns(2)
        col1.markdown("6. Once the processing is complete, the output image will be displayed on the app. You can download it using the **Download** button below.")
        col2.image("image03.png", width=500)


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

