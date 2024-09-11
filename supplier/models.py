from django.db import models

# Create your models here.
class supplier(models.Model):
    shopname=models.CharField(max_length=50)
    typeshop=models.CharField(max_length=50)
    empname=models.CharField(max_length=50)
    address=models.TextField()
    