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




from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

def registerUser(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
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
                return HttpResponse("<h1> Le compte est désactivé  </h1>")
        else:
            message = "Identifiant invalide"
            return render(request, 'login.html', {'message': message})
    else:
        pass
    return render(request, 'login.html')




def logout(request):
    lougouts(request)
    return redirect('home')
