# Generated by Django 3.2.25 on 2025-04-23 05:12

import PcPart.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PcPart', '0002_part_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='Rate',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='part',
            name='image_filename',
            field=models.ImageField(default='', upload_to=PcPart.models.imageSaver),
            preserve_default=False,
        ),
    ]
