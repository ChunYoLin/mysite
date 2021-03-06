# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 21:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0006_auto_20171102_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.IntegerField(default=0)),
                ('budget', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.Budget')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 9, 21, 59, 40, 752613)),
        ),
        migrations.AlterField(
            model_name='incomes',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 9, 21, 59, 40, 752139)),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
