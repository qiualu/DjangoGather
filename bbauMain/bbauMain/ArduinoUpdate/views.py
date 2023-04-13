from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):

    return HttpResponse('hello world')


def showimage(request,data):
    print(1235,data)

    return HttpResponse(data)


