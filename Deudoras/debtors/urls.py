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
    # path('scdashboard',views.school_dasboard, name = 'School dashboard'),
    # path('usdashboard',),
    path('about us', views.about_us, name=' About us'),
    # path('userdashboard',views.user_dashboard,name='User dashboard')

def loginSchool(request):
    return render(request,'debtors/login/login-school')

def loginStudents(request):
    return render(request,'debtors/login/login-students')

def loginUser(request):
    return render(request,'debtors/login/login-user')
]