# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-14 15:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0025_auto_20190814_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_status',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.TicketStatus'),
        ),
    ]
