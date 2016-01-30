# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 16:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hhs', '0002_user_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_date', models.DateField()),
                ('swap_after_end', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='house',
            name='contract_end_date',
        ),
        migrations.AddField(
            model_name='house',
            name='lat_long',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hhs.House'),
        ),
        migrations.AddField(
            model_name='contract',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]