# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='test',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='subjects',
            field=models.ManyToManyField(to='main.Subject'),
        ),
    ]
