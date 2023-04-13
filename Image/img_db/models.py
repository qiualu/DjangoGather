from django.db import models

# Create your models here.
class IMG(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=20)


class User(models.Model):
    name = models.CharField(max_length=50)

    # upload_to 指定上传文件位置
    # 这里指定存放在img/ 目录下
    headimg = models.FileField(upload_to="img/")

    # 返回名称
    def __str__(self):
        returnself.name

