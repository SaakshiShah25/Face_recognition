from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .forms import UserCreationForm,NewForm
from django.contrib.auth import logout,get_user_model,authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from logic import recognize
from .models import Account,New,Manual
import csv
import pickle
import pandas as pd
from csv import writer
from django.contrib import messages
from django.contrib.auth.models import auth







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


def idk(d,request):
    new=New.objects.filter(acc=request.user).values_list('subject','division')
    accounts = Account.objects.all().values_list('email', 'username', 'sapid', 'department')
    accounts=request.user
   
    with open(str(accounts.sapid) + '_' + accounts.department +'_' +new[0][0] +'_' + new[0][1] + '.csv', 'w',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Attendance'])
        for key in d.keys():
            f.write("%s, %s\n" % (key,d[key]))
        writer.writerow(['Email', ' UserName', 'SapId', 'Department',])
        accounts = Account.objects.all().values_list('email', 'username', 'sapid', 'department')
        accounts=request.user
        print(accounts)
        writer.writerow([accounts.email,accounts.username,accounts.sapid,accounts.department])
        writer.writerow(['Subject','Division'])
        for xyz in new:
            writer.writerow(xyz)
   

def final_csv(request):
    with open('data.pkl', 'rb') as f:
        mydict = pickle.load(f)
        f.close()
    idk(mydict,request)
    return HttpResponse("Done!")

    

    