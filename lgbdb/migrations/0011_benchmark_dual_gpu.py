# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lgbdb', '0010_auto_20160201_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='benchmark',
            name='dual_gpu',
            field=models.CharField(choices=[(b'None', b'None'), (b'SLI', b'SLI (NVidia)'), (b'Crossfire', b'Crossfire (AMD)')], default='None', max_length=50),
        ),
    ]
