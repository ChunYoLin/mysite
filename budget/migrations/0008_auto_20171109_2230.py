# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 22:30
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0007_auto_20171109_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ratio', models.IntegerField(default=70, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('is_paid', models.BooleanField(default=True)),
                ('budget', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.Budget')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LivingCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ratio', models.IntegerField(default=30, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('value', models.IntegerField(default=0)),
                ('remain', models.IntegerField(default=0)),
                ('budget', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.Budget')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Investment',
        ),
        migrations.AddField(
            model_name='debt',
            name='is_paid',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 9, 22, 30, 28, 256207)),
        ),
        migrations.AlterField(
            model_name='incomes',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 9, 22, 30, 28, 255763)),
        ),
    ]
