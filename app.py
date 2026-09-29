import streamlit as st
from langdetect import detect
from googletrans import Translator
from database import register_user, authenticate_user, add_chat, get_chat_history, delete_user
from chatbot import chat_with_gpt

st.set_page_config(page_title="Multi-Page Chatbot", layout="centered")

if "page" not in st.session_state:
    st.session_state["page"] = "home"

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "username" not in st.session_state:
    st.session_state["username"] = ""

def go_to_page(page):
    st.session_state["page"] = page
    st.rerun()

# Home Page (Login/Register)
if st.session_state["page"] == "home" and not st.session_state["logged_in"]:
    st.title("Welcome to the Chatbot")
    menu = st.radio("Select an option", ["Login", "Register"], key="auth_menu")
    
    if menu == "Login":
        with st.form("login_form"):
            st.subheader("Login")
            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password", type="password", key="login_password")
            login_submit = st.form_submit_button("Login")
        
        if login_submit:
            if authenticate_user(username, password):
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.success("Logged in successfully!")
                go_to_page("chat")
            else:
                st.error("Invalid credentials.")
    
    if menu == "Register":
        with st.form("register_form"):
            st.subheader("Register New Account")
            new_user = st.text_input("New Username", key="register_username")
            new_pass = st.text_input("New Password", type="password", key="register_password")
            register_submit = st.form_submit_button("Register")
        
        if register_submit:
            if register_user(new_user, new_pass):
                st.success(f"User registration successful! Welcome, {new_user}. Please login.")
                st.rerun()  # Ensures page refresh after success
            else:
                st.error("Username already exists!")

# Chat Page
if st.session_state["logged_in"] and st.session_state["page"] == "chat":
    st.subheader(f"Welcome, {st.session_state['username']}!")
    
    # Language Selection
    languages = ['English', 'Spanish', 'French']
    language_codes = {'English': 'en', 'Spanish': 'es', 'French': 'fr'}
    selected_language = st.selectbox("Choose your language", languages, key="language_select")
    target_language = language_codes[selected_language]
    translator = Translator()
    
    # User Input Section
    user_input = st.text_input(f"Ask something in {selected_language}:", key="user_input")
    
    col1, col2 = st.columns([4, 1])
    
    with col1:
        if st.button("Send", use_container_width=True) and user_input:
            detected_language = detect(user_input)
            translated_input = translator.translate(user_input, src=detected_language, dest='en').text
            response_in_english = chat_with_gpt(translated_input)  # Now uses GPT + fallback
            final_response = translator.translate(response_in_english, src='en', dest=target_language).text

            add_chat(st.session_state["username"], user_input, final_response)

            st.markdown(f'**You:** {user_input}')
            st.markdown(f'**Bot:** {final_response}')  # Final response may include GPT + Web search

    
    with col2:
        if st.button("Logout", use_container_width=True):
            st.session_state.clear()
            st.session_state["logged_in"] = False
            st.session_state["username"] = ""
            go_to_page("home")

        if st.button("Delete Account", use_container_width=True):
            if delete_user(st.session_state["username"]):
                st.session_state.clear()
                st.session_state["logged_in"] = False
                st.session_state["username"] = ""
                st.success("Your account has been deleted successfully.")
                go_to_page("home")
            else:
                st.error("Failed to delete account.")
    
    # Display Chat History (Latest First)
    st.subheader("Chat History")
    if st.session_state["username"]:
        history = get_chat_history(st.session_state["username"])
        for msg, resp, time in reversed(history):
            st.markdown(f'**{time}** - **You:** {msg}')
            st.markdown(f'**Bot:** {resp}')

# Run Streamlit with a fixed port
if __name__ == "__main__":
    import os
    os.environ["STREAMLIT_SERVER_PORT"] = "8501"