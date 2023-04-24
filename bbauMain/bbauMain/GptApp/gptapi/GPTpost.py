

import requests
import json,random




class pcApi:
    def __init__(self):
        self.id = random.getrandbits(64)

        self.url = "https://api.aichatos.cloud/api/generateStream"

        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Referer": "https://chat9.yqcloud.top/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48",
            "Host": "api.aichatos.cloud",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Origin": "https://chat9.yqcloud.top",
            "Sec-Ch-Ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not: A - Brand\";v=\"99\"",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
        }
    def getId(self):
        self.id = random.getrandbits(64)
        return self.id
    def updata(self,content,id):
        # self.id = random.getrandbits(64)
        self.data = {
            "prompt": content,
            "userId": "#/chat/" + str(id),
            "network": True,
            "apikey": "",
            "system": "",
            "withoutContext": False,
        }
        print(self.data)

    def getpost(self):
        # response = requests.request("POST", self.url, json=self.data)
        response = requests.request("POST", self.url, headers=self.headers, json=self.data, verify=True)
        # response = requests.request("POST", self.url, headers=self.headers, json=self.data, verify=True, stream=True)
        # for chunk in response.iter_content(chunk_size=8192):
        #     print(chunk.decode('utf-8'),len(chunk))
        return response.text
    def getstreampost(self):
        # response = requests.request("POST", self.url, json=self.data)
        #response = requests.request("POST", self.url, headers=self.headers, json=self.data, verify=True)
        response = requests.request("POST", self.url, headers=self.headers, json=self.data, verify=True, stream=True)

        return response