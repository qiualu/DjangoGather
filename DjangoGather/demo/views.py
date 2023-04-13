#-*- coding: UTF-8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseNotFound

def index(request):
    # return HttpResponse("funtion : index : Hello demo")
    return render(request, "demo/html/index.html")

def returnText(request):
    return HttpResponse("funtion : returnText : 返回方式_文本返回")

def returnNotFound(request):
    return HttpResponseNotFound("funtion : returnNotFound : 返回方式_文本返回 _ 404 带错误返回")

# 状态代码创建返回类  带状态码
def returnTextStatus(request):
    return HttpResponse("funtion :  returnTextStatus : 返回方式_文本返回 _带状态码 ",status=200)



def special_case_2003(request,):
    print("poll_id  ")
    return HttpResponse("funtion : special_case_2003 : Hello demo")

def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'demo/html/index.html', context)


