import streamlit as st
from streamlit_lottie import st_lottie
import json
from PIL import Image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64

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
    # 🖌️ StyleGen
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
        st.title("🦄 What We Do!!!")
        left, right = st.columns(2)
        with right:
            resized_image = self.image.resize((800, 500))
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
        st.markdown(
            "<p style='text-align: center; font-size: 15pt; font-style: italic;'>\"StyleGen is an appliction in which you can apply the style of one image to another image while preserving its content.\"</p>",
            unsafe_allow_html=True)

        #st.markdown("<p style=\"text-align: center; font-size: 15pt; font-style: italic;\">Image style transfer is the process of applying the style of one image to another image while preserving its content.</p>", unsafe_allow_html=True)


class HowToUse:

    def __init__(self):
        pass

    def howtouse_display(self):

        # step 1
        #st.set_page_config(layout="wide")
        st.write("""""")
        st.write("""""")
        st.write("""""")
        st.title("💡 How to Use StyleGen")
        st.subheader("Follow these simple steps to generate stylish images:")

        # step 2

        st.markdown("1. Click the **Multipage Options** menu on the top left corner of the app.")
        st.image("1.png", width=1000)

        # step 3

        st.markdown("2. Select the **Try StyleGen** option from the dropdown menu.")
        st.image("2.png", width=1000)

        # step 4

        st.markdown("3. Upload your content image and style image in JPG/PNG/JPEG format.")
        st.image("3.png", width=1000)

        # step 5

        st.markdown("4. Choose the number of epochs to scale the model. More epochs mean better results but longer processing time.")
        st.image("4.png", width=1000)

        # step 6

        st.markdown("5. The inputs are fed into the VGG-19 model for processing. This may take some time, so please be patient.")
        st.image("5.png", width=1000)

        # step 7

        st.markdown("6. Once the processing is complete, the output image will be displayed on the app. You can download it using the **Download** button below.")
        st.image("6.png", width=1000)


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
        st.title("📝 Contact Us")

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

class Footer:

    def __init__(self):
        pass

    def footer_display(self):

        # Read the icon image file
        with open("github.png", "rb") as f1:
            img_bytes_f1 = f1.read()
            data_url_f1 = base64.b64encode(img_bytes_f1).decode("utf-8")

        with open("linkedin.png", "rb") as f2:
            img_bytes_f2 = f2.read()
            data_url_f2 = base64.b64encode(img_bytes_f2).decode("utf-8")

        with open("web.png", "rb") as f3:
            img_bytes_f3 = f3.read()
            data_url_f3 = base64.b64encode(img_bytes_f3).decode("utf-8")

        # Define the HTML and CSS for the footer
        footer_html = f"""
        <style>
        .footer {{
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin-top: 30px;
            padding: 20px;
            color: #6C757D;
            font-size: 14px;
            font-weight: 500;
            text-align: center;
        }}

        .footer a {{
            color: #6C757D;
            text-decoration: none;
            margin-left: 20px;
            margin-right: 20px;
        }}

        .footer a:hover {{
            color: #0366d6;
        }}

        .footer .icon-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            grid-gap: 20px;
        }}

        .footer .icon {{
            height: 48px;
            width: 48px;
        }}

        .footer p {{
            margin-top: 20px;
        }}
        </style>
        <div class="footer">
            <div class="icon-grid">
                <a href="https://github.com/DeepakVishak"><img src="data:image/png;base64,{data_url_f1}" class="icon" alt="github"></a>
                <a href="https://www.linkedin.com/in/deepak-vishak-0417b9201/"><img src="data:image/png;base64,{data_url_f2}" class="icon" alt="linkedin"></a>
                <a href="https://deepakvishak.github.io/"><img src="data:image/png;base64,{data_url_f3}" class="icon" alt="web"></a>
            </div>
            <p>&copy; 2023 All Rights Reserved</p>
        </div>
        """

        # Add the footer to the app

        st.markdown(footer_html, unsafe_allow_html=True)





