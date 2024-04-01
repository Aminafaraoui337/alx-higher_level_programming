#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    text = response.text
    
    print("Body response:")
    print("\t- type:".format(type(text)))
    print("\t- content:".forma(text))

