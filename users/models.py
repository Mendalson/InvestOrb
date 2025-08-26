from django.db import models


# Create your models here.
class User(models.Model):
    Username = models.CharField(max_length=100, unique=True, null=False, blank=False)
    Password = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.Username
