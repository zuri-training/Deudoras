from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Landing, name='home'),
    path('userhome', views.UserHome, name='UserHome'),
   #  path('usersignup', views.UserSignup, name='UserSignup'),
    path('usersignin', views.UserSignin, name='usersignin'),
    path('schoolhome', views.SchoolHome, name='SchoolHome'),
    path('schoolsignup', views.SchoolSignup, name='SchoolSignup'),
   #  path('schoolsignin', views.SchoolSignin, name='schoolsignin'),
    path('signout', views.signout, name='signout'),
    path('help', views.need_help,name='Help'),
    # path('scdashboard',views.school_dasboard, name = 'School dashboard'),
    # path('usdashboard',),
    path('about us', views.about_us, name='About us'),
    # path('userdashboard',views.user_dashboard,name='User dashboard')
path('contact us', views.Contactus, name = 'Contact us'),
 path('loginSchool',views.SchoolSignin, name='Sclogin'),
 path('loginStudent',views.loginStudents , name='Stlogin'),
 path('loginuser',views.loginUser , name='userlogin'),
  path('signupuser1',views.signupuser1 , name='signup1'),
   # path('signupuser2',views.signupuser2 , name='signup2'),
path('schools',views.Schools, name='School list'),
path('debtors',views.Debtors, name='debtors list'),
path('articles',views.Articles, name='Articles'),
]
