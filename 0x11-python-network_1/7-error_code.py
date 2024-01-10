#!/usr/bin/python3
"""Error code"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    code = req.status_code
    if code == 200:
        print(req.text)

