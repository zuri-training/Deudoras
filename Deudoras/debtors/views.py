from django.shortcuts import render


# Create your views here.
from imaplib import _Authenticator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from geeksforgeeks import settings
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from . tokens import generate_token
# from django.utils.encoding import force_bytes, force_text



# Create your views here.

def Landing(request):
    return render(request, "index.html")


def SchoolHome(request):
    return render(request, "login/school.html")


def UserHome(request):
    return render(request, "login/user.html")


def SchoolSignup(request):
    
    if request.method == "POST":
        school_name = request.POST['schoolname']
        email = request.POST['email']
        location = request.POST['location']
        registration_number = request.POST['registration number']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']

        if location != 'gbagada':
            messages.error(request, "School is outside our jurisdiction.")
            return redirect('home')
        
        if User.objects.filter(email=email.exists()):
            messages.error(request, "Email Already Registered! Try Login Instead")
            return redirect('home')
        
        if password != confirm_password:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        

        myuser = User.objects.create_user(school_name, email, password)
        
        myuser.is_active = True
        myuser.save()

        messages.success(request, 'Your account has been succesfully created')

        return redirect('schoolsignin')


    return render(request, 'login/SchoolSignup.html')


def UserSignup(request):
    
    if request.method == "POST":
        username = request.POST['username']
        user_email = request.POST['user_email']
        debtors_id = request.POST['debtors_id']
        user_password = request.POST['password1']
        confirm_user_password = request.POST['password2']
        

        if User.objects.filter(username=username.exists()):
            messages.error(request, "Username Already Registered! Try a different one.")
            return redirect('landing')

        if User.objects.filter(user_email=user_email.exists()):
            messages.error(request, "Email Already Registered! Try Login instead")
            return redirect('landing')
        
        if user_password != confirm_user_password:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('landing')
        

        myuser = User.objects.create_user(username, user_email, user_password)
        
        myuser.is_active = True
        myuser.save()

        messages.success(request, 'Your account has been succesfully created')

        return redirect('usersignin')


    return render(request, 'login/UserSignup.html')


def SchoolSignin(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass1']

        user = authenticate(email=email, password=password)

        if user is not None:
            school_name =user.school_name
            login(request, user)
            return render(request, "login/landing.html", {'name':school_name})

        else:
            messages.error(request, "Bad credentials!!")
            return redirect('landing')

        return redirect('landing')


    return render(request, "login/schoolsignin.html")
    

def UserSignin(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password1']

        user = authenticate(email=email, password=password)

        if user is not None:
            username =user.username
            login(request, user)
            return render(request, "login/landing.html", {'name':username})

        else:
            messages.error(request, "Bad credentials!!")
            return redirect('landing')

        return redirect('landing')


    return render(request, "login/usersignin.html")



def signout(request):
    logout(request)
    messages.success(request, "logged out succesfully")
    return redirect('home')