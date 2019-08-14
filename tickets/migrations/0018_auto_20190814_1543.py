# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-14 14:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0017_auto_20190814_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_status',
            field=models.ForeignKey(default='Open', null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.TicketStatus'),
        ),
    ]
