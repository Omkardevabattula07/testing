from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Userprofile
from django.contrib.auth.models import User
common=["1234567890","password","qwerty"]
# Create your views here.
def home(request):
    return render(request,'home.html')
def register_view(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        bio=request.POST['bio']
        profile_pic=request.FILES.get('profile_pic')
        if User.objects.filter(username=username).exists():
            messages.error(request,'username already taken')
            return redirect('register')
        elif password != password2:
            messages.error(request,'passwords dont match')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error (request,"email already taken")
            return redirect('register')
        elif len(password)<10:
            messages.error(request,'Too small password')
            return redirect("register")
        elif password in common:
            messages.error(request,"It is a common password")
            return redirect("register")
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            userprofile=Userprofile(user=user,bio=bio,profile_pic=profile_pic)
            userprofile.save()
            messages.success(request,'Registration successfull')
            return redirect('login')
    return render(request,'register.html')

def login_view(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect('superuser')
            else:
                return redirect('userprofile')
        else:
            return render(request,'login.html',{'error':'invalid credentials'})

    else :
        return render(request,'login.html')
def logout_view(request):
    logout(request)
    return redirect('home')
@login_required
def superuser(request):
    if request.user.is_superuser:
        users=User.objects.all()
        return render(request,'superuser.html',{'users':users})
    else:
        return render (request,'user.html')
@login_required
def userprofile(request):
    users=User.objects.all()
    return render (request,'user.html',{'users':users})
    


