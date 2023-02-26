import streamlit as st
import core
import os

class Main:

    def __init__(self):
        self.photo_upload = None
        self.style_upload = None
        self.epoch = 200
        self.params = []

    def main_parameters_return(self):

        photo_file_path = os.path.join(os.path.dirname(__file__), self.photo_upload.name)
        style_file_path = os.path.join(os.path.dirname(__file__), self.style_upload.name)

        self.params.append(photo_file_path)
        self.params.append(style_file_path)
        self.params.append(self.epoch)
        #st.write(self.params[0])

        return self.params

    def call_core(self):

        p = self.main_parameters_return()
        c = core.Core(p[0], p[1], p[2])
        c.image_style_processing()

    def main_display(self):

        st.title("StyleGen")
        st.subheader("Image Style Transfer using VGG - 19")
        self.photo_upload = st.file_uploader(label="Photo Upload", type=['jpeg','jpg','png'], accept_multiple_files=False,
                                             key="photo_upload")
        self.style_upload = st.file_uploader(label="Style Upload", type=['jpeg','jpg','png'], accept_multiple_files=False,
                                             key="style_upload")
        self.epoch = st.slider(label="Number of Epoches", min_value=200, max_value=4000,step=100, format="%d",
                                     key="epoch")



        if st.button("SUBMIT"):
            try:
                if self.photo_upload is None or self.style_upload is None:
                    st.error("Please upload both photo and style files.")
                else:
                    # Check if the file format is jpg
                    if self.photo_upload.type == "image/jpeg" or self.photo_upload.type == "image/jpg" or self.photo_upload.type == "image/png" \
                            and self.style_upload.type == "image/jpeg" or self.style_upload.type == "image/jpg" or self.style_upload.type == "image/png":
                        #st.success("File format is correct!")
                        # Your code for Image Style Transfer using VGG - 19
                        self.call_core()

                    else:
                        st.error("Please upload files in JPEG/JPG/PNG format.")
            except Exception as e:
                st.error("Please upload files in JPEG/JPG/PNG format.")
                st.write(e)








