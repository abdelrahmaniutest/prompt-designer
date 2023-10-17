import streamlit as st
import requests
from datetime import datetime

def api(name, description, prompt, author, date):

    # Define the URL of the API endpoint
    url = 'http://127.0.0.1:8000/modes/'

    data = {
        'name': name,
        'description': description,
        'prompt': prompt,
        "Author": author,
        "Date": date
    }

    response = requests.post(url, json=data)



# Set the page title
st.set_page_config(page_title="Input Form App")

# Page title
st.title("Prompt Designer 🤖😉")

# Input 1
name = st.text_input("Prompt Name", placeholder="Name...")

# Input 2
description = st.text_input("Prompt Description", placeholder="Description...")

# Input 3
author = st.text_input("Prompt Author", placeholder="Author Name...")

st.write("""
<style>
    .custom-text-input {
        height: 500px !important;
    }
</style>
""", unsafe_allow_html=True)

# Input 4
# prompt = st.text_input("Prompt Instructions", placeholder="Prompt...")
prompt = st.text_area("", height=300, placeholder="Prompt...")

# Create a button to submit the form
if st.button("Submit"):

    try:
        api(name, description, prompt, author, str(datetime.now()))
        st.success("Promt saved successfully!")
        
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")


        
    
