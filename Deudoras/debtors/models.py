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
<<<<<<< HEAD
    certificate = models.FileField()
=======
    Local_government = models.CharField(max_length=200)
    
>>>>>>> b147aa2d328cd3179d1b4ce213c303b56fb0180d

class Debtors(models.Model):
    name = models.CharField(max_length=200)
    student_id = models.IntegerField()
    student_class = models.CharField(max_length=200)
<<<<<<< HEAD
    info = models.TextField()
    school_id = models.ForeignKey(School,on_delete=models.DO_NOTHING)
    amount_owed = models.DecimalField(max_digits=15,decimal_places=2)

=======
    address = models.CharField(max_length=200)
    school_id = models.ForeignKey(School,on_delete=models.CASCADE)
    contact = models.IntegerField()

class Debt(models.Model):
    School_id = models.ForeignKey(School, on_delete=models.CASCADE)
    debtor_id = models.ForeignKey(Debtors, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    session = models.CharField(max_length=200)
    stclass = models.CharField(max_length=200)
    amount = models.DecimalField( max_digits=12, decimal_places=2)
    term = models.IntegerField()
>>>>>>> b147aa2d328cd3179d1b4ce213c303b56fb0180d
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    debtors_id = models.ForeignKey(Debtors,on_delete=models.CASCADE)


class Comment(models.Model):
    school_id = models.ForeignKey(School,on_delete=models.DO_NOTHING)
    comment = models.TextField()
    datetime = models.DateTimeField()
<<<<<<< HEAD
    # section_id = models.ForeignKey(School,on_delete=models.CASCADE)

class Contend(models.Model):
    proof_of_pay = models.FileField()
    details = models.TextField()
    student_id = models.ForeignKey(Debtors,on_delete=models.CASCADE)
=======
    status = models.CharField(max_length=200)
    proofofpayment = models.FileField()
    debt_id = models.ForeignKey(Debt,on_delete=models.CASCADE)
    

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    poster = models.ForeignKey(School, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField()
    image = models.FileField()
    document = models.FileField()
    summary = models.CharField(max_length=200)
>>>>>>> b147aa2d328cd3179d1b4ce213c303b56fb0180d
