# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-28 06:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists_ms', '0006_auto_20190528_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='estimatedDate',
            field=models.DateField(default=datetime.datetime.now, null=True),
        ),
    ]
