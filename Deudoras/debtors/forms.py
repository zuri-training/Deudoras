from tkinter import Widget
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import School

# Create your forms here.

# class NewSchool(ModelForm):
# 	class Meta:
# 		model = School
# 		fields = ("name","email","CAC","location","Local_government")
# Widgets ={
# 			"name": forms.TextInput(attrs ={'class': 'form_item' ,'id':'SchoolName','label' : 'School Name', 'placeholder':"Ava Memorial College"})
# 			,"email": forms.EmailField(attrs ={'class': 'form_item' ,'id':'SchoolEmail','label' : 'School Email Address', 'placeholder':"Avacollege@yahoo.com"})
# 			,"CAC": forms.TextInput(attrs ={'class': 'form_item'}),
# 			"location": forms.TextInput(attrs ={'class': 'form_item'}),
# 			"Local_government": forms.TextInput(attrs ={'class': 'form_item'})
# 		}
# class NewUserForm(UserCreationForm):
# 	email = forms.EmailField()
# 	name = forms.CharField()
# 	class Meta:
# 		model = models.School
# 		fields = ("username", "email", "password1", "password2")

# 	def save(self, commit=True):
# 		user = super(NewUserForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user