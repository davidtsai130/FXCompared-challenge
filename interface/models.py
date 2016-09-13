from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=75)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name +'- balance: '+ str(self.balance)

class Transaction(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True)
    transaction = models.CharField(max_length=25)
    transaction_type = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    account_from = models.ForeignKey(Account, related_name="account_from")
    account_to = models.ForeignKey(Account, related_name="account_to")
