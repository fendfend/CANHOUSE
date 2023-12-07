from django.db import models
from datetime import datetime

# Create your models here.
# Field Data Type: char, image, text, boolean, datatime


class Realtor (models.Model):
    name = models.CharField(max_length=200) #shortwords <200
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True) #True represents empty
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False) #mvp=vip
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name