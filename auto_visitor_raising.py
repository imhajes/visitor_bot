import requests
import json
from tqdm import tqdm

def bot(url, _type="GET", header={}, data={}):
    if _type == "GET":
        html = requests.get(url, headers = header, data = data).content
    elif _type == "POST":
        html = requests.post(url, headers = header, data = data).content        

    return html

if __name__ == "__main__":
    url = "<Input_URL>"

    for i in tqdm(range(100)):
        bot(url)