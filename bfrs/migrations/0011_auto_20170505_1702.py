# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-05 09:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bfrs', '0010_auto_20170505_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spatialdatahistory',
            name='bushfire',
        ),
        migrations.RemoveField(
            model_name='spatialdatahistory',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='spatialdatahistory',
            name='modifier',
        ),
        migrations.RemoveField(
            model_name='spatialdatahistory',
            name='tenure',
        ),
        migrations.DeleteModel(
            name='SpatialDataHistory',
        ),
    ]