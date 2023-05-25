import streamlit as st
from streamlit_lottie import st_lottie
import json

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
        st.set_page_config(layout="wide")
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


