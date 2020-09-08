# Generated by Django 3.1 on 2020-09-08 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClaimsApp', '0016_auto_20200907_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claims',
            name='Claim_status',
            field=models.CharField(choices=[('NNP', 'NNP'), ('Claim', 'Claim'), ('Claim_Under_Process', 'Claim Under Process'), ('Disputed', 'Disputed'), ('Paid and Closed', 'Paid and Closed'), ('Overdue Cleared', 'Overdue Cleared'), ('Overdue Cleared and Reinstated', 'Overdue Cleared and Reinstated')], default='NNP', max_length=1000),
        ),
    ]
