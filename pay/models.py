from django.db import models

# Create your models here.
class payment(models.Model):
    userid = models.CharField(max_length=30,null=True,default=0)
    
    fullName = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50,null=True)
    sum = models.CharField(max_length=50,null=True)
    pageCode = models.CharField(max_length=30,null=True)
    processId = models.CharField(max_length=30,null=True,default=0)
    processToken = models.CharField(max_length=30,null=True)