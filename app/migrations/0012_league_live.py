# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20161111_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='live',
            field=models.BooleanField(default=False),
        ),
    ]
