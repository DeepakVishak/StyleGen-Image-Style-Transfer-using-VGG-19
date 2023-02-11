import streamlit as st
from PIL import Image

st.title("Streamlit Example")

st.write("This is a simple Streamlit app.")

image = Image.open("image.jpg")
st.image(image, caption='Image', use_column_width=True)
