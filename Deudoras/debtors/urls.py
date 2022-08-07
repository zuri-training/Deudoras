from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Landing, name='landing'),
    path('userhome', views.UserHome, name='UserHome'),
    path('usersignup', views.UserSignup, name='UserSignup'),
    path('usersignin', views.UserSignin, name='usersignin'),
    path('schoolhome', views.SchoolHome, name='SchoolHome'),
    path('schoolsignup', views.SchoolSignup, name='SchoolSignup'),
    path('schoolsignin', views.SchoolSignin, name='schoolsignin'),
    path('signout', views.signout, name='signout'),
    path('help', views.need_help,name='Help'),

]