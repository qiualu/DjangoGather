from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.http import JsonResponse

import time

shbbanben = {
    1 : 1,
    2 : 1,
    3 : 1,
}


def index(request):
    
    # data = "2022 Home:" + str(time.time())
    data = {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    }
    # return HttpResponse(data) # 返回字符串
    return JsonResponse(data)   # 返回json


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




