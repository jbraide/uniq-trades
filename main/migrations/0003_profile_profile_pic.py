# Generated by Django 2.2 on 2020-04-05 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
