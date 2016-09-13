# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Application_text', models.CharField(max_length=100000)),
                ('pay_expected', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='job_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_id', models.IntegerField()),
                ('details', models.CharField(max_length=100000)),
                ('pay', models.CharField(max_length=50)),
                ('deadline', models.DateTimeField(verbose_name=b'Date to complete the project till')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('company_name', models.ForeignKey(to='registration.job_provider')),
            ],
        ),
        migrations.AddField(
            model_name='job_application',
            name='job_id',
            field=models.ForeignKey(to='registration.job_details'),
        ),
    ]
