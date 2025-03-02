import webbrowser
import re

def website_opener(domain):
    # Check if domain contains a dot, implying a TLD is included
    if '.' not in domain:
        domain += '.com'  # Default to .com if no TLD is provided
    
    # Simple regex to validate domain format
    if not re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', domain):
        print("Invalid domain format.")
        return False
    
    url = f'https://www.{domain}'
    try:
        webbrowser.open(url)
        print(f"Opening {url}")
        return True
    except Exception as e:
        print(f"Failed to open {url}. Error: {e}")
        return False
#website_opener("peteranswers")