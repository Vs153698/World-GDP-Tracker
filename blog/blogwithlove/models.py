from django.db import models

# Create your models here.
class Year(models.Model):
    year = models.CharField(max_length=10000,default="",null=True,blank=True)
    def __str__(self):
        return self.year
class Contact(models.Model):
    name = models.CharField(max_length=60,null=True,blank=True,default="")
    email = models.EmailField(null=True,blank=True)
    message= models.TextField(max_length=1000,null=True,blank=True)
    def __str__(self):
        return self.name
