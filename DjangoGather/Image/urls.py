from django.conf.urls import url

from . import views
from django.views.static import serve


from django.conf.urls.static import static
from django.conf import settings

from django.urls import path

urlpatterns = [

    url('imgDowmload$', views.imgDowmload),
    url('qrcodeCreate/(.+)$', views.qrcodeCreate),

    # url('showimage$', views.showimage), # 显示图片
    url('showimage/(.+)$', views.showimage),# 显示图片

    url('getimgPath$', views.getimgPath), # 获得图片的地址
    url('sendImageData$', views.sendImageData), # 上传图片到服务器
    url('sendImageData2$', views.sendImageData2),  # 上传图片到服务器

    # --------
    url(r'upload$', views.uploadImg),
    url(r'show$', views.showImg),



    url(r'^$', views.index),  # #添加index/路径配置

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  这句话是用来指定和映射静态文件的路径






