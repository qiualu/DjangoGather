from django.conf.urls import url

from . import views
from django.views.static import serve


from django.conf.urls.static import static
from django.conf import settings

from django.urls import path

urlpatterns = [

    url('getBin/(.+)$', views.showimage),# 显示图片
    url(r'^$', views.index),  # #添加index/路径配置

]
#  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  这句话是用来指定和映射静态文件的路径

