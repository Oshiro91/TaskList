import streamlit as st

if 'logged_user' not in st.session_state:
    st.session_state.logged_user = None

st.write(st.session_state.logged_user)

st.title("Second Page")

def logout_button():
    logout_button = st.sidebar.button("Logout")
    if logout_button:
        st.session_state.logged_user = None
        if 'messages' in st.session_state:
            del st.session_state.messages
        st.rerun()

logout_button()