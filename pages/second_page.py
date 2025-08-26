import streamlit as st

st.title("Second Page")

def logout_button():
    logout_button = st.sidebar.button("Logout")
    if logout_button:
        st.session_state.logged_user = None
        if 'messages' in st.session_state:
            del st.session_state.messages
        st.rerun()

logout_button()