# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 10:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_studentconnectexercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentConnectSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['subject_code']},
        ),
        migrations.AddField(
            model_name='studentconnectsubject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Subject'),
        ),
        migrations.AddField(
            model_name='studentconnectsubject',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
