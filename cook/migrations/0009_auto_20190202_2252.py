# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-02-02 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0008_auto_20190202_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='avatar',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]