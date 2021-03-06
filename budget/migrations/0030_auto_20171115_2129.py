# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 21:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0029_auto_20171115_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Food', '食'), ('Clothing', '衣'), ('Accommodation', '住'), ('Transportation', '行'), ('Education', '育'), ('Entertainment', '樂'), ('Deposit', '存款'), ('Investment', '投資')], default='Food', max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 21, 29, 39, 632563)),
        ),
        migrations.AlterField(
            model_name='incomes',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 15, 21, 29, 39, 632028)),
        ),
    ]
