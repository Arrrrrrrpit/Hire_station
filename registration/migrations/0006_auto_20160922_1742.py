# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20160922_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='height_field',
            field=models.IntegerField(default=100, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='width_field',
            field=models.IntegerField(default=100, null=True),
        ),
    ]
