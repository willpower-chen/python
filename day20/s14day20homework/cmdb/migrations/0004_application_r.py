# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-22 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20161222_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='r',
            field=models.ManyToManyField(to='cmdb.Host'),
        ),
    ]