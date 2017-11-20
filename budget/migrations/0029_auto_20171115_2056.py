# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 20:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0028_auto_20171115_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bank',
            name='category',
        ),
        migrations.RemoveField(
            model_name='budget',
            name='category',
        ),
        migrations.RemoveField(
            model_name='debt',
            name='category',
        ),
        migrations.RemoveField(
            model_name='deposit',
            name='category',
        ),
        migrations.RemoveField(
            model_name='expenses',
            name='category',
        ),
        migrations.RemoveField(
            model_name='incomes',
            name='category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.RemoveField(
            model_name='livingcost',
            name='category',
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 20, 56, 33, 510278)),
        ),
        migrations.AlterField(
            model_name='incomes',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 20, 56, 33, 509771)),
        ),
    ]