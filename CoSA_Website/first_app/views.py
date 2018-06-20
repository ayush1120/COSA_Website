from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from first_app.forms import RegisterForm
# Create your views here.

def index(request):
    logged_in = request.user.is_authenticated
    return render(request, 'first_app\main_page\index.html', {'logged_in':logged_in})

def knowYC(request):
    return render(request, 'first_app\know_your_council\index.html')


def register(request):
    registerForm = RegisterForm()
    errors = None
    if request.method=='POST':
        registerForm = RegisterForm(request.POST)
        
        if registerForm.is_valid():
            user = registerForm.save()
            user.set_password(user.password)
            user.save()
            return redirect('/login/')
        else:
            errors = registerForm.errors.as_data

    return render(request, 'first_app\Register\login.html', {'form':registerForm,
                                                             'errors':errors})


def loginView(request):
    
    if request.user.is_authenticated:
        return redirect('/')

    else:
        error_msg = None
        if(request.method=='POST'):
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                error_msg = 'Login Failed : Invaild Credentials !'

    return render(request, 'first_app/Login/login.html', {'error_msg':error_msg})
