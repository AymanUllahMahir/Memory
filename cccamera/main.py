import streamlit as st
from streamlit_option_menu import option_menu
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "project", "Group List", "Thanks-Note"],
        icons=["house", "arrow-up-right-circle", "person", "chat-left-heart-fill"],
        orientation="horizontal",
        default_index=0,
    )

if selected == "Home":
    st.write("Welcome to our project's official website")
elif selected == "project":
    st.write("Project name : Smart Attendance System ")
elif selected == "Group List":
    st.write("1. Ayman Ullah Mahir")
    st.write("2. Nahidul Islam ")
    st.write("Samia Islam অকর্মা")
else:
    st.write("Lots of Gratefulness to our honorable Masud Rana Robin sir who introduced us to the wandering and amazing world of programming and taught us walking !! He taught us to walk but soon we will run. we will win. We will lose. A plant grows. Someday that was alsop as seed. Now we are seed. Soon we will become tree. Thank you so much sir ")