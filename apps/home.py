import streamlit as st
#from PIL import Image


def app():

    st.title("cycle_safe(berlin) - helping to keep you and your bike safe")

    st.header("How can we use Machine Learning to mitigate")
    st.header("1. Bike theft risk")
    st.header("2. Bike accident risk")

    #image = Image.open('./images/BikeTheft.png')
    st.image("./images/BikeTheft.png", caption='bike theft')

    st.markdown("### The Team")

    st.header("Hitoshi Michinaka [Linkedin](https://www.linkedin.com/in/hmichinaka/)")
    st.header("Dominik Abratanski [Linkedin](https://www.linkedin.com/in/dominikabratanski/)")
    st.header("Lukas Hartung [Linkedin](https://www.linkedin.com/in/lukas-h-0438578b/)")
    st.header("Marlon Deus [Linkedin](https://www.linkedin.com/in/marlon-deus-0a37031b4/)")
    st.header("Paul Roberts [Linkedin](https://www.linkedin.com/in/paul-roberts-871a6790/)")
    st.header("Jakob Hohenstein [Linkedin](https://www.linkedin.com/in/jakob-hohenstein-53667914a/)")
