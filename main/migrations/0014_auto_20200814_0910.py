# Generated by Django 2.2 on 2020-08-14 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200813_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountupgrade',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]