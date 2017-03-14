# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-14 04:57
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bfrs', '0011_bushfire_archive'),
    ]

    operations = [
        migrations.AddField(
            model_name='bushfire',
            name='dispatch_aerial',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bushfire',
            name='dispatch_pw',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='incident_no',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999)], verbose_name=b'Fire Number'),
        ),
    ]
