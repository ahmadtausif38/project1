from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

         #Password Checking
        if password1!=password2: 
            messages.error(request,"Password and Confirm Password Doesn't Match...!!")
            return redirect("register")

        #Username Matching
        if User.objects.filter(username=username).exists():
             messages.info(request,"This Username Already taken...!")
             return redirect("register")

        #Email Matching
        if User.objects.filter(email=email).exists():
            messages.info(request,"Email Already Registerd..!")
            return redirect("register")
        user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email, password= password1)
        user.save()
        messages.success(request,"Your Account Created Successfully..Back to login")
        return redirect("register")
    else:    
        return render(request,'register.html')

def login1(request):
    if request.method=='POST': 
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/index')
        else:
            messages.error(request,"Invalid Credential..!")
            return redirect('login')
    return redirect('login')

def LogOut(request):
    auth.logout(request)
    messages.success(request,"Successfully Logout..!")
    return redirect('login')