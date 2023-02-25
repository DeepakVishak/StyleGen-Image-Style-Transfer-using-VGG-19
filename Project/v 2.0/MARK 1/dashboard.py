import streamlit as st
import requests
from io import BytesIO
from PIL import Image

# Define the user's name and avatar image URL
user_name = "John Smith"
avatar_url = "https://avatars.githubusercontent.com/u/71172436?s=400&u=d775a3e3bc8aaae9d08cc1e856c86e0498b2f6a5&v=4"

# Define the images you want to display
image_urls = ["https://avatars.githubusercontent.com/u/71172436?s=400&u=d775a3e3bc8aaae9d08cc1e856c86e0498b2f6a5&v=4",
              "https://avatars.githubusercontent.com/u/71172436?s=400&u=d775a3e3bc8aaae9d08cc1e856c86e0498b2f6a5&v=4",
              "https://avatars.githubusercontent.com/u/71172436?s=400&u=d775a3e3bc8aaae9d08cc1e856c86e0498b2f6a5&v=4",
              "https://avatars.githubusercontent.com/u/71172436?s=400&u=d775a3e3bc8aaae9d08cc1e856c86e0498b2f6a5&v=4",
              "https://avatars.githubusercontent.com/u/71172436?s=400&u=d775a3e3bc8aaae9d08cc1e856c86e0498b2f6a5&v=4"]

# Load the avatar image using PIL and resize it
response = requests.get(avatar_url)
avatar_image = Image.open(BytesIO(response.content))
avatar_image = avatar_image.resize((100, 100))

# Set the page title and icon
st.set_page_config(page_title="Image Grid Dashboard", page_icon=avatar_image)

# Display the user's name and avatar
st.image(avatar_image, width=100)
st.write(user_name)

# Create a grid to display the images
col1, col2, col3 = st.columns(3)

# Display each image in the grid
for i, image_url in enumerate(image_urls):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    image = image.resize((200, 200))
    if i % 3 == 0:
        col1.image(image)
    elif i % 3 == 1:
        col2.image(image)
    else:
        col3.image(image)
