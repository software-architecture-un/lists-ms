# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-27 06:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists_ms', '0002_auto_20190527_0502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listplace',
            old_name='place_lat',
            new_name='placeLat',
        ),
        migrations.RenameField(
            model_name='listplace',
            old_name='place_lon',
            new_name='placeLon',
        ),
    ]
