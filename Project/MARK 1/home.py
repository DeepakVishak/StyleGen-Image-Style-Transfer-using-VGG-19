import streamlit as st

class Home:

    def __init__(self):
        pass

    def display(self):
        st.title("Image Style Transfer using VGG - 19")
        st.file_uploader(label="Photo Upload")
        st.file_uploader(label="Artistic Upload")
        st.text_input(label="Number of Epoches")
        st.button(label="SUBMIT")

h = Home()
h.display()
