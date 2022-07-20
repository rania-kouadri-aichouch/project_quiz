from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as lougouts
from django.contrib import messages
from .forms import RegisterForm

def registerUser(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



def login(request):
    
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                django_login(request, user)
                return redirect('home')
            else:
                return HttpResponse("<h1> you account is disabled  </h1>")
        else:
            message = "Invalid username or password"
            return render(request, 'login.html', {'message': message})
    else:
        pass
    return render(request, 'login.html')




def logout(request):
    lougouts(request)
    return redirect('home')
