from distutils.command.upload import upload
from tkinter import CASCADE
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin


# from .forms import NewUserForm

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email,name,password =None):
        user = self.model(email =self.normalize_email(email),
        name =name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,name,password):
        user = self.create_user(email =self.normalize_email(email), 
        name =name )
        user.set_password(password)
        
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
def get_profile_image_filepath(self,filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def get_Contendproof_filepath(self,filename):
    return f'contend_proof/{self.pk}/{"contens_proof.pdf"}'

def get_article_filepath(self,filename):
    return f'article/{self.pk}/{"article.word"}'
def get_article_image_filepath(self,filename):
    return f'article/{self.pk}/{"article.png"}'

def get_default_image():
    return 'jj.png'

class Account(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(verbose_name='email',max_length=60, unique=True,null=True)
    
    name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(verbose_name='date joined' , auto_now_add=True)
    last_login  = models.DateTimeField(verbose_name='last login' , auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    username = None
    objects = MyAccountManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS= ['name']


    def __str__(self):
        return self.name

    def has_perm(self,perm,obj = None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True
    def schools(self,list):
        objects=[]
        for i in list:
            objects.append(Account.object.get(id = i))
        return objects



    
class School(models.Model):
    account = models.OneToOneField(Account,null=True, on_delete= models.CASCADE)
    logo = models.ImageField(upload_to = get_profile_image_filepath)
    location = models.TextField()
    CAC = models.IntegerField()
    certificate = models.FileField()
    Local_government = models.CharField(max_length=200)
    def list(self):
        return School.object.all()
    

class Debtors(models.Model):
    debtor = models.OneToOneField(Account,null=True, on_delete= models.CASCADE)
  
    student_id = models.IntegerField()
    student_class = models.CharField(max_length=200)
    
    info = models.TextField()
    address = models.CharField(max_length=200)
    school_id = models.ForeignKey(School,on_delete=models.CASCADE)
    contact = models.IntegerField()
    def list(self,pk):
        return Debtors.object.get(school_id=pk)

class Debt(models.Model):
    School_id = models.ForeignKey(School, on_delete=models.CASCADE)
    debtor_id = models.ForeignKey(Debtors, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    session = models.CharField(max_length=200)
    stclass = models.CharField(max_length=200)
    amount = models.DecimalField( max_digits=12, decimal_places=2)
    term = models.IntegerField()
    def debtor_sum(self,pk):
        list = Debt.objects.get(debtor_id =pk)
        add = sum(list)
        return add
    def school_sum(self,pk):
        list = Debt.objects.get(debtor_id =pk)
        add = sum(list)
        return add


class User(models.Model):
    name = models.CharField(max_length=200)
    
    password = models.CharField(max_length=200)
    debtors_id = models.ForeignKey(Debtors,on_delete=models.CASCADE)



    # section_id = models.ForeignKey(School,on_delete=models.CASCADE)

class Dispute(models.Model):
    school_id = debtor_id = models.ForeignKey(School,on_delete=models.CASCADE)
    details = models.TextField()
    debtor_id = models.ForeignKey(Debtors,on_delete=models.CASCADE)
    status = models.CharField(max_length=200)
    proofofpayment = models.FileField(upload_to=get_Contendproof_filepath)
    debt_id = models.ForeignKey(Debt,on_delete=models.CASCADE)
    

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    poster = models.ForeignKey(School, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField()
    image = models.FileField(upload_to=get_article_image_filepath)
    document = models.FileField(upload_to=get_article_filepath)
    summary = models.CharField(max_length=200)


class ArticleComments(models.Model):
    id = models.AutoField(primary_key=True)
    school_id = models.ForeignKey(School,on_delete=models.CASCADE)
    comment = models.TextField()
    datetime = models.DateTimeField()
    article_id = models.ForeignKey(Article,on_delete=models.CASCADE)
    status =models.BooleanField()
class DebtorComments(models.Model):
    id = models.AutoField(primary_key=True)
    school_id = models.ForeignKey(School,on_delete=models.CASCADE)
    comment = models.TextField()
    datetime = models.DateTimeField()
    debtor_id = models.ForeignKey(Debtors,on_delete=models.CASCADE)
    status =models.BooleanField()
