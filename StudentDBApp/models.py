from django.db import models
from django.db import models
#Create your models here.


class Student(models.Model):
    name=models.CharField(max_length=30)
    marks=models.IntegerField()


class Student2(models.Model):       #Faker-data
    rollno=models.IntegerField()
    name=models.CharField(max_length=30)        #single-line-text
    dob=models.DateField()
    marks=models.IntegerField()
    email=models.EmailField()
    phonenumber=models.BigIntegerField()
    address=models.TextField()          #multi-line-text