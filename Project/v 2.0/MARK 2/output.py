import streamlit as st
import base64

class Output:

    def __init__(self,img):
        self.image =  img

    def display(self):

        st.balloons()
        st.title("StyleGen")
        st.header("Image Style Transfer using VGG - 19")
        st.subheader("Here is the output!!!")
        #st.image(self.image)

        # Convert image to bytes
        image_bytes = self.image.tobytes()

        # Define function to create a download link
        def get_image_download_link(img_bytes):
            b64 = base64.b64encode(img_bytes).decode()
            href = f'data:application/octet-stream;base64,{b64}'
            return href

        # Show image and download button
        st.image(self.image, caption="Output Image")
        button = st.download_button(
            label="Download image",
            data=get_image_download_link(image_bytes),
            file_name="output_image.jpg",
        )



