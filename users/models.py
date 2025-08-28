from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return self.username
