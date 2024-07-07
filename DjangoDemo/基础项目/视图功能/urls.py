from django.urls import path

from . import views

from django.urls import re_path

urlpatterns = [
    path('', views.index, name='index'),


    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('html/index', views.html_index, name='html_index'),
    path('html/html_render', views.html_render, name='html_render'),

    path('html/ModelID/<int:question_id>', views.ModelID, name='ModelID'),
    path('html/前五个数据', views.前五个数据, name='ModelAll'),
    path('html/前五跳转_选项模型/<int:question_id>', views.前五跳转_选项模型, name='前五跳转_选项模型'),

    re_path(r'^.*$', views.index, name='index'),
]

