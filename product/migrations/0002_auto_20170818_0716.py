# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='boxcount',
            field=models.IntegerField(null=True, verbose_name='Box count'),
        ),
        migrations.AlterField(
            model_name='product',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/product'),
        ),
    ]