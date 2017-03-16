# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-13 01:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0006_auto_20170113_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityname', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Userlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(default='123456', max_length=32)),
                ('email', models.CharField(max_length=32)),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.City')),
            ],
        ),
    ]
