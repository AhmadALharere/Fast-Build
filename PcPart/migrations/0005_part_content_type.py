# Generated by Django 3.2.25 on 2025-04-26 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('PcPart', '0004_auto_20250424_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='content_type',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
