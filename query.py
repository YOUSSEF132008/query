import os
from os import system as ss
ll = 'pip install'
try:
	from cfonts import render
except ModuleNotFoundError:
	ss(ll+' python-cfonts')
try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    
import re
import urllib.parse

print(f'''{render('YOUSSEF', colors=['green', 'yellow'], align='center')}''')
def extract_tgwebappdata():
    url_input = input("Enter the URL: ").strip()

    # Regular expression to extract tgWebAppData
    match = re.search(r"tgWebAppData=([^&]+)", url_input)

    if match:
        tgWebAppData = urllib.parse.unquote(match.group(1))  # Decode URL encoding
        print("\nExtracted tgWebAppData:")
        print(tgWebAppData)
    else:
        print("\nError: 'tgWebAppData' parameter not found in the URL.")

if __name__ == "__main__":
    extract_tgwebappdata()