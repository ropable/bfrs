# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-09-14 02:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bfrs', '0015_auto_20180903_0929'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bushfire',
            options={'permissions': (('final_authorise_bushfire', 'Can final authorise bushfire'),)},
        ),
    ]
