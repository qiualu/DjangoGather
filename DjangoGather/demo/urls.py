from django.conf.urls import url
from django.urls import path,include
from django.views.static import serve

# 视图文件
from . import views
from . import viewsTemplates
from . import viewsStatic

from . import viewsClass

# rest --- Api 数据接口
from rest_framework import routers
from .viewsRest import BlogViewSet
routers = routers.DefaultRouter()
routers.register(r'blog',BlogViewSet)


urlpatterns = [


    # -----viewsStatic.py------ rest API
    url(r'^viewsRest/', include(routers.urls)),

    # -----viewsClass.py------ 类视图
    url(r'^viewsClass/index$', viewsClass.IndexView.as_view()),

    # -----views.py------
    url(r'^returnText$', views.returnText),  # 返回方式_文本返回
    url(r'^returnNotFound$', views.returnNotFound),  # 返回方式_文本返回 _ 404 带错误返回
    url(r'^returnTextStatus$', views.returnTextStatus),  # 返回方式_文本返回 带状态码
    path('articles/2003/', views.special_case_2003),
    path('runoob/', views.runoob),

    # -----viewsTemplates.py------ 关于模板类的视图
    url(r'^viewsTemplates/variate$', viewsTemplates.variate),  # 模板HTML 接收变量
    url(r'^viewsTemplates/variateList$', viewsTemplates.variateList),  # 模板HTML 接收 列表 变量
    url(r'^viewsTemplates/variateFilter$', viewsTemplates.variateFilter),  # 模板HTML 接收 变量 过滤器
    url(r'^viewsTemplates/staticFileSet$', viewsTemplates.staticFileSet),  # 模板HTML 接收 变量 过滤器

    # -----viewsStatic.py------ 关于模板类的视图
    url(r'^viewsStatic/index$', viewsStatic.index),  # 模板HTML 接收 变量 过滤器
    url(r'^viewsStatic/vueLearn$', viewsStatic.index),  # vue 模版 使用案例


    # Dome 模版 索引
    url(r'^', views.index),  # #添加index/路径配置    ^ 开头   $ 结尾   配置路由 第二种写法 path('articles/2003/', views.index),
]






