import streamlit as st

class Home:

    def __init__(self):
        self.photo_upload = None
        self.style_upload = None
        self.epoch = 200
        self.params = []

    def home_parameters_return(self):

        self.params.append(self.photo_upload)
        self.params.append(self.style_upload)
        self.params.append(self.epoch)
        st.write(self.params)

        return self.params

    def home_display(self):
        st.title("Image Style Transfer using VGG - 19")
        self.photo_upload = st.file_uploader(label="Photo Upload", type=['jpeg'], accept_multiple_files=False,
                                             key="photo_upload")
        self.style_upload = st.file_uploader(label="Style Upload", type=['jpeg'], accept_multiple_files=False,
                                             key="style_upload")
        self.epoch = st.slider(label="Number of Epoches", min_value=200, max_value=4000,step=100, format="%d",
                                     key="epoch")

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("SUBMIT"):
                try:
                    if self.photo_upload is None or self.style_upload is None:
                        st.error("Please upload both photo and style files.")
                    else:
                        # Check if the file format is jpg
                        if self.photo_upload.type == "image/jpeg" and self.style_upload.type == "image/jpeg":
                            st.success("File format is correct!")
                            self.home_parameters_return()
                            # Your code for Image Style Transfer using VGG - 19
                        else:
                            st.error("Please upload files in JPEG format.")
                except Exception as e:
                    st.error("Please upload files in JPEG format.")
                    #st.write(e)



        with col3:
            st.button("DOWNLOAD LAST RESULT")




h = Home()
h.home_display()

