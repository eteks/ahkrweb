# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 07:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170821_0950'),
        ('manageuser', '0004_auto_20170823_0714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adminusers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_status', models.BooleanField(default=False, verbose_name='Active')),
                ('admin_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_user', to='users.Users', verbose_name='Admin user')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Users', verbose_name='Manager')),
            ],
            options={
                'verbose_name_plural': 'Admin',
            },
        ),
        migrations.CreateModel(
            name='Managerusers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_status', models.BooleanField(default=False, verbose_name='Active')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_user', to='users.Users', verbose_name='Employee')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Users', verbose_name='Manager')),
            ],
            options={
                'verbose_name_plural': 'Manager',
            },
        ),
        migrations.AlterModelOptions(
            name='superadminusers',
            options={'verbose_name_plural': 'SuperAdmin'},
        ),
        migrations.AlterUniqueTogether(
            name='managerusers',
            unique_together=set([('manager', 'employee')]),
        ),
        migrations.AlterUniqueTogether(
            name='adminusers',
            unique_together=set([('admin_user', 'manager')]),
        ),
    ]
