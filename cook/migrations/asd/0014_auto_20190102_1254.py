# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-02 11:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0013_auto_20190102_1253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ['name']},
        ),
    ]
