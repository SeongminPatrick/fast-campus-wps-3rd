# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='youtubeuser',
            options={'verbose_name': '사용자', 'verbose_name_plural': '사용자 목록'},
        ),
        migrations.AddField(
            model_name='youtubeuser',
            name='nickname',
            field=models.CharField(max_length=24, null=True),
        ),
    ]