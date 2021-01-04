import requests
import time
from random import randint
from tqdm import tqdm

def bot(url, _type="GET", header={}, data={}):
    if _type == "GET":
        html = requests.get(url, headers = header, data = data).content
    elif _type == "POST":
        html = requests.post(url, headers = header, data = data).content        

    return html

if __name__ == "__main__":
    url = "<Target_URL>"

    print("Start raising ...")
    while True:
        bot(url)
        time.sleep(randint(0, 1))
