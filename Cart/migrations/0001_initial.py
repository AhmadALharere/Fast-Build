# Generated by Django 3.2.25 on 2025-04-24 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('PcPart', '0003_auto_20250423_0812'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopBascet',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('total_cost', models.IntegerField(default=0)),
                ('state', models.CharField(choices=[('Waiting', 'Waiting'), ('Ready', 'Ready'), ('Done', 'Done'), ('Canceled', 'Canceled'), ('Rejected', 'Rejected')], default='Waiting', max_length=10)),
                ('compitability', models.CharField(choices=[('safe', 'safe'), ('warning', 'warning'), ('Danger', 'Danger'), ('Undefined', 'Undefined')], default='Undefined', max_length=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('bascet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cart.shopbascet')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PcPart.part')),
            ],
        ),
        migrations.CreateModel(
            name='Descount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('quantity', models.PositiveIntegerField()),
                ('is_quantity_limit', models.BooleanField()),
                ('is_dated_limit', models.BooleanField()),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PcPart.part')),
            ],
        ),
    ]
