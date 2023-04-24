from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.http import JsonResponse
# 禁用缓存
from django.views.decorators.cache import never_cache
from django.middleware.csrf import get_token
from django.http import StreamingHttpResponse

from .gptapi.GPTpost import pcApi

import json
import time
import requests
import json,random

def index(request):
    data = [1, 2, 3, 4]
    return render(request, 'WebHome/home.html', {'data': data})


# 将所有视图函数都加上@never_cache装饰器 # 禁用缓存
@never_cache
def chat(request):
    if request.method == 'GET':
        token = get_token(request)
        data = [1, 2, 3, 4]
        print("token: ", token)
        gpt = pcApi()
        id = gpt.getId()
        return render(request, 'GptApp/chat.html', {'data': data,'csrf_token': token,"id":id})
    elif request.method == 'POST':
        # prompt = request.POST.get('prompt', '')  # 获取请求中的 prompt 参数 id
        # id = request.POST.get('id', '')  # 获取请求中的 prompt 参数 id

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        prompt = body_data.get('prompt', '')  # 获取 JSON 请求中的 prompt 参数值
        id = body_data.get('id', '')  # 获取 JSON 请求中的 id 参数值

        token = request.COOKIES.get('csrftoken')

        print("id", id, " prompt ", prompt, " token ", token)

        gpt = pcApi()
        gpt.updata(prompt,id)
        # # text = gpt.getpost()
        Gptresponse = gpt.getstreampost()
        # text = ""
        # headers = gpt.headers
        # data = gpt.data
        # url = gpt.url
        #
        # Gptresponse = requests.request("POST",  url, headers= headers, json= data, verify=True, stream=True)

        # for chunk in response.iter_content(chunk_size=8192):
        #     print(chunk.decode('utf-8'),len(chunk))
        #     text += chunk.decode('utf-8')

        def stream():
            # 生成响应内容
            # yield 'start\n'
            # for i in range(10):
            #     # 每次返回的数据量可以自己调整
            #     time.sleep(0.5)
            #     yield 'data {}\n'.format(i)
            # yield 'end\n'
            for chunk in Gptresponse.iter_content(chunk_size=8192):
                # print(chunk.decode('utf-8'), len(chunk))
                # text += chunk.decode('utf-8')
                yield chunk.decode('utf-8')

        response = StreamingHttpResponse(stream(), content_type='application/octet-stream')
        return response

        # print("gpt", text)
        # response = {}
        # response['content'] = text  # 假设返回的内容是 "Hello world"
        # response['test'] = "测试字段"
        # return JsonResponse(response)
    else:
        return HttpResponse("404 请求异常")  # 返回字符串