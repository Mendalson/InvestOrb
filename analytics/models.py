from django.db import models
from django.conf import settings


class Broker(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Account(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    account_id = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    opened_at = models.DateTimeField(null=True, blank=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Security(models.Model):
    ticker = models.CharField(max_length=32)
    name = models.CharField(max_length=100)
    isin = models.CharField(max_length=12, unique=True)
    type = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.ticker}, {self.isin}"


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    security = models.ForeignKey(Security, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    type = models.CharField(max_length=64)
    quantity = models.DecimalField(max_digits=16, decimal_places=4)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=16, default="RUB")


class Position(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    security = models.ForeignKey(Security, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=16, decimal_places=4)
    average_price = models.DecimalField(max_digits=12, decimal_places=2)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
