# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhs', '0003_auto_20160130_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='price',
        ),
        migrations.AddField(
            model_name='contract',
            name='price',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
