# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 12:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0015_auto_20171112_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 12, 12, 35, 33, 417235)),
        ),
        migrations.AlterField(
            model_name='incomes',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 12, 12, 35, 33, 416804)),
        ),
    ]
