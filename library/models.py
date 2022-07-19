from re import I
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime,timedelta
from django.contrib.auth.models import PermissionsMixin ,AbstractBaseUser
from .manager import CustomUserManager

class MyUser(AbstractBaseUser, PermissionsMixin):
    username = None 
    email = models.EmailField('Email address',
                                unique = True,
                                error_messages = {
                                   'unique': 'This email already exists.'
                              })
    first_name = models.CharField('First name',
                            blank = False,
                            max_length = 50)
    last_name = models.CharField('Last name',
                            blank = False,
                            max_length = 50)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager() 
    
    def __str__(self):
        return self.email


class Book(models.Model):
    catchoice= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biography'),
        ('history', 'History'),
        ('novel', 'Novel'),
        ('fantasy', 'Fantasy'),
        ('thriller', 'Thriller'),
        ('romance', 'Romance'),
        ('scifi','Sci-Fi')
        ]
    name=models.CharField(max_length=30)
    isbn=models.PositiveIntegerField()
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=30,choices=catchoice,default='education')
    def __str__(self):
        return str(self.name)+"["+str(self.isbn)+']'


def get_expiry():
    return datetime.today() + timedelta(days=15)

    

