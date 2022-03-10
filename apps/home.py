import streamlit as st
#from PIL import Image


def app():

    st.title("cycle_safe(berlin):")
    st.header("helping to keep you and your bike safe")

    st.subheader("How can we use Machine Learning to mitigate")
    st.subheader("1. Bike theft risk")
    st.subheader("2. Bike accident risk")

    #image = Image.open('./images/BikeTheft.png')
    st.image("./images/BikeTheft.png", caption='bike theft')

    st.header("The Team")

    st.subheader("Hitoshi Michinaka [Linkedin](https://www.linkedin.com/in/hmichinaka/)")
    st.subheader("Dominik Abratanski [Linkedin](https://www.linkedin.com/in/dominikabratanski/)")
    st.subheader("Lukas Hartung [Linkedin](https://www.linkedin.com/in/lukas-h-0438578b/)")
    st.subheader("Marlon Deus [Linkedin](https://www.linkedin.com/in/marlon-deus-0a37031b4/)")
    st.subheader("Paul Roberts [Linkedin](https://www.linkedin.com/in/paul-roberts-871a6790/)")
    st.subheader("Jakob Hohenstein [Linkedin](https://www.linkedin.com/in/jakob-hohenstein-53667914a/)")
