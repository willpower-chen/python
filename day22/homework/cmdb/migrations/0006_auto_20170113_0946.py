# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-13 01:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0005_userlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlist',
            name='c',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Userlist',
        ),
    ]