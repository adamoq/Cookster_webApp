# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-02-02 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0012_auto_20190203_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='avatar',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]