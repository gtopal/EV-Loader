# Generated by Django 3.1 on 2020-12-11 20:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Name')),
                ('cost', models.FloatField(blank=True, default=0, null=True, verbose_name='Cost')),
                ('sku', models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator(message='8 characters required', regex='^.{8}$')], verbose_name='Sku')),
            ],
        ),
    ]
