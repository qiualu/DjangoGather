from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from urllib.parse import unquote

import urllib.parse

def index(request):
    request_path = request.path  # 获取请求路径，如 /%E6%8A%95%E7%A5%A8%E5%BA%94%E7%94%A8/

    # 解码请求路径中的 URL 编码部分
    decoded_path = urllib.parse.unquote(request_path, encoding='utf-8')

    # 打印解码后的请求路径
    # print(f"请求路径: {decoded_path}")
    return HttpResponse("视图功能 index")
def detail(request, question_id):
    request_path = request.path  # 获取请求路径，如 /%E6%8A%95%E7%A5%A8%E5%BA%94%E7%94%A8/

    # 解码请求路径中的 URL 编码部分
    decoded_path = urllib.parse.unquote(request_path, encoding='utf-8')

    # 打印解码后的请求路径
    # print(f"请求路径: {decoded_path}")
    # 使用元组来传递所有格式化参数
    return HttpResponse("视图:  %s at question %s." % (decoded_path, question_id))
def results(request, question_id):
    response = "视图:  results of question %s."

    # 运算符来格式化一个只设计用于单个参数的
    return HttpResponse(response % question_id)
def vote(request, question_id):
    request_path = request.path  # 获取请求路径，如 /%E6%8A%95%E7%A5%A8%E5%BA%94%E7%94%A8/

    # 解码请求路径中的 URL 编码部分
    decoded_path = urllib.parse.unquote(request_path, encoding='utf-8')

    return HttpResponse("视图:  on question %s." % question_id)


from django.template import loader
def html_index(request):
    template = loader.get_template('html/index.html')
    context = {
            'latest_question_list': 5,
        }
    return HttpResponse(template.render(context, request))

from django.http import Http404

from polls.models import Question

def html_render(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    latest_question_list = [0,0,0,1,5,6]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'html/index.html', context)

def html_id_model(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'model_id.html', {'question': question})










