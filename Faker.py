import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','StudentDBProject.settings');
import django
django.setup()

from StudentDBApp.models import Student2;
from faker import Faker;
from random import *;
fakerObj=Faker();

def phonenumbergen():
    d1=randint(6,9)     #6,7,8,9
    num=str(d1)
    for i in range(9):
        num=num+str(randint(0,9))   #0-9 9-times
    print(num)
    return int(num)

def populate(n):
    for i in range(n):
        frollno=fakerObj.random_int(min=1,max=999)
        fname=fakerObj.name()
        fdob=fakerObj.date()
        fmarks=fakerObj.random_int(min=1,max=100)
        femail=fakerObj.email()
        fphonenumber=phonenumbergen();
        faddress=fakerObj.address()
        studentrecord=Student2.objects.get_or_create(rollno=frollno,name=fname,dob=fdob,marks=fmarks,email=femail,phonenumber=fphonenumber,address=faddress)[0]		#[0] not-required

populate(5);