# Generated by Django 4.2.13 on 2024-06-25 08:10
import sys

import django.core.validators
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):
    dependencies = [
        ('workstation', '0012_alter_datasourceconfig_channels_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='strategyconfig',
            name='over_buy',
            field=models.IntegerField(default='80', validators=[django.core.validators.MinValueValidator(0),
                                                                django.core.validators.MaxValueValidator(100)],
                                      verbose_name='超买阈值'),
        ),
        migrations.AddField(
            model_name='strategyconfig',
            name='over_sell',
            field=models.IntegerField(default='20', validators=[django.core.validators.MinValueValidator(0),
                                                                django.core.validators.MaxValueValidator(100)],
                                      verbose_name='超卖阈值'),
        )
    ]
    if "migrate" in sys.argv:
        db = [arg.split("=")[1] for arg in sys.argv if arg.startswith("--database")]
        if len(db) > 0 and db[0] == "data":
            operations = []
