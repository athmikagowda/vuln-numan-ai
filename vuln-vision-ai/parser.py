import re

def parse_nmap_log(raw_text):
    """Extract open ports, services, and versions from Nmap output."""
    findings = []
    lines = raw_text.strip().split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if '/tcp' in line or '/udp' in line or 'open' in line.lower():
            findings.append(f'Line {i+1}: {line}')
        if re.search(r'(open|version)[^\d]*(\d+\.\d+(?:\.\d+)?)', line, re.I):
            findings.append(f'Line {i+1}: {line}')
    return '\n'.join(findings) if findings else raw_text

def parse_burp_export(raw_text):
    """Extract Burp Suite issues (simplified for common formats)."""
    findings = []
    lines = raw_text.strip().split('\n')
    for i, line in enumerate(lines):
        if any(keyword in line.lower() for keyword in ['sql injection', 'xss', 'high', 'medium', 'cve', 'vulnerable']):
            findings.append(f'Line {i+1}: {line.strip()}')
    return '\n'.join(findings) if findings else raw_text

def clean_input(raw_text):
    """General cleanup for any log format."""
    cleaned = re.sub(r'\n{3,}', '\n\n', raw_text)  # Remove excess blank lines
    cleaned = re.sub(r'\s+', ' ', cleaned)          # Normalize whitespace
    return cleaned[:30000]                           # Truncate to 30k chars
