from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .forms import UserCreationForm
from django.contrib.auth import logout,get_user_model,authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from logic import recognize


#from logic import haha



# Create your views here.

def home(request):
   # message = haha()
    return render(request,'home.html')

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=UserCreationForm()
    return render(request,'signup.html',{'form':form})
    
  

def login_view(request):
    #user=request.user
    if request.user.is_authenticated:
        return redirect("home")
    if request.POST:
        """
        form=AuthenticationForm(request.POST)
        print(request.POST)
        if form.is_valid():"""
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Stuck here")
            return HttpResponse("Form valid")
        #else:
        return HttpResponse("Form is not valid")
    else:
        form=AuthenticationForm()
        #return HttpResponse("Nothing happened") 
    
    return render(request,'login.html',{'form':form})      

def logout_view(request):
    logout(request)
    return redirect('home')  

def table(request):
    message=recognize()
    return render(request,'table.html',{'message':message})                

