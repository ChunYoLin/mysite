# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 23:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0023_auto_20171113_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 13, 23, 20, 14, 386483)),
        ),
        migrations.AlterField(
            model_name='incomes',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 13, 23, 20, 14, 385987)),
        ),
    ]