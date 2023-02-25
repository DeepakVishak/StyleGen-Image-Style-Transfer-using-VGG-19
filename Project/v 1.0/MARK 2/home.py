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

        st.title("StyleGen")
        st.subheader("Image Style Transfer using VGG - 19")
        self.photo_upload = st.file_uploader(label="Photo Upload", type=['jpeg','jpg','png'], accept_multiple_files=False,
                                             key="photo_upload")
        self.style_upload = st.file_uploader(label="Style Upload", type=['jpeg','jpg','png'], accept_multiple_files=False,
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
                        if self.photo_upload.type == "image/jpeg" or self.photo_upload.type == "image/jpg" or self.photo_upload.type == "image/png" \
                                and self.style_upload.type == "image/jpeg" or self.style_upload.type == "image/jpg" or self.style_upload.type == "image/png":
                            st.success("File format is correct!")
                            #self.home_parameters_return()
                            # Your code for Image Style Transfer using VGG - 19
                        else:
                            st.error("Please upload files in JPEG/JPG/PNG format.")
                except Exception as e:
                    st.error("Please upload files in JPEG/JPG/PNG format.")
                    #st.write(e)



h = Home()
h.home_display()

