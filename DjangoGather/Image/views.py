from django.shortcuts import render

# Create your views here.
import numpy as np

from django.http import JsonResponse,HttpResponse


import qrcode
from io import BytesIO

import time
import os,sys

sys.path.append(r'.\static\image\imgData')

def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'image/html/index.html', context)

# 返回图片地址
def getimgPath(request):


    print(os.getcwd())

    return HttpResponse("hello world zhensha")
# 上传图片到服务器
def sendImageData(request):

    # start = time.time()
    imgSrc = request.FILES.getlist('img')
    for item in imgSrc:
        # print(os.getcwd())
        # print(" kkkk -  ",os.path.join(os.path.join(os.getcwd(),"static\image\imgData"),item.name))
        # imgpath = os.path.join(os.path.join(os.getcwd(),"static\image\imgData"),item.name)
        with open(item.name,'wb') as f:
            for c in item.chunks():
                f.write(c)
                print("---  save img ---")
    # print("运行时间 ",time.time() - start) # 运行时间  0.0020294189453125
    return HttpResponse("hello world zhensha")

# 上传图片到服务器
def sendImageData2(request):

    print("sendImageData  POST -- ")
    if request.POST:
        print(" - - - -5512- - -- ")
        myFile = request.FILES.get("image", None)
        # print(type(myFile))
        print(request.POST["image"])
        print(request.POST["width"])
        print(request.POST["height"])
        #
        nparr = np.frombuffer(myFile.read(), dtype=np.uint8)
        # with open("yy4.jpg", 'wb') as f:
        #     f.write(myFile.read())
        #     print("end")
        # print(type(myFile.read()))
        print('nparr type       ：', type(nparr))
        print(nparr)
        print(len(nparr),nparr[0],nparr[1],nparr[2],nparr[3],nparr[4],nparr[5])

        width  = int(request.POST["width"])
        height = int(request.POST["width"])
        tulist = []
        for h in range(width-2,width):
            widthlist = []
            for w in range(height-2,height):
                rgba = []
                index = (h * width * 4) + (w * 4)
                # rgba.append(nparr[index])
                # rgba.append(nparr[index+1])
                # rgba.append(nparr[index+2])
                # rgba.append(nparr[index+3])
                # widthlist.append(rgba)

                print(index+3)

            # tulist.append(widthlist)
        # print(tulist)
    return HttpResponse("hello world zhensha")

def imgDowmload(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'image/html/imgDowmload.html', context)

def qrcodeCreate(request,data):

    img = qrcode.make(data)
    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()
    response = HttpResponse(image_stream, content_type="image/png")
    return response

def qrcodeCreate2(request,data):
    context = {}

    img = qrcode.make(data)
    print("创建二维码",data)
    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()
    print("创建二维码", 12315)
    context['image_stream'] = image_stream
    # return render(request, 'image/html/qrcodeCreate.html', context)

    response = HttpResponse(image_stream, content_type="image/png")
    return response




def showimage(request,data):
    # print(1235,data)

    imgpath = r"/static/image/imgData/" + data
    print("shu - ", imgpath)
    return render(request, 'image/html/showimage.html' ,{"imgpath": imgpath})


# - ----- --- - --  -- -- -
from django.views.decorators.csrf import csrf_exempt
from .models import IMG

@csrf_exempt
def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img'),
            name = request.FILES.get('img').name
        )
        new_img.save()
    return render(request, 'image/html/uploadimg.html')

@csrf_exempt
def showImg(request):
    imgs = IMG.objects.all()
    content = {
        'imgs':imgs,
    }
    for i in imgs:
        print(i.img.url)
    return render(request, 'image/html/showimg.html', content)

