# Generated by Django 3.2.25 on 2025-04-28 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0009_auto_20250428_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
