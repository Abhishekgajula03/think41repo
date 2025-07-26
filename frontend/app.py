import streamlit as st
import requests

st.title("E-Commerce Chatbot")
question = st.text_input("Ask a question:")

if question:
    try:
        response = requests.post(
            'http://localhost:5000/query',
            json={'question': question},
            timeout=5  # Wait max 5 seconds for a response
        )
        if response.status_code == 200:
            st.write(response.json())
        else:
            st.error(f"Backend error: {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Could not connect to backend. Is Flask running? Error: {e}")
