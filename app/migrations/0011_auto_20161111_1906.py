# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 19:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20161111_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squad',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]