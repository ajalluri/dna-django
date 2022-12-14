from django.db import models

# Create your models here.

class User(models.Model):
    
    userid = models.CharField(max_length=120,unique=True)
    username = models.CharField(max_length=120,unique=True)
    email = models.EmailField(null=False)
    designation = models.TextField(max_length=1000,null=True)
    skills = models.TextField(max_length=1000,null=True)
  


    