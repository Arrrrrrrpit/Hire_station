# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 04:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0012_auto_20160915_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdetails',
            name='company_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='details',
            field=models.CharField(max_length=100000, primary_key=True, serialize=False),
        ),
    ]
