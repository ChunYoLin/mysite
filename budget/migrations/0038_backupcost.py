# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 23:41
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0037_auto_20171115_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackupCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.IntegerField(default=0)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('ratio', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('remain', models.IntegerField(default=0)),
                ('budget', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='budget.Budget')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
