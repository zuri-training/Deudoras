from tkinter import CASCADE
from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    logo = models.ImageField()
    location = models.TextField()
    CAC = models.IntegerField()
    certificate = models.FileField()

class Debtors(models.Model):
    name = models.CharField(max_length=200)
    student_id = models.IntegerField()
    student_class = models.CharField(max_length=200)
    info = models.TextField()
    school_id = models.ForeignKey(School,on_delete=models.DO_NOTHING)
    amount_owed = models.DecimalField(max_digits=15,decimal_places=2)

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    debtors_id = models.ForeignKey(Debtors,on_delete=models.CASCADE)


class Comment(models.Model):
    school_id = models.ForeignKey(School,on_delete=models.DO_NOTHING)
    comment = models.TextField()
    datetime = models.DateTimeField()
    # section_id = models.ForeignKey(School,on_delete=models.CASCADE)

class Contend(models.Model):
    proof_of_pay = models.FileField()
    details = models.TextField()
    student_id = models.ForeignKey(Debtors,on_delete=models.CASCADE)