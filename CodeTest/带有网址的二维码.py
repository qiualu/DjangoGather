import qrcode
import numpy as np
import requests
import json

import cv2

# print("start")
# img = qrcode.make('https://www.baidu.com')
# # img <qrcode.image.pil.PilImage object at 0x1044ed9d0>
# img = qrcode.make(data)
#
# print("zxc")
#
# with open('test66.png', 'wb') as f:
#     img.save(f)
#
# print("end")


import qrcode
img = qrcode.make('https://www.baidu.com/s?ie=UTF-8&wd=dajngo%20%E9%93%BE%E6%8E%A5%E7%94%9F%E6%88%90%E4%BA%8C%E7%BB%B4%E7%A0%81')
img.save('test23.png')



# ------------------------------------
# import requests
# import json
#
# imag = open('test.png','rb')
# print("tupan  -- ",type(imag))
# files = {
#     "tn":"pc",
#     "image":("123.jpg",open('test.png','rb'),"image/jpeg"),
#     "from":"pc",
#     "image_source":"PC_UPLOAD_SEARCH_FILE",
#     "range":'{"page_from": "searchIndex"}'
# }
#
# url = "http://127.0.0.1:8000/image/sendImageData"
#
# #r = requests.post(url,data={})
#
# data = {'image': "image125" }
#
# r = requests.post(url,data=data,files=files)
# print(r)


# ------------------------------------

# pic1 = open('test.png', mode='rb')
#
# pic = open('test.png', mode='rb')
# print('pic type         ：',type(pic))
# data = pic.read()
# print('data type        ：',type(data))
# nparr = np.frombuffer(data, dtype=np.uint8)
# print('nparr type       ：',type(nparr))
# segment_data = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
# print('segment_data type：',type(segment_data))

# print(" --------------------------- ")
#
# from io import BytesIO
# from io import BufferedReader
#
#
# #print(op("out1").numpyArray(delayed=False, writable=False))
# img_encode = segment_data
# print('img_encode type：',type(img_encode))
#
# str_encode = img_encode.tostring()
# print('str_encode type：',type(str_encode))
#
# f4 = BytesIO(str_encode)	#转化为_io.BytesIO类型
# print('f4 type：',type(f4))
#
# f5 = BufferedReader(f4)		#转化为_io.BufferedReader类型
# print('f5 type：',type(f5))
#
# if type(f5) == type(pic):
#     print("格式相同")
# else:
#     print("格式不同")

# print(type(f4))
# print(type(f5))




# if type(f5) == type(pic):
# imag = open('test.png','rb')
# pic1 = open('test.png', mode='rb')

# files = {
#     "tn":"pc",
#     "image":("123.jpg",pic,"image/jpeg"),
#     "from":"pc",
#     "image_source":"PC_UPLOAD_SEARCH_FILE",
#     "range":'{"page_from": "searchIndex"}'
# }
#
# url = "http://127.0.0.1:8000/image/sendImageData"
#
# # r = requests.post(url,data={})
#
# data = {'image': "image125" }
#
# r = requests.post(url,data=data,files=files)
# print(r)



