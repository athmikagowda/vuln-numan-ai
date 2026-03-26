import google.generativeai as genai
import os
import time
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def analyze_vulnerability(cleaned_data: str) -> str:
    for attempt in range(3):
        try:
            model = genai.GenerativeModel(
                model_name='gemini-2.0-flash-lite',
                system_instruction=SYSTEM_PROMPT
            )
            user_message = f"""Analyze this vulnerability data:
{cleaned_data}
Provide remediation only for explicitly stated findings."""
            response = model.generate_content(user_message)
            return response.text

        except Exception as e:
            if "429" in str(e):
                wait_time = 30 * (attempt + 1)
                print(f"Rate limited. Waiting {wait_time} seconds... (attempt {attempt+1}/3)")
                time.sleep(wait_time)  # ✅ Fixed indentation
            else:
                return f"Analysis failed: {str(e)}. Check your API key and internet connection."

    return "Analysis failed after 3 retries. Please wait a few minutes and try again."
