import streamlit as st


class HowToUse:

    def __init__(self):
        pass

    def howtouse_display(self):

        # step 1
        #st.set_page_config(layout="wide")
        st.write("""""")
        st.write("""""")
        st.write("""""")
        st.title("How to Use StyleGen")
        st.subheader("Follow these simple image03s to generate stylish images:")

        # step 2
        col1, col2 = st.columns(2)
        col1.markdown("1. Click the **Multipage Options** menu on the top left corner of the app.")
        col2.image("image03.png", width=500)

        # step 3
        col1, col2 = st.columns(2)
        col1.markdown("2. Select the **Try StyleGen** option from the dropdown menu.")
        col2.image("image03.png", width=500)

        # step 4
        col1, col2 = st.columns(2)
        col1.markdown("3. Upload your content image and style image in JPG/PNG/JPEG format.")
        col2.image("image03.png", width=500)

        # step 5
        col1, col2 = st.columns(2)
        col1.markdown("4. Choose the number of epochs to scale the model. More epochs mean better results but longer processing time.")
        col2.image("image03.png", width=500)

        # step 6
        col1, col2 = st.columns(2)
        col1.markdown("5. The inputs are fed into the VGG-19 model for processing. This may take some time, so please be patient.")
        col2.image("image03.png", width=500)

        # step 7
        col1, col2 = st.columns(2)
        col1.markdown("6. Once the processing is complete, the output image will be displayed on the app. You can download it using the **Download** button below.")
        col2.image("image03.png", width=500)


