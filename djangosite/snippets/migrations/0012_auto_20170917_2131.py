# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0011_auto_20170917_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionlevel',
            name='aquatic_ecotoxicity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='actionlevel',
            name='direct_exposure',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='actionlevel',
            name='dw_toxicity',
            field=models.FloatField(blank=True, null=True, verbose_name='Drinking Water Toxicity'),
        ),
        migrations.AlterField(
            model_name='actionlevel',
            name='gw_gross_contamination',
            field=models.FloatField(blank=True, null=True, verbose_name='Groundwater Gross Contamination'),
        ),
        migrations.AlterField(
            model_name='actionlevel',
            name='gw_vapor_emissions',
            field=models.FloatField(blank=True, null=True, verbose_name='Groundwater Vapor Emissions'),
        ),
        migrations.AlterField(
            model_name='actionlevel',
            name='indoor_air',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='actionlevel',
            name='leaching',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='actionlevel',
            name='shallow_soil_vapor',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='actionlevel',
            name='soil_gross_contamination',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='actionlevel',
            name='soil_vapor_emissions',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='actionlevel',
            name='terrestrial_ecotoxicity',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
