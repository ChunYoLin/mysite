from django.db import models
from django.utils import timezone

# Create your models here.

class Budget(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=20)
    value = models.IntegerField(default=0)
    remain = models.IntegerField(default=0)
    budget = models.ForeignKey(
        'Budget',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

class Bank(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Investment(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Incomes(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now())
    bank = models.ForeignKey(
        'Bank',
        on_delete=models.CASCADE,
    )
    budget = models.ForeignKey(
        'Budget',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name

class Expenses(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now())
    bank = models.ForeignKey(
        'Bank',
        on_delete=models.CASCADE,
    )
    item = models.ForeignKey(
        'Item',
        on_delete=models.CASCADE,
    )
    budget = models.ForeignKey(
        'Budget',
        on_delete=models.CASCADE,
        null = True
    )

    def __str__(self):
        return self.name

