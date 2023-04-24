
from bbauMain.bbauMain.GptApp.gptapi.GPTpost import pcApi

import requests
import json,random

# import requests
# import ssl
#
# hostname = "api.aichatos.cloud"

# # 创建SSL上下文对象，并设置check_hostname属性
# context = ssl.SSLContext()
# context.check_hostname = True
#
gpt = pcApi()

gpt.updata("生辰八字是怎么计算出来的",gpt.id)
text = gpt.getpost()
print(text)

