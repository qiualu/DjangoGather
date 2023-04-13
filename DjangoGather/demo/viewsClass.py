
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse


class IndexView(View):

    def get(self,request):

        # 不分离 架构
        return render(request,"demo/viewsClass/index.html")
