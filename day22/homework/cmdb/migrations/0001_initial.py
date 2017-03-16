# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-12 21:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32)),
                ('code', models.CharField(default='SA', max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(db_index=True, max_length=32)),
                ('ip', models.GenericIPAddressField(db_index=True)),
                ('port', models.IntegerField()),
                ('b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Business')),
            ],
        ),
        migrations.CreateModel(
            name='Userlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(default='123456', max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='r',
            field=models.ManyToManyField(to='cmdb.Host'),
        ),
    ]