from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

from budget.base import *


class Budget(model_base):
    pass

class Debt(model_base):
    remain = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False)
    expenses = GenericRelation("Expenses")
    budget = models.ForeignKey(
            'Budget',
            on_delete=models.CASCADE,
            null=True
    )

class Deposit(model_base, budget_ratio):
    budget = models.ForeignKey(
            'Budget',
            on_delete=models.CASCADE,
            null=True
    )
    income = models.OneToOneField(
            'Incomes',
            on_delete=models.CASCADE,
            null=True
    )
    
    def update(self, *args, **kwargs):
        r = self.income.remain
        self.value = int(r*(self.ratio))
        self.name = "存款_{}".format(self.income.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
class LivingCost(model_base, budget_ratio):
    expenses = GenericRelation("Expenses")
    remain = models.IntegerField(default=0)
    budget = models.ForeignKey(
            'Budget',
            on_delete=models.CASCADE,
            null=True
    )

    def update(self, *args, **kwargs):
        self.value = 0
        for i in self.budget.incomes_set.all():
            self.value += i.remain 
        self.value *= self.ratio
        self.value = int(self.value)
        self.remain = self.value
        for ex in self.expenses.all():
            self.remain -= ex.value

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class BackupCost(model_base, budget_ratio):
    expenses = GenericRelation("Expenses")
    remain = models.IntegerField(default=0)
    budget = models.ForeignKey(
            'Budget',
            on_delete=models.CASCADE,
            null=True
    )

    def update(self, *args, **kwargs):
        self.value = 0
        for i in self.budget.incomes_set.all():
            self.value += i.remain 
        self.value *= self.ratio
        self.value = int(self.value)
        self.remain = self.value
        for ex in self.expenses.all():
            self.remain -= ex.value

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Bank(model_base):
    pass

class Incomes(model_base):
    remain = models.IntegerField(default=0)
    bank = models.ForeignKey(
        'Bank',
        on_delete=models.CASCADE,
    )
    budget = models.ForeignKey(
        'Budget',
        on_delete=models.CASCADE,
    )

class Expenses(model_base, Category):
    bank = models.ForeignKey(
        'Bank',
        on_delete=models.CASCADE,
    )
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    belong_to = GenericForeignKey('content_type', 'object_id')
    budget = models.ForeignKey(
        'Budget',
        on_delete=models.CASCADE,
    )

