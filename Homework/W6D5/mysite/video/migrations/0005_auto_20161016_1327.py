# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 13:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_auto_20161016_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 16, 13, 27, 50, 609349, tzinfo=utc)),
        ),
    ]
