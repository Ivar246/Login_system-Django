from email import message
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request, "authentication/index.html")


def signup(request):
   
   if request.method == "POST":
       user = User.objects.all()
       username = request.POST['username']
       f_name = request.POST['f_name']
       l_name = request.POST['l_name']
       email = request.POST['email']
       password = request.POST['password']
       c_password = request.POST['c_password']
       if password == c_password:
            if user.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('signup')
            elif user.filter(username=username).exists():
                messages.info(request, 'username already exist')
                return redirect('signup')
            else:
                myuser = User.objects.create_user(username, email, password)
                myuser.first_name = f_name 
                myuser.last_name = l_name
                myuser.save();
                messages.success(request, "Your Account has been sucessfully created.")
                return redirect('signin')
       else:
                messages.info(request, "password doesn't match")
                return redirect('signup')
   else:
         return render(request, "authentication/signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.all().values()
        print(user)
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.info(request, 'logged in successfully')
            return redirect('home')
            
        else:
            messages.info(request, 'Bad credentials')
            return  redirect('signin')
    else:  
        return render(request, "authentication/signin.html")


def signout(request):
    logout(request)


def success(request):
    return render(request, 'authentication/success.html')
