# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-12 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_remove_ticket_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='category',
            field=models.TextField(null=True),
        ),
    ]
