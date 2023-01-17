from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from hashlib import sha1
from time import time

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class buy_from(models.Model):
    choices = [
        ('store','store'),
        ('site','site')
    ]
    name = models.CharField(max_length=255)
    type = models.CharField(choices=choices,max_length=255)

    def __str__(self):
        return f'{self.name}-{self.type}'

class customers(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class orders(models.Model):
    user = models.ForeignKey(customers,on_delete=models.CASCADE)
    date = models.DateField()
    category = models.ManyToManyField(category)
    amount = models.BigIntegerField()
    text = models.CharField(max_length=255,blank=True)
    s = str(int(sha1(str(time()).encode("utf-8")).hexdigest(), 16) % (10 ** 8))
    followCode = models.CharField(default=s,auto_created=True,unique=True,max_length=255,editable=False)
    def __str__(self):
        return self.followCode

class changes(models.Model):
    order = models.ManyToManyField(orders)
    date = models.DateField()
    rate = models.IntegerField()
    rial = models.BigIntegerField()
    lir = models.IntegerField()
    

    def __str__(self):
        return f'{self.rate}'

class buy(models.Model):
    order = models.ManyToManyField(orders)
    date = models.DateField()
    amount = models.IntegerField()
    change = models.ManyToManyField(changes)
    category = models.ManyToManyField(category)
    buy_from = models.ForeignKey(buy_from,on_delete=models.CASCADE)
    text = models.CharField(max_length=255,blank=True)
    def __str__(self):
        return f'{self.date}-{self.buy_from}-{self.amount}'
    @property
    def sud(self):
        return self.amount * 0.3

class otherCosts(models.Model):
    text = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    date = models.DateField()
    order = models.ManyToManyField(orders)
    def __str__(self):
        return self.text