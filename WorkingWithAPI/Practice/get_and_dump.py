import requests
import json

def get_and_dump(path, url):
    r = requests.get(url)

    print("Status code: ", r.status_code)
    # store apt response in a variable
    response_data = r.json()
    with open(path, 'w') as fobj:
        json.dump(response_data, fobj)

def load_data(path):
    try:
        with open(path, 'r') as fobj:
            data = json.load(fobj)
            return data
    except FileNotFoundError:
        print("File Not Found")
