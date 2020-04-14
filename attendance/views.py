from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .forms import UserCreationForm,NewForm
from django.contrib.auth import logout,get_user_model,authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from logic import recognize
from .models import Account,New,Manual
import csv
import pandas as pd
from csv import writer
from django.contrib import messages
from django.contrib.auth.models import auth
from bs4 import BeautifulSoup
import requests






# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        username=request.POST['username']
        email=request.POST['email']
        sapid=request.POST['sapid']
        department=request.POST['department']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if username=='' or email=='' or sapid=='' or department=='' or pass1=='' or pass2=='':
            messages.error(request,'Please fill the details correctly!')
            return redirect('signup') 
        if pass1==pass2:
            if Account.objects.filter(username=username).exists() and Account.objects.filter(email=email).exists() and Account.objects.filter(sapid=sapid).exists() and Account.objects.filter(department=department).exists():
                messages.info(request,'Your account already exists!')
                return redirect('home')
            elif Account.objects.filter(username=username).exists():
                messages.info(request,'Username is taken')
                return redirect('signup')
            elif Account.objects.filter(email=email).exists():
                messages.info(request,'Email is taken')
                return redirect('signup')
            else:
                form.save()
                messages.success(request,'Account is created successfully!')
                return redirect('home')
        else:
            messages.error(request,'Passwords not matching!')
            return redirect('signup')
    else:
        form=UserCreationForm()
    return render(request,'signup.html',{'form':form})
    
  

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials!')
            return redirect('login')
    else:
        return render(request,'login.html')      

def logout_view(request):
    logout(request)
    return redirect('home')  

def table(request):
    message=recognize()
    with open('data.csv','a+',newline='') as response:
                writer = csv.writer(response)
                writer.writerow(['Email', ' UserName', 'SapId', 'Department',])
                accounts = Account.objects.all().values_list('email', 'username', 'sapid', 'department')
                accounts=request.user
                writer.writerow([accounts.email,accounts.username,accounts.sapid,accounts.department])
                writer.writerow(['Subject','Division'])
                new=New.objects.filter(acc=request.user).values_list('subject','division')
                for xyz in new:
                    writer.writerow(xyz)
    new=New.objects.filter(acc=request.user)
    context={'message':message,'new':new}
    return render(request,'table.html',context)                

def add(request):
    if request.method=='POST':
        form=NewForm(request.POST)
        if form.is_valid():
            new,created=New.objects.get_or_create(acc=form.cleaned_data['acc'])
            new.subject=request.POST['subject']
            new.division=request.POST['division']
            new.save()
            #mynew=New.objects.filter(acc=request.user)
            messages.success(request,"Details submitted successfully!")
            return redirect('add')
    else:
        form=NewForm()
        mynew=New.objects.filter(acc=request.user)
        if mynew=='':
            context={'form':form}
            return render(request,'add.html',context)
        else:
            context={'form':form,'mynew':mynew}
            return render(request,'add.html',context)

def counter(request):
    if request.method=='POST':
        count=request.POST['count']
    return count


def manage(request):
    #gotcount=counter(request)
    #context={'gotcount':gotcount}
    return render(request,'manual.html')

def remove_data(request):
    Manual.objects.all().delete()
    return render(request,'manual.html')

def manual(request):
    if request.method=='POST':
        sr_no=request.POST['sr_no']
        name=request.POST['name']
        status=request.POST['status']
        manual=Manual(sr_no=sr_no,name=name,status=status)
        manual.save()
        messages.success(request,"Your attendance has been recorded!")
    return render(request,'manual.html')

def update(request):
    with open('data.csv','a+',newline='') as response:
        writer = csv.writer(response)
        manual = Manual.objects.all().values_list('name', 'status')
        for m in manual:
         writer.writerow(m)
    return HttpResponse("Task done!!!")
    
def dict_update(request):
    mdict=mydict
    manual=Manual.objects.all().values_list('name','status')
    for m in manual:
        mdict.update({m[0]:m[1]})
    print(mdict)
    return HttpResponse("Updated Dictionary!!")
    
    