# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 23:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_auto_20171031_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='bank',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='item',
        ),
        migrations.AddField(
            model_name='expenses',
            name='budget',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.Budget'),
        ),
        migrations.AddField(
            model_name='incomes',
            name='budget',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.Budget'),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 10, 31, 23, 43, 42, 767528)),
        ),
        migrations.AlterField(
            model_name='incomes',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 10, 31, 23, 43, 42, 767108)),
        ),
        migrations.DeleteModel(
            name='Transactions',
        ),
    ]
