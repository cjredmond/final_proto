# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 21:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20161110_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squad',
            name='baseball1',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='baseball1', to='app.Team'),
        ),
        migrations.AlterField(
            model_name='squad',
            name='baseball2',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='baseball2', to='app.Team'),
        ),
        migrations.AlterField(
            model_name='squad',
            name='basketball1',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='basketball1', to='app.Team'),
        ),
        migrations.AlterField(
            model_name='squad',
            name='basketball2',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='basketball2', to='app.Team'),
        ),
        migrations.AlterField(
            model_name='squad',
            name='football1',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='football1', to='app.Team'),
        ),
        migrations.AlterField(
            model_name='squad',
            name='football2',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='football2', to='app.Team'),
        ),
    ]