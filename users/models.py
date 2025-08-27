from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, unique=True, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.username
