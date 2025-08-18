import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(layout="wide", page_icon="📊", page_title="TaskList")
st.session_state.pages = {}

st.session_state.pages = {
    "Login": [
         st.Page("./pages/main_page.py", title="Main Page", icon="🏠"),
         st.Page("./pages/second_page.py", title="Second Page", icon="🏠"),
    ],
}

pg = st.navigation(st.session_state.pages)
pg.run()