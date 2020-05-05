from django.db import models
import time
from django.db import models


class userinfo(models.Model):
    # 如果没有models.AutoField，默认会创建一个id的自增列
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    comment = models.TextField()
    time = models.DateTimeField(default=time.strftime("%Y-%m-%d %H:%M:%S"))
    solve = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class pic(models.Model):
    img_url = models.ImageField(upload_to='img', default='')  # upload_to指定图片上传的途径，如果不存在则自动创建
    name = models.CharField(max_length=30)
    time = models.DateTimeField(default=time.strftime("%Y-%m-%d %H:%M:%S"))
    delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
