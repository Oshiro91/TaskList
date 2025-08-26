import streamlit as st
import pandas as pd
from streamlit_theme import st_theme

# Set page configuration
st.set_page_config(layout="wide", page_icon="🤖", initial_sidebar_state="expanded")

if 'logged_user' not in st.session_state:
    st.session_state.logged_user = None

def get_theme():

    try:
        theme_data = st_theme()
        if theme_data and isinstance(theme_data, dict):
            return theme_data.get('base', 'light')
        return 'light'
    except Exception:
        return 'dark'

# Check theme
theme = get_theme()

if st.session_state.logged_user is None :
    st.session_state.pages = {
        "Login": [
            st.Page("./pages/login.py", title="Login"),
        ],
    }

elif st.session_state.logged_user == 'FERNANDO':
    # Sidebar Menu Configuration
    st.session_state.pages = {
        "pages": [
             st.Page("./pages/second_page.py", title="Chatbot"),
            
         ],
    }

pg = st.navigation(st.session_state.pages)
pg.run()