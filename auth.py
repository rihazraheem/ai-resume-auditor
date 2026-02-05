import streamlit as st
from config import Config

class AuthManager:
    @staticmethod
    def login():
        if "authenticated" not in st.session_state:
            st.session_state.authenticated = False

        if not st.session_state.authenticated:
            st.subheader("HR Login")
            user=st.text_input("Username")
            pwd=st.text_input("Password", type="password")
            
            if st.button("Access Portal"):
                if user==Config.HR_USERNAME and pwd==Config.HR_PASSWORD:
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("Invalid credentials.")
            return False
        
        AuthManager.show_logout_button()
        return True

    @staticmethod
    def show_logout_button():
        with st.sidebar:
            st.write(f"Logged in as: {Config.HR_USERNAME}")
            if st.button("Logout"):
                st.session_state.authenticated=False
                st.rerun()
