# Generated by Django 3.1.4 on 2020-12-29 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_service', '0002_payment_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='last_payment_date',
            field=models.DateField(default=datetime.date(2020, 12, 29)),
        ),
    ]
