# Generated by Django 3.1 on 2020-09-13 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClaimsApp', '0004_auto_20200913_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditlimits',
            name='Address',
            field=models.CharField(default=0, max_length=200),
        ),
    ]