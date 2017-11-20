from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


cur_date = timezone.now

class model_base(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField(default=0)
    date = models.DateField(default=cur_date)

    def __str__(self):
        return self.name
    
    def update(self):
        pass

    class Meta:
        abstract=True

CHOICES = (
    ("Food", "食"),
    ("Clothing", "衣"),
    ("Accommodation", "住"),
    ("Transportation", "行"),
    ("Education", "育"),
    ("Entertainment", "樂"),
)

class Category(models.Model):
    category = models.CharField(
        max_length=30,
        choices=CHOICES,
        default="Food",
    )
    class Meta:
        abstract=True

class budget_ratio(models.Model):
    ratio = models.FloatField(
        default=0.,
        validators=[MinValueValidator(0.), MaxValueValidator(1.0)]
    )
    class Meta:
        abstract=True

