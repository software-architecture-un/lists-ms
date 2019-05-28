# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-25 05:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('comment', models.CharField(max_length=2048, null=True)),
                ('estimatedDate', models.DateField()),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ListPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_init', models.FloatField(max_length=30)),
                ('place_end', models.FloatField(max_length=30)),
                ('id_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists_ms.List')),
            ],
        ),
    ]