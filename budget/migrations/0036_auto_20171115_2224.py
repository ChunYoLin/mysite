# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 22:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('budget', '0035_auto_20171115_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenses',
            name='LC',
        ),
        migrations.AddField(
            model_name='expenses',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='expenses',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
