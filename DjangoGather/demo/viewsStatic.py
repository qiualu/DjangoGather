#-*- coding: UTF-8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseNotFound

def index(request):
    # return HttpResponse("funtion : index : Hello demo")
    return render(request, "demo/viewsStatic/index.html")

def vueLearn(request):
    # return HttpResponse("funtion : index : Hello demo")
    return render(request, "demo/viewsStatic/vueLearn.html")





