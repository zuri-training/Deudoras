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

def home(request):
    return render(request, "login/index.html")


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

    return render(request, 'login/schoolsignin.html')


def UserSignup(request):
    
    if request.method == "POST":
        username = request.POST['username']
        user_email = request.POST['user_email']
        debtors_id = request.POST['debtors_id']
        user_password = request.POST['password1']
        confirm_user_password = request.POST['password2']
        

        if User.objects.filter(username=username.exists()):
            messages.error(request, "Username Already Registered! Try a different one.")
            return redirect('home')

        if User.objects.filter(user_email=user_email.exists()):
            messages.error(request, "Email Already Registered! Try Login instead")
            return redirect('home')
        
        if user_password != confirm_user_password:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        

        myuser = User.objects.create_user(username, user_email, user_password)
        
        myuser.is_active = True
        myuser.save()

        messages.success(request, 'Your account has been succesfully created')

    return render(request, 'login/usersignin.html')


# def activate(request,uidb64,token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         myuser = User.objects.get(pk=uid)
#     except (TypeError,ValueError,OverflowError,User.DoesNotExist):
#         myuser = None

#     if myuser is not None and generate_token.check_token(myuser, token):
#         myuser.is_active = True
#         # user.profile.signup_confirmation = True
#         myuser.save()
#         login(request,myuser)
#         messages.success(request, "Your Account has been activated!!")
#         return redirect('signin')
#     else:
#         return render(request,'activation_failed.html')



def SchoolSignin(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass1']

        user = authenticate(email=email, password=password)

        if user is not None:
            name =user.name
            login(request, user)
            return render(request, "login/index.html", {'name':name})

        else:
            messages.error(request, "Bad credentials!!")
            return redirect('home')

    return render(request, "login/schoolsignin.html")
    

def UserSignin(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password1']

        user = authenticate(email=email, password=password)

        if user is not None:
            name =user.name
            login(request, user)
            return render(request, "login/index.html", {'name':name})

        else:
            messages.error(request, "Bad credentials!!")
            return redirect('home')

    return render(request, "login/usersignin.html")



def signout(request):
    logout(request)
    messages.success(request, "logged out succesfully")
    return redirect('home')

