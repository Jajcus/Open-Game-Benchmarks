# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lgbdb', '0004_auto_20160126_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benchmark',
            name='additional_notes',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='benchmark',
            name='fps_data',
            field=models.CommaSeparatedIntegerField(default='', max_length=1500),
        ),
    ]
