# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0010_auto_20170914_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contaminant',
            name='direct_exposure',
        ),
        migrations.AlterField(
            model_name='actionlevel',
            name='dw_toxicity',
            field=models.FloatField(blank=True, verbose_name='Drinking Water Toxicity'),
        ),
        migrations.AlterField(
            model_name='actionlevel',
            name='gw_gross_contamination',
            field=models.FloatField(blank=True, verbose_name='Groundwater Gross Contamination'),
        ),
        migrations.AlterField(
            model_name='actionlevel',
            name='gw_vapor_emissions',
            field=models.FloatField(blank=True, verbose_name='Groundwater Vapor Emissions'),
        ),
    ]
