import streamlit as st
import pandas as pd # pip install pandas
from matplotlib import pyplot as plt # pip install matplotlib
import time

plt.style.use("ggplot")

data = {
    "num":[x for x in range(1,11)],
    "square":[x**2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice":[x*3 for x in range(1,11)]
}
rad = st.sidebar.radio("Navigation",["home","about"])

if rad == "home":
    df = pd.DataFrame(data = data)

    col = st.sidebar.multiselect("Select a Column",df.columns)

    plt.plot(df['num'],df[col])
    st.pyplot()

if rad == "about":

    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)

    st.balloons()

    st.write("This is about page")
    st.info("information")
    st.exception(RuntimeError("this is an error"))
    st.error("error")
    st.success("horreh")
    st.warning("warning")