# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 21:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20161110_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squad',
            name='baseball1',
        ),
        migrations.RemoveField(
            model_name='squad',
            name='baseball2',
        ),
        migrations.RemoveField(
            model_name='squad',
            name='basketball1',
        ),
        migrations.RemoveField(
            model_name='squad',
            name='basketball2',
        ),
        migrations.RemoveField(
            model_name='squad',
            name='football1',
        ),
        migrations.RemoveField(
            model_name='squad',
            name='football2',
        ),
        migrations.RemoveField(
            model_name='team',
            name='owner',
        ),
        migrations.AddField(
            model_name='team',
            name='squad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Squad'),
        ),
    ]