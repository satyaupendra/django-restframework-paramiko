from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class ParamikoModel(models.Model): 
    user_name=models.CharField(max_length=150)
    password=models.CharField(max_length=200)
    ip=models.CharField(max_length=200)
    pathToFile=models.CharField(max_length=200,default="/")
