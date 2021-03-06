from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager



# Create your models here.
class MyAccountManager(BaseUserManager):
     def create_user(self,email,username,sapid,department,password=None):
         if not email:
             raise ValueError("Users must have an email address")
         if not username:
             raise ValueError("Users must have a username")
         user=self.model(
             email=self.normalize_email(email),
             username=username,
             sapid=sapid,
             department=department,
             
            
         )
         user.set_password(password)
         user.save(using=self._db)
         return user

     def create_superuser(self,email,username,sapid,department,password):
         user=self.create_user(
             email=self.normalize_email(email),
             username=username,
             password=password,
             sapid=sapid,
             department=department,
             
         )

         user.is_admin=True
         user.is_staff=True
         user.is_superuser=True
         user.save(using=self._db)
         return user


class Account(AbstractBaseUser,PermissionsMixin):
     email=models.EmailField(verbose_name="email",max_length=60,unique=True)
     username=models.CharField(max_length=50,unique=True)
     sapid=models.BigIntegerField()
     department=models.CharField(max_length=30)
     is_admin=models.BooleanField(default=False)
     is_active=models.BooleanField(default=True)
     is_staff=models.BooleanField(default=False)
     is_superuser=models.BooleanField(default=False)


     USERNAME_FIELD='email'
     REQUIRED_FIELDS=['username','sapid','department'
     ]

     objects=MyAccountManager()

     def __str__(self):
         return self.email
     def has_perm(self,perm,obj=None):
         return self.is_admin
     def has_module_perms(self,app_model):
         return True

SUBJECT_CHOICES=(

    ('OSTL','OSTL'),
    ('COA','COA'),
    ('AOAD','AOAD'),
    ('OS','OS'),
    ('MATH','MATH'),
    ('CG','CG'),
  )
DIV_CHOICES=(
    ('SE-A','SE-A'),
    ('SE-B','SE-B'),
    ('TE-A','TE-A'),
    ('TE-B','TE-B'),
)

class New(models.Model):
    subject=models.CharField(choices=SUBJECT_CHOICES,max_length=30,default="")
    division=models.CharField(choices=DIV_CHOICES,max_length=30,default="")
    acc=models.ForeignKey(Account, on_delete=models.CASCADE,default="")
    


