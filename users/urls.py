'''Defines URL Patterns for Users'''
from django.urls import path, include
from .import views

app_name = 'users'
urlpatterns = [
    #Include Default Auth Urls.
    path('', include('django.contrib.auth.urls')),
    #Registration Page
    path('register/', views.register, name = 'register'),
]