
from django.contrib import admin
from django.urls import path, register_converter, re_path
from . import views

app_name = 'img_db'

urlpatterns = [
    path('add$', views.add, name='add'),
    path('sendmessage$',views.apost),

]

