# Generated by Django 3.1 on 2020-09-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClaimsApp', '0017_auto_20200908_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='claims',
            name='Claim_Extension_Number',
            field=models.CharField(default=0, max_length=50),
        ),
    ]