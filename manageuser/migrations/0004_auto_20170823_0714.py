# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 07:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170821_0950'),
        ('company', '0006_auto_20170821_1016'),
        ('manageuser', '0003_auto_20170823_0658'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='superadminusers',
            unique_together=set([('company_name', 'admin_user')]),
        ),
    ]