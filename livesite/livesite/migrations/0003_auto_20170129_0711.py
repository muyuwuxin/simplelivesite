# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livesite', '0002_auto_20170129_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='describe',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='id_card',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='title',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
