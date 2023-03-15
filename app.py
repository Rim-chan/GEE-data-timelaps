import streamlit as st
from multiapp import MultiApp
from apps import timelaps

st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here

apps.add_app("Time Laps", timelaps.app)


# The main app
apps.run()