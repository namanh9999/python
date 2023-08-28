import requests 
import json

def dump_data(path,url):
    patten_url = "https://hacker-news.firebaseio.com/v0/item/"
    urls = []
    r = requests.get(url)
    print("Status code: " , r.status_code)
    response = r.json()
    print(type(response))
    for item in response:
        make_url = patten_url + str(item) + ".json"
        urls.append(make_url)
    print(urls)
    save_data(path, urls)

def save_data(path, urls):
    data_temp = [] 
    for url in urls[:30]:
        r = requests.get(url)
        print("Status code: " , r.status_code)
        response = r.json()
        print(response)
        data_temp.append(response)
    try:
        with open(path , 'w') as fobj:
            json.dump(data_temp, fobj)
    except FileNotFoundError:
        print("File not found")

def load_data(path, url):
    dump_data(path, url)
    try:
        with open(path , 'r') as fobj:
            data = json.load(fobj)
        return data
    except FileNotFoundError:
        print("File not found: ")

def only_load(path):
    try:
        with open(path , 'r') as fobj:
            data = json.load(fobj)
            return data
    except FileNotFoundError:
        print("File not found")