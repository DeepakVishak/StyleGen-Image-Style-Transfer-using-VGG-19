import streamlit as st
from streamlit_lottie import st_lottie
import json
from PIL import Image

class json_file:

    def __init__(self):
        pass

    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)


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

