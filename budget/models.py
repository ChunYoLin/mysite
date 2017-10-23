from django.db import models

# Create your models here.

class Budget(models.Model):
    Budget_name = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.Budget_name

class Item(models.Model):
    budget = models.ForeignKey(
        'Budget',
        on_delete=models.CASCADE,
    )
    Item_name = models.CharField(max_length=20)
    Description = models.CharField(max_length=200)
    Value = models.IntegerField(default=0)

    def __str__(self):
        return self.Item_name
