# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20170328_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='main.Subject'),
        ),
    ]
