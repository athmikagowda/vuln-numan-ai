# 🔒 Vuln-Vision AI

Intelligent Security Remediation Tool powered by AI (Gemini + Groq)

## 📁 Project Structure

```
vuln-vision-ai/
├── app.py                    # Main Streamlit app
├── app2.py                   # Connection Debugger
├── gemini_client.py          # Groq AI client
├── gemini_client_backup.py   # Gemini AI backup client
├── parser.py                 # Log parser (Nmap, Burp Suite)
├── prompts.py                # AI system prompts
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
└── .gitignore                # Git ignore file
```

## 🚀 Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/vuln-vision-ai.git
cd vuln-vision-ai
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup environment variables
```bash
cp .env.example .env
# Open .env and add your API keys
```

### 4. Run the app
```bash
streamlit run app.py
```

## 🔑 API Keys Required
- **GEMINI_API_KEY** - Get from [Google AI Studio](https://makersuite.google.com/)
- **GROQ_API_KEY** - Get from [Groq Console](https://console.groq.com/)

## ⚠️ Disclaimer
For authorized penetration testing only.
