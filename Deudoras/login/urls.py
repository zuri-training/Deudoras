from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('usersignup', views.UserSignup, name='UserSignup'),
    path('usersignin', views.UserSignin, name='usersignin'),
    path('schoolsignup', views.SchoolSignup, name='SchoolSignup'),
    path('schoolsignin', views.SchoolSignin, name='schoolsignin'),
    path('signout', views.signout, name='signout'),

]
