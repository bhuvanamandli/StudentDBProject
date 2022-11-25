from django.shortcuts import render
from StudentDBApp.models import Student,Student2
from StudentDBApp import forms
from StudentDBApp.forms import StudentLoginForm

#Create your views here.
def studentview(request):
    studentlist = Student.objects.order_by('marks')
    dict1={'studentlist':studentlist}
    return render(request,'StudentDBApp/students.html',context=dict1);

def student_homepage(request):				#new
    students= Student2.objects.all()
    #students=Student2.objects.filter(marks__lt=35)
    #students=Student2.objects.filter(marks__gt=50)
    #students=Student2.objects.filter(name__startswith='K')
    #students=Student2.objects.all().order_by('marks')  #ASC
    #students=Student2.objects.all().order_by('-marks')   #DESC
    return render(request, 'StudentDBApp/index.html', {'students':students})

def studentinputview(req):
    formObj=forms.StudentForm()
    dict1={'form1':formObj}
    return render(req,'StudentDBApp/input.html',context=dict1)

import time
def studentinputverifyview(req):
    if req.method=='POST':
        formObj=forms.StudentForm(req.POST)
        if formObj.is_valid():
            print("Form-request Validation")
            time.sleep(3)
            print('NAME :',formObj.cleaned_data['name'])
            print('MARKS :',formObj.cleaned_data['marks'])
            formObj = forms.StudentForm()
            dict1={'form1':formObj,'msg':'Data submitted suceesfully...Do you want to enter another data!?'}
    return render(req,'StudentDBApp/input.html',context=dict1)

def studentinputview2(request):
    sentdata=False;
    if request.method=='POST':
        formObj=forms.StudentForm(request.POST)
        if formObj.is_valid():
            print('Form-Request-data Validation Success and printing data')
            time.sleep(5)
            print('Name:',formObj.cleaned_data['name'])
            print('Marks:',formObj.cleaned_data['marks'])
            sentdata=True;
            formObj = forms.StudentForm();            #empty-form
            dict1 = {'form1': formObj, 'sentdata': sentdata}
            return render(request, 'StudentDBApp/thankyou.html', context=dict1);
    formObj=forms.StudentForm();
    dict1={'form1': formObj}
    return render(request,'StudentDBApp/input2.html',context=dict1);

def studentloginpageview(request):
    formObj=StudentLoginForm(); #Empty-form
    dict1={'form1': formObj}
    return render(request,'StudentDBApp/login.html',context=dict1);

def studentloginverifypageview(req):
    sentdata=False
    if req.method=='POST':
        formObj=StudentLoginForm(req.POST)
        if formObj.is_valid():
            print("login-verfication requested")
            print("USERNAME :",formObj.cleaned_data['username'])
            print("PASSWORD :",formObj.cleaned_data['password'])
            username=formObj.cleaned_data['username']
            password=formObj.cleaned_data['password']
            #if username=='sai' and password=='123':
            sentdata=True
            username = formObj.cleaned_data['username']
            dict1={'user':username,'sentdata':sentdata}
            return render(req,'StudentDBApp/loginsucess.html',dict1)
            #else:
                #return render(req,'StudentDBApp/loginunsucess.html')


def feedbackview(request):
    sentdata=False;
    formsObj = forms.FeedBackForm();
    if request.method == 'POST':
        formsObj = forms.FeedBackForm(request.POST);
        if formsObj.is_valid():
            print('Form Validation Success and printing information');
            print('Name:', formsObj.cleaned_data['name'])
            print('Roll No:', formsObj.cleaned_data['rollno'])
            print('Email:', formsObj.cleaned_data['email'])
            print('FeedBack:', formsObj.cleaned_data['feedback'])
            formsObj = forms.FeedBackForm();
            sentdata=True;
    return render(request, 'StudentDBApp/feedback.html', {'form1': formsObj,'sentdata':sentdata});


from StudentDBApp.forms import SignupForm
def signup_form_view(request):
    sentdata = False;
    formsObj=SignupForm();      #empty-form
    if request.method=='POST':
        formsObj=SignupForm(request.POST)       #formobj with submitted-data
        if formsObj.is_valid():
            print('Basic Validation completed and Printing Data...!!!')
            print('Name:',formsObj.cleaned_data['name'])
            print('Password:',formsObj.cleaned_data['password'])
            print('Email:',formsObj.cleaned_data['email'])
            formsObj = SignupForm();  #again-empty-form
            sentdata=True;
    return render(request,'StudentDBApp/signup.html',{'form1':formsObj,'sentdata':sentdata})

