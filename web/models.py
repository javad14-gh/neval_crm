from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=255)

class buy_from(models.Model):
    choices = [
        ('store','store'),
        ('site','online')
    ]
    name = models.CharField(max_length=255)
    type = models.CharField(choices=choices,max_length=255)

class orders(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    category = models.ManyToManyField(category)
    amount = models.BigIntegerField()
    text = models.CharField(max_length=255,blank=True)

class changes(models.Model):
    order = models.ManyToManyField(orders)
    date = models.DateField()
    rate = models.IntegerField()
    rial = models.BigIntegerField()
    lir = models.IntegerField()

class buy(models.Model):
    order = models.ManyToManyField(orders)
    date = models.DateField()
    amount = models.BigIntegerField()
    change = models.ManyToManyField(changes)
    buy_from = models.ForeignKey(buy_from,on_delete=models.CASCADE)
    text = models.CharField(max_length=255,blank=True)

class otherCosts(models.Model):
    text = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    date = models.DateField()
    order = models.ManyToManyField(orders)

