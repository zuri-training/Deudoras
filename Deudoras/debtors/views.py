from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from . import forms
# Create your views here.
from imaplib import _Authenticator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import models
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .decorators import not_user,users
# from django.utils.encoding import force_bytes, force_text

from .models import School,Debtors,Debt, Article
# from Deudoras import debtors

# Create your views here.


def Landing(request):
    return render(request, "debtors/index.html")
def SchoolSignup(request):
    
    # if form._
    if request.method == "POST":
        school_name = request.POST.get('SchoolName')
        email = request.POST.get('SchoolEmail')
        location = request.POST.get('SchoolAddress')
        lga = request.POST.get('LGA')
        cac = request.POST.get('SchoolCAC')
        password = request.POST.get('Password')
        print(email)
        # if location != 'gbagada':
    #         messages.error(request, "School is outside our jurisdiction.")
    #         return redirect('home')
    #     if User.objects.filter(email=email.exists()):
    # #         messages.error(request, "Email Already Registered! Try Login Instead")
    # #         return redirect('home')
    #     if password != confirm_password:
    # #         messages.error(request, "Passwords didn't matched!!")
    # #         return redirect('home')
        myuser = School.objects.create(name =school_name ,email = email, password =password,location =location, CAC =cac, Local_government =lga)
        group = Group.objects.get(name ='customer')
        user = group.add(group)
        # School.objects.create(user)
        
        myuser.is_active = True
        myuser.save()

        messages.success(request, 'Your account has been succesfully created')

        return render(request,"debtors/login/login-school.html")

    return render(request,"debtors/signup_school.html")
def add_debtor(request):
    
    # if form._
    if request.method == "POST":
        school_name = request.POST.get('SchoolName')
        email = request.POST.get('SchoolEmail')
        location = request.POST.get('SchoolAddress')
        lga = request.POST.get('LGA')
        cac = request.POST.get('SchoolCAC')
        password = request.POST.get('Password')
        print(email)
        # if location != 'gbagada':
    #         messages.error(request, "School is outside our jurisdiction.")
    #         return redirect('home')
    #     if User.objects.filter(email=email.exists()):
    # #         messages.error(request, "Email Already Registered! Try Login Instead")
    # #         return redirect('home')
    #     if password != confirm_password:
    # #         messages.error(request, "Passwords didn't matched!!")
    # #         return redirect('home')
        myuser = School.objects.create(name =school_name ,email = email, password =password,location =location, CAC =cac, Local_government =lga)
        group = Group.objects.get(name ='customer')
        user = group.add(group)
        # School.objects.create(user)
        
        myuser.is_active = True
        myuser.save()

        messages.success(request, 'Your account has been succesfully created')

        return render(request,"debtors/login/login-school.html")

    return render(request,"debtors/signup_school.html")
def need_help(request):
    return render(request,'debtors/need_help.html')


def about_us(request):
    
    return render(request,'debtors/about us.html')

@login_required
def debt_by_debtor(request,pk):
    debt = Debt.objects.get(debtors_id = pk)
    return render(request,"debtors/debts.html",{'debts':debt})
def SchoolSignin(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            school_name =user.school_name
            login(request, user)
            return render(request, "school_dashboard.html", {'name':school_name})

        else:
            messages.error(request, "Bad credentials!!")
            

        

    return render(request, "login/schoolsignin.html")


def UserSignin(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            username =user.username
            login(request, user)
            return render(request, "debtors/userdashboard.html", {'name':username})

        else:
            messages.error(request, "Bad credentials!!")

        return redirect('landing')


    return render(request, "debtorslogin/usersignin.html")
    








def loginStudents(request):
    return render(request,'debtors/login/login-students.html')

def loginUser(request):
    return render(request,'debtors/login/login-users.html')


def signupuser1(request):
    return render(request, 'debtors/SignUpNormalUser1.html')

def signupuser2(request):
    return render(request, 'debtors/SignUpNormalUser2.html')







def signout(request):
    logout(request)
    messages.success(request, "logged out succesfully")
    return redirect('debtors/index.html')









@users(allowed_roles=['school'])

def SchoolHome(request,pk):
    return  render(request, 'debtors/school_dashboard.html/')
def Debtors(request,pk):
    debtor = Debtors.objects.get(School_id = pk )
    return render(request, 'debtors/debtors_list.html',{'debtors': debtor})
def Schools(request):
    schools = School.objects.all()
    return render(request,'debtors/school_list.html',{'schools': schools})
def debt_by_school(request,pk):
    debt = Debt.objects.get(school_id = pk)
    return render(request,"debtors/debtors.html",{'debts':debt})















@users(allowed_roles=['student'])

def UserHome(request,pk):
    # , pk
    user = Debtors.objects.get(id = pk)
    debt = request.user.Debt.all()
    return render(request,'debtors/dashboard_parents.html',{'debt':debt,'user':user})



    #     
        
    #     
        
    #     
        









    







