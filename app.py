import streamlit as st
from multiapp import MultiApp
from apps import timelaps, Home

st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here
apps.add_app("Contact", Home.app)
apps.add_app("Time Laps", timelaps.app)


# The main app
apps.run()