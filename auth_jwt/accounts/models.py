from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    full_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=25)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []