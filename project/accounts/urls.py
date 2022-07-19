from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.registerUser, name='reg'), #registration url
    path('login/', views.login, name='login'), #login url
    path('logout/', views.logout, name='logout'),  #logout url
]
