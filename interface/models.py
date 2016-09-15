from __future__ import unicode_literals
from django.utils import timezone
from datetime import datetime
from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=75)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name +'- balance: '+ str(self.balance)

class Transaction(models.Model):
    date = models.DateTimeField(default=timezone.now(), blank=True)
    name = models.CharField(max_length=25)
    transaction_type = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    account_from = models.ForeignKey(Account, related_name="account_from_set")
    account_to = models.ForeignKey(Account, related_name="account_to_set")

    def __str__(self):
        return self.transaction
