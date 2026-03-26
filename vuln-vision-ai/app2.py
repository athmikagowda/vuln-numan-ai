import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Use environment variable instead of hardcoded key
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("Connection Debugger")

if st.button("Force Test"):
    st.info("Attempting to connect...")
    try:
        response = model.generate_content("Say 'System Online'", request_options={"timeout": 5})
        st.success(f"Response: {response.text}")
    except Exception as e:
        st.error("Connection Failed!")
        st.code(f"Error Details: {str(e)}")
        st.warning("If the error says 'Deadline Exceeded', your Wi-Fi/Internet is blocking the AI.")
