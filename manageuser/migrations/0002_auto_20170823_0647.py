# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 06:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_auto_20170821_1016'),
        ('users', '0004_auto_20170821_0950'),
        ('manageuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperAdminusers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_status', models.BooleanField(default=False, verbose_name='Active')),
                ('admin_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Users', verbose_name='Admin user')),
                ('company_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='company.Company', verbose_name='Company')),
            ],
        ),
        migrations.AlterField(
            model_name='userpermission',
            name='can_add_employee',
            field=models.BooleanField(default=False, verbose_name='Can add employee'),
        ),
        migrations.AlterField(
            model_name='userpermission',
            name='can_delete_employee',
            field=models.BooleanField(default=False, verbose_name='Can delete employee'),
        ),
        migrations.AlterField(
            model_name='userpermission',
            name='can_edit_employee',
            field=models.BooleanField(default=False, verbose_name='Can edit employee'),
        ),
    ]
