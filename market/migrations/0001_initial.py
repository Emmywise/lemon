# Generated by Django 3.1.2 on 2021-08-12 21:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('isin', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('limit_price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)])),
                ('side', models.CharField(choices=[('buy', 'buy'), ('sell', 'sell')], max_length=4)),
                ('valid_until', models.IntegerField()),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
    ]
