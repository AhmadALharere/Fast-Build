# Generated by Django 3.2.25 on 2025-06-22 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0025_auto_20250621_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default='Male', max_length=10),
        ),
    ]
