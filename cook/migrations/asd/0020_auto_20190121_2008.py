# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-21 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0019_auto_20190120_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantdetail',
            name='autoorder',
            field=models.CharField(choices=[('0', 'active'), ('1', 'notactive')], default='0', max_length=1),
        ),
        migrations.AddField(
            model_name='restaurantdetail',
            name='takeaway',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('0', 'waiter'), ('1', 'cook'), ('2', 'provaider'), ('3', 'supplier')], max_length=1),
        ),
    ]
