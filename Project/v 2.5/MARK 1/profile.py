import streamlit as st
import datetime

# Define avatar options
avatars = {
    "🐶 Dog": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/285/dog-face_1f436.png",
    "🐱 Cat": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/285/cat-face_1f431.png",
    "🐻 Bear": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/285/bear-face_1f43b.png",
    "🐵 Monkey": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/285/monkey-face_1f435.png",
    "🐘 Elephant": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/285/elephant_1f418.png",
    "🐬 Dolphin": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/285/dolphin_1f42c.png",
    "🦁 Lion": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/285/lion-face_1f981.png",
    "🦊 Fox": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/285/fox-face_1f98a.png",
    "🐰 Rabbit": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/285/rabbit-face_1f430.png",
    "🐻 Panda": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/285/panda-face_1f43c.png"
}
# Define password recovery questions
questions = [
    "What is your favorite color?",
    "What is the name of your first pet?",
    "What is your mother's maiden name?",
    "What is the name of your favorite teacher?",
    "What is your favorite book?"
]

# Define registration form fields
st.header("User Registration")
name = st.text_input("Name")
email = st.text_input("Email")
min_date = datetime.datetime.strptime('1939-01-01', '%Y-%m-%d').date()
dob = st.date_input("Date of Birth",min_value=min_date)
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

# Divide avatar options into multiple lists
avatar_lists = [list(avatars.items())[i:i+3] for i in range(0, len(avatars), 3)]

# Display avatar options in separate columns
try:
    st.subheader("Select your avatar")
    cols = st.columns(4)

    for i, col in enumerate(cols):
        for key, value in avatar_lists[i]:
            if col.button(key):
                selected_avatar = value
            #col.image(value, use_column_width=True)
except:
    pass


selected_question = st.selectbox("Select a password recovery question", questions)
answer = st.text_input("Answer to password recovery question")

# Validate form submission
if st.button("Submit"):
    if not name:
        st.warning("Please enter your name.")
    elif not email:
        st.warning("Please enter your email.")
    elif not dob:
        st.warning("Please enter your date of birth.")
    elif not password:
        st.warning("Please enter your password.")
    elif password != confirm_password:
        st.warning("Passwords do not match.")
    elif not answer:
        st.warning("Please enter an answer to the password recovery question.")
    else:
        # Save user data and password recovery question/answer to database or do other processing
        st.success("Registration successful!")
