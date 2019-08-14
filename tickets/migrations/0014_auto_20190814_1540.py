# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-14 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0013_auto_20190814_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('Bug', 'Bug'), ('Feature', 'Feature')], default='Bug', max_length=7, unique=True),
        ),
    ]