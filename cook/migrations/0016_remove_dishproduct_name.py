# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-13 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0015_dishproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dishproduct',
            name='name',
        ),
    ]
