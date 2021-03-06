# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 13:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0018_auto_20171112_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='incomes',
            name='livingcost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.LivingCost'),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 12, 13, 4, 5, 673327)),
        ),
        migrations.AlterField(
            model_name='incomes',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 12, 13, 4, 5, 672261)),
        ),
    ]
