# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-13 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_userlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityname', models.CharField(max_length=32)),
            ],
        ),
        migrations.DeleteModel(
            name='Userlist',
        ),
    ]
