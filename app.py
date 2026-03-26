import streamlit as st
import io
from parser import parse_nmap_log, parse_burp_export, clean_input
from gemini_client import analyze_vulnerability

st.set_page_config(page_title='Vuln-Vision AI', layout='wide', initial_sidebar_state='expanded')
st.title('🔒 Vuln-Vision AI - Intelligent Security Remediation')
st.markdown('Upload or paste raw vulnerability scan output (Nmap, Burp Suite, etc.) for AI-powered analysis with fixes.')

# Sidebar for instructions
with st.sidebar:
    st.markdown('### Quick Start')
    st.code('''Sample Nmap input:
Starting Nmap scan...
22/tcp open ssh OpenSSH 7.2
80/tcp open http Apache httpd 2.4.18
443/tcp open https nginx 1.14.0
3306/tcp open mysql MySQL 5.7.32''', language='bash')
    st.markdown('### Expected Output')
    st.markdown('- OWASP mappings\n- Severity ratings\n- Business impacts\n- Code/config patches')

# Session state for persistence
if 'result' not in st.session_state:
    st.session_state.result = None
if 'cleaned_data' not in st.session_state:
    st.session_state.cleaned_data = None

# Input options
col1, col2 = st.columns([1, 3])
with col1:
    input_type = st.selectbox('Input Type', ['Nmap Log', 'Burp Suite Export', 'Raw Text'])
with col2:
    raw_input = st.text_area('Paste your scan output:', height=200, key='raw_input')

uploaded_file = st.file_uploader('Or upload a log file', type=['txt', 'xml', 'log', 'nmap'])

if uploaded_file:
    raw_input = io.StringIO(uploaded_file.read().decode('utf-8', errors='ignore')).read()
    st.session_state.raw_input = raw_input  # Persist for reruns

# Process input
if st.button('🚀 Analyze Vulnerabilities', type='primary', use_container_width=True) and raw_input.strip():
    with st.spinner('🤖 AI analyzing your scan data... (Gemini 1.5 Pro)'):
        if input_type == 'Nmap Log':
            cleaned = parse_nmap_log(raw_input)
        elif input_type == 'Burp Suite Export':
            cleaned = parse_burp_export(raw_input)
        else:
            cleaned = clean_input(raw_input)

        st.session_state.cleaned_data = cleaned
        st.session_state.result = analyze_vulnerability(cleaned)
        st.rerun()  # ✅ Fixed indentation

# Display results
if st.session_state.result:
    st.success('✅ Analysis Complete!')
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('### 🔍 Cleaned Input Sent to AI')
        st.text_area('', st.session_state.cleaned_data, height=300, disabled=True)

    with col2:
        st.markdown('### 📋 Remediation Report')
        st.markdown('```markdown\n' + st.session_state.result + '\n```')

# Footer
st.markdown('---')
st.markdown('Built with Streamlit + Google Gemini 1.5 Pro | For authorized pentesting only')
