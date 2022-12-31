import re
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
# Create your views here.

def index(request):
    return render(request,'index.html')
def register(request):
    if request.method=='POST':
        us=request.POST.get('user_name',False)
        fn=request.POST.get('first_name',False)
        ln=request.POST.get('last_name',False)
        p1=request.POST.get('password1',False)
        p2=request.POST.get('password2',False)
        em=request.POST.get('email',False)
        if p1==p2:
            user=User.objects.create_user(username=us,first_name=fn,last_name=ln,email=em,password=p1)
            user.save()
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'password not matching')
            return render(request,'register.html')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        us=request.POST.get('user_name',False)
        pass1=request.POST.get('password1',False)
        user=auth.authenticate(username=us,password=pass1)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')