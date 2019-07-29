# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-07-23 05:49
from __future__ import unicode_literals

import bfrs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bfrs', '0027_document_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='other_title',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'Other Document Title'),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='reporting_year',
            field=models.PositiveSmallIntegerField(blank=True, default=bfrs.models.current_finyear, verbose_name=b'Reporting Year'),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='year',
            field=models.PositiveSmallIntegerField(default=bfrs.models.current_finyear, verbose_name=b'Financial Year'),
        ),
        migrations.AlterField(
            model_name='bushfiresnapshot',
            name='reporting_year',
            field=models.PositiveSmallIntegerField(blank=True, default=bfrs.models.current_finyear, verbose_name=b'Reporting Year'),
        ),
        migrations.AlterField(
            model_name='bushfiresnapshot',
            name='year',
            field=models.PositiveSmallIntegerField(default=bfrs.models.current_finyear, verbose_name=b'Financial Year'),
        ),
    ]
