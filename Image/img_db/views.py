from django.shortcuts import render

from .models import User
from .forms import AddForm


# Create your views here.
def add(request):
  # 判断是否为post 方法提交
  if request.method == "POST":
    af = AddForm(request.POST, request.FILES)
  # 判断表单值是否和法
  if af.is_valid():
    name = af.cleaned_data['name']
    headimg = af.cleaned_data['headimg']
    user = User(name=name, headimg=headimg)
    user.save()
    return render(request, 'app01/index.html', context={"user":user})
  else:
    af = AddForm()
    return render(request, 'app01/add.html', context={"af":af})


def apost():
  if request.method == 'POST':  # 当提交表单时
    dic = {}
    # 判断是否传参
    if request.POST:
      print(request.POST)
      a = request.POST.get('a', 0)
      b = request.POST.get('b', 0)
      # 判断参数中是否含有a和b
      if a and b:
        res = add_args(a, b)
        dic['number'] = res
        dic = json.dumps(dic)
        return HttpResponse(dic)
      else:
        return HttpResponse('输入错误')
    else:
      return HttpResponse('输入为空')

  else:
    return HttpResponse('方法错误')

