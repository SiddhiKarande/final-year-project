import streamlit as st

def login():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Check if the username and password are correct (this is a simple example)
        if username == "user" and password == "password":
            st.success("Logged in successfully!")
            return True
        else:
            st.error("Invalid username or password. Please try again.")
            return False

if __name__ == "__main__":
    login()
