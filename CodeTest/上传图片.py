import requests
import json

def upload():
    try:
        files=[("img",open('wd1.jpg', 'rb')),("img",open('wd2.jpg', 'rb')),("img",open('wd3.jpg', 'rb')),("img",open('wd4.jpg', 'rb'))]
        x = requests.post("http://127.0.0.1:8000/image/sendImageData",files=files)
        print(json.loads(x.text, encoding='utf-8'))
    except Exception as e:
        print(e)


upload()
