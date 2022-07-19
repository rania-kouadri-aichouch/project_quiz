from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.users, name='users'), #get all users results
    
]
