# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-25 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_user_name', models.CharField(max_length=35)),
                ('d_first_name', models.CharField(max_length=35)),
                ('d_last_name', models.CharField(max_length=35)),
                ('d_birth_date', models.CharField(max_length=35)),
                ('d_password', models.CharField(max_length=35)),
            ],
        ),
    ]
