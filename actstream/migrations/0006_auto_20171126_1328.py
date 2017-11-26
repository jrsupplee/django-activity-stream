# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0005_auto_20161119_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='action',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]