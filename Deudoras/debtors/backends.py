import email
from django.contrib.auth.backends import ModelBackend
from .models import Account


class accountbackend(ModelBackend):
    def authenticate(self, request, email,password):
        
        try:
            account = Account.objects.get(email=email,password=password)
            
            return account
        except Account.DoesNotExist:
            pass