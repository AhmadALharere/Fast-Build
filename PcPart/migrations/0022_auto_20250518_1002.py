# Generated by Django 3.2.25 on 2025-05-18 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PcPart', '0021_auto_20250518_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpu',
            name='tdp',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='old_power_requirement',
        ),
    ]
