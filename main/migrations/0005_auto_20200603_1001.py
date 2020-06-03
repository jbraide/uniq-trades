# Generated by Django 2.2 on 2020-06-03 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_profile_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=50)),
                ('address', models.TextField()),
                ('routing_number', models.PositiveIntegerField()),
                ('account_number', models.PositiveIntegerField()),
                ('account_type', models.CharField(max_length=20)),
                ('swift_code', models.PositiveIntegerField()),
                ('local_currency', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('password', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Withdraw',
        ),
    ]
