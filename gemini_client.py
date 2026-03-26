import os
from groq import Groq
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT

load_dotenv()

def analyze_vulnerability(cleaned_data: str) -> str:
    try:
        client = Groq(api_key=os.getenv('GROQ_API_KEY'))
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
