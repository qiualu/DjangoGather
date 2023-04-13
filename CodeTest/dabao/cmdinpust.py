


import sys
import requests
import json



imgname = ""

for arg in sys.argv:
    print(arg)
    if arg:
        imgname = arg
    print(type(arg))


# 123.jpg为图片，与代码在当前目录下，image/jpeg 为图片格式
files = {
    "tn": "pc",
    "image": (imgname, open(imgname, 'rb'), "image/jpeg"),
    "from": "pc",
    "image_source": "PC_UPLOAD_SEARCH_FILE",
    "range": '{"page_from": "searchIndex"}'
}

url = "https://api.lightfactorymedia.com/caisi/upload01"
r = requests.post(url, files=files)
print(r, r.status_code, r.text)
jsonData = r.text

text = json.loads(jsonData)

urlimg = r"https://api.lightfactorymedia.com/caisi/img?src=" + text["src"]
print(urlimg)

import qrcode
img = qrcode.make(urlimg)
img.save('ewm.png')


















