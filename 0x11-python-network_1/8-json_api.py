#!/usr/bin/python3
""" Json api"""


if __name__ == '__main__':
    import sys
    import requests
    import json

    if (len(sys.argv) > 1):
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        resp = response.json()
        if (resp):
            print(f'[{resp.get("id")}] {resp.get("name")}')
        else:
            print('No result')
    except json.JSONDecodeError:
        print('Not a valid JSON')
