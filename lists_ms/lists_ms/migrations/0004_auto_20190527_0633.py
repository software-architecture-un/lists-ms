# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-27 06:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists_ms', '0003_auto_20190527_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listplace',
            name='id_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='lists_ms.List'),
        ),
    ]
