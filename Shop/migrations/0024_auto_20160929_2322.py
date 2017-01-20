# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0023_order_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='session',
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]