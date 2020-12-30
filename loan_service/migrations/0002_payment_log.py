# Generated by Django 3.1.4 on 2020-12-29 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField()),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('interest_since_last_payment', models.DecimalField(decimal_places=2, max_digits=20)),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan_service.loan')),
            ],
        ),
    ]
