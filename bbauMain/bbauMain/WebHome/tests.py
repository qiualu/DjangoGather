from django.test import TestCase

# Create your tests here.


import requests
import json,random


id = random.getrandbits(64)
print(id)
url = "https://api.aichatos.cloud/api/generateStream"

headers = {
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

content = "冬天的冷可以保存到夏天吗" #input("请输入需要请问的问题:")

data = {
        "prompt": content,
        "userId": "#/chat/154545645",  # + str(id),
        "network": True,
        "apikey": "",
        "system": "",
        "withoutContext": False,
    }
def pp():

    # POST 请求参数

    # 发送 POST 请求并获取响应
    # response = requests.post(url, headers=headers, data=json.dumps(data))
    response = requests.request("POST", url, headers=headers,  json=data)  # data=json.dumps(data)
    # 打印响应内容
    print(response.text)

# 游戏开始上传服务器
def gameup():
    # url = "http://39.108.51.207/bracelet-portal/api/v1/game/permission/checkAuth"
    # url = "http://172.16.1.3:7020/bracelet-portal/api/v1/game/permission/checkAuth" #
    # http = str(op("fwqi1")[0,0])
    # url = http + "/bracelet-portal/api/v1/game/permission/checkAuth"  #

    payload = {
        "deviceSn": "ST-NFC-GAME-G1",  # "deviceSn": "ST-NFC-GAME-G1",
        "braceletSn": "TB68B6B3344824" ,  # "braceletSn": "TB68B6B3344824"
        "taskId": "10"
    }
    # //headers = {"SerialNO": "342342343432"}
    response = requests.request("POST", url, json=payload)
    print("游戏开始上传服务器 : ", response.text)
    print("--------------------------------------")


response = requests.request("POST", url, headers=headers,  json=data)  # data=json.dumps(data)
print(response.text)

