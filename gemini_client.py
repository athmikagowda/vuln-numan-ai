import os
from groq import Groq
from prompts import SYSTEM_PROMPT

try:
    import streamlit as st
    api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
except:
    api_key = os.getenv("GROQ_API_KEY")

def analyze_vulnerability(cleaned_data: str) -> str:
    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Analyze this vulnerability data:\n{cleaned_data}\nProvide remediation only for explicitly stated findings."}
            ],
            max_tokens=2000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Analysis failed: {str(e)}"
