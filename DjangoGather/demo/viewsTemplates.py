#-*- coding: UTF-8 -*-
from django.shortcuts import render

# Create your views here.


def variate(request):
    context = {}
    context['hello'] = 'Hello World!'
    # print("输出模板变量")   字典 , 键 对应HTML变量名   值
    return render(request, 'demo/viewsTemplates/variate.html', context)


def variateList(request):
    views_list = ["列表变量第一个","列表变量第二个","列表变量第三个"]
    print("模板变量列表")
    return render(request, "demo/viewsTemplates/variateList.html", {"views_list": views_list})

def  variateFilter(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['putong'] = 'who me!'
    context['leghtStr'] = "When you return an error such as HttpResponseNotFound, you're responsible for defining the HTML of the resulting error page:"
    context['views_str'] = "<a href='https://www.runoob.com/'>点击跳转</a>"
    import datetime
    now = datetime.datetime.now()
    context['timeD'] = now

    context['condition'] = 1
    context['condition1'] = 1
    context['condition2'] = 1

    context['forList'] = ["列表一", "列表二","列表三"]

    zhongEnglist = True
    if zhongEnglist:
        return render(request, 'demo/viewsTemplates/变量过滤器.html', context)
    else:
        return render(request, 'demo/viewsTemplates/variateFilter.html', context)



def staticFileSet(request):

    return render(request,"demo/viewsTemplates/staticFileSet.html")


