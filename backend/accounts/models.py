from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
# Create your models here.


class CustomUser(AbstractBaseUser):
    GENDER_CHOICES = [
        ('male','Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ]
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(choices = GENDER_CHOICES, null=True)
    email = models.EmailField(unique=True)
    last_login = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=15, null=False)
    is_varified = models.BooleanField(default=False)
    bio = models.CharField(max_length=300)

    def __str__(self):
        return self.profile_name
    