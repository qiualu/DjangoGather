from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.http import JsonResponse
# 禁用缓存
from django.views.decorators.cache import never_cache
from django.middleware.csrf import get_token



import json
import time

shbbanben = {
    1 : 1,
    2 : 1,
    3 : 1,
}

# # 'http://127.0.0.1:8000/'
# def index(request):
#     print("=== index ===")
#
#     # data = "2022 Home:" + str(time.time())
#     data = {
#         'name': 'John',
#         'age': 30,
#         'city': 'New York'
#     }
#     # return HttpResponse(data) # 返回字符串
#     return JsonResponse(data)   # 返回json


def index(request):
    data = [1, 2, 3, 4]
    return render(request, 'WebHome/home.html', {'data': data})



def showHead(request):
    if request.method == 'OPTIONS':
        print("=== OPTIONS ===")
        # 处理预检请求
        response = HttpResponse(status=204)
        response['Access-Control-Allow-Origin'] = '*'  # # 允许所有来源跨域访问
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'  # 允许 GET、POST、PUT、DELETE 方法
        response['Access-Control-Allow-Headers'] = 'Accept,yhname'  # 允许 Content-Type 请求头 ,Content-Type,
        response['Access-Control-Allow-Credentials'] = 'true'  # 允许发送 Cookie 凭证信息
        return response
    elif request.method == 'GET':
        print("=== GET ===")
        # 获取请求头信息
        accept_header = request.META.get('HTTP_ACCEPT')
        yhname_header = request.META.get('HTTP_YHNAME')

        # 获取请求网址
        url = request.build_absolute_uri()
        # 获取请求参数
        params = request.GET
        print("params :", params["name"], accept_header, yhname_header)
        data = {
            'name': 'John',
            'age': 30,
            'city': 'New York',
            'accept_header': accept_header,  # 将请求头信息添加到响应数据中
            'yhname_header': yhname_header,
            'url': url,  # 将请求网址添加到响应数据中
            'params': dict(params)  # 将请求参数添加到响应数据中
        }
        response = JsonResponse(data, safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Accept,yhname'
        return response

def showimage(request,data):
  
    
    data = "get : " + str(data)
    
    return HttpResponse(data)
    
    
 
def getBinBb(request,data):
    
    try:
        sbh = int(data);
        if sbh in shbbanben:
            data = shbbanben[sbh]
        else:
            data = 0
        return HttpResponse(data)
        
    except:
        data = 0
        return HttpResponse(data)




