
from django.http import HttpResponse
from django.shortcuts import render

      
def landing(request):
    return render(request,'landing.html')


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'aboutus.html')
