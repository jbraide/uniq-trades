# Generated by Django 2.2 on 2020-08-18 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200818_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountupgrade',
            name='back_page',
            field=models.FileField(default='', upload_to='docs/back-page'),
        ),
        migrations.AlterField(
            model_name='accountupgrade',
            name='front_page',
            field=models.FileField(default='', upload_to='docs/front-page'),
        ),
    ]
