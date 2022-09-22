from django.db import models

class Customers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    isadmin = models.BooleanField(default=False)

class Account(models.Model):
    accountnumber = models.IntegerField(primary_key=True)
    balance = models.DecimalField(max_digits=20,decimal_places=2)
    lastchangedate = models.DateField()
    isactive = models.BooleanField(default=True)
    customers = models.ForeignKey(Customers,related_name='account',on_delete=models.CASCADE)
