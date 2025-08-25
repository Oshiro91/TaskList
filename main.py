import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(layout="wide", page_icon="📊", page_title="TaskList")
st.session_state.pages = {}

st.session_state.pages = {
    "Login": [
         st.Page("./pages/login.py", title="login", icon="🔑")
    ],
}

pg = st.navigation(st.session_state.pages)
pg.run()