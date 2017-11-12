from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

    
class model_base(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract=True

class Budget(model_base):
    date = models.DateField()

class Debt(model_base):
    value = models.IntegerField(default=0)
    remain = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False)
    budget = models.ForeignKey(
            'Budget',
            on_delete=models.CASCADE,
            null=True
    )

class Deposit(model_base):
    ratio = models.IntegerField(
        default=70,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    value = models.IntegerField(default=0)
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
    def save(self, *args, **kwargs):
        r = self.income.remain
        self.value = int(r*(self.ratio/100.))
        self.name = "存款_{}".format(self.income.name)
        super().save(*args, **kwargs)
    
class LivingCost(model_base):
    ratio = models.IntegerField(
        default=30,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    value = models.IntegerField(default=0)
    remain = models.IntegerField(default=0)
    budget = models.ForeignKey(
            'Budget',
            on_delete=models.CASCADE,
            null=True
    )
    def save(self, *args, **kwargs):
        self.value = 0
        for i in self.incomes_set.all():
            self.value += i.remain 
        self.value *= (self.ratio/100.)
        self.remain = self.value
        for ex in self.expenses_set.all():
            self.remain -= ex.value
        super().save(*args, **kwargs)
    
class Item(model_base):
    value = models.IntegerField(default=0)
    remain = models.IntegerField(default=0)
    budget = models.ForeignKey(
        'Budget',
        on_delete=models.CASCADE,
    )

class Bank(model_base):
    value = models.IntegerField(default=0)

class Incomes(model_base):
    value = models.IntegerField(default=0)
    remain = models.IntegerField(default=0)
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
    livingcost = models.ForeignKey(
        'LivingCost',
        on_delete=models.CASCADE,
        null=True
    )

class Expenses(model_base):
    value = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now())
    bank = models.ForeignKey(
        'Bank',
        on_delete=models.CASCADE,
    )
    item = models.ForeignKey(
        'LivingCost',
        on_delete=models.CASCADE,
    )
    budget = models.ForeignKey(
        'Budget',
        on_delete=models.CASCADE,
        null = True
    )

