# Generated by Django 3.1 on 2020-09-07 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClaimsApp', '0013_auto_20200906_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='claims',
            name='Limit_Withdrawal',
            field=models.DateField(auto_now=True),
        ),
    ]