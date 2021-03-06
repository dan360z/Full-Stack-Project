# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-13 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password1', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
            ],
        ),
    ]
