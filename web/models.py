from __future__ import unicode_literals
from django.db import models

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

    def __str__(self):
        return f'{self.date}-{self.user}'

class changes(models.Model):
    order = models.ManyToManyField(orders)
    date = models.DateField()
    rate = models.IntegerField()
    rial = models.BigIntegerField()
    lir = models.IntegerField()

    def __str__(self):
        return f'{self.date}-{self.rate}'

class buy(models.Model):
    order = models.ManyToManyField(orders)
    date = models.DateField()
    amount = models.BigIntegerField()
    change = models.ManyToManyField(changes)
    category = models.ManyToManyField(category)
    buy_from = models.ForeignKey(buy_from,on_delete=models.CASCADE)
    text = models.CharField(max_length=255,blank=True)
    def __str__(self):
        return f'{self.date}-{self.buy_from}-{self.amount}'

class otherCosts(models.Model):
    text = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    date = models.DateField()
    order = models.ManyToManyField(orders)
    def __str__(self):
        return self.text