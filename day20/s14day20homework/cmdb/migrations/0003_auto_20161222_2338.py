# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-22 15:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_application_hosttoapplication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hosttoapplication',
            name='aobj',
        ),
        migrations.RemoveField(
            model_name='hosttoapplication',
            name='hobj',
        ),
        migrations.DeleteModel(
            name='HostToApplication',
        ),
    ]
