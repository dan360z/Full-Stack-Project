# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-18 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0049_auto_20190818_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('Bug', 'Bug'), ('Feature', 'Feature')], max_length=7, unique=True),
        ),
    ]
