# Generated by Django 3.1.4 on 2020-12-30 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan_service', '0005_loan_interest_rate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='payment_log',
            new_name='PaymentLog',
        ),
    ]
