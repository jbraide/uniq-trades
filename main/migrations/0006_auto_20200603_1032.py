# Generated by Django 2.2 on 2020-06-03 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200603_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banktransfer',
            name='account_type',
            field=models.CharField(help_text='Savings, current, etc', max_length=20),
        ),
    ]
