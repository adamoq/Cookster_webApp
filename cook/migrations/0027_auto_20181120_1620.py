# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-20 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0026_product_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookOrderTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='cooktask',
            name='orders',
        ),
        migrations.AlterField(
            model_name='cookorder',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='cook.Product'),
        ),
        migrations.AddField(
            model_name='cookordertask',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to='cook.CookOrder'),
        ),
        migrations.AddField(
            model_name='cookordertask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to='cook.CookTask'),
        ),
        migrations.AddField(
            model_name='cooktask',
            name='cookorders',
            field=models.ManyToManyField(related_name='orders', through='cook.CookOrderTask', to='cook.CookOrder'),
        ),
    ]