from typing import List
from django.db import models
from django.contrib.auth.models import AbstractUser

from user.manager import UserManager
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    username = None

    USERNAME_FIELD: str = "email"

    REQUIRED_FIELDS: List[str] = ["name"]

    objects = UserManager()