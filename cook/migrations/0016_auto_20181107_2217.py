# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-07 21:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cook', '0015_auto_20181107_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantdetail',
            name='users',
        ),
        migrations.AddField(
            model_name='restaurantdetail',
            name='users',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]