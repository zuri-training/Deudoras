from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    logo = models.ImageField()
    certificate = models.FileField()


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Debtors(models.Model):
    name = models.CharField(max_length=200)
    student = models.IntegerField()
    school_class = models.CharField(max_length=200)
    info = models.TextField()
    school_id = models.ForeignKey(School,on_delete=models.DO_NOTHING)

class Comment(models.Model):
    school_id = models.ForeignKey(School,on_delete=models.DO_NOTHING)
    comment = models.TextField()
    datetime = models.DateTimeField()

class Contend(models.Model):
    proof_of_pay = models.FileField()
    details = models.TextField()