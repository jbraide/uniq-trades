# Generated by Django 2.2 on 2020-08-19 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BankTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=50)),
                ('address', models.TextField()),
                ('routing_number', models.PositiveIntegerField()),
                ('bank_name', models.CharField(max_length=100)),
                ('account_number', models.PositiveIntegerField()),
                ('account_type', models.CharField(help_text='Savings, current, etc', max_length=20)),
                ('swift_code', models.CharField(max_length=15)),
                ('local_currency', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('password', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Bitcoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bitcoin_address', models.CharField(max_length=40)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('password', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('card_name', models.CharField(default='', max_length=50)),
                ('card_number', models.BigIntegerField()),
                ('card_type', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], max_length=10)),
                ('card_company', models.CharField(choices=[('Master', 'Master'), ('Visa', 'Visa'), ('Maestro', 'Maestro'), ('Others', 'Others')], max_length=25)),
                ('month', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])),
                ('year', models.IntegerField(choices=[(20, 20), (21, 21), (22, 22), (23, 23), (24, 24)])),
                ('expiry_date', models.IntegerField()),
                ('cvv', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=40)),
                ('plan_amount', models.PositiveIntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='WithdrawalBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TradingHistory',
            fields=[
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(choices=[('Deposit', 'deposit'), ('Withdraw', 'Withdraw')], max_length=15)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('transaction_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Approved', 'approved'), ('Pending', 'pending'), ('Declined', 'declined')], max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TotalWithdrawal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TotalDeposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=23)),
                ('last_name', models.CharField(blank=True, default='', max_length=23)),
                ('email', models.EmailField(max_length=50)),
                ('street_address', models.CharField(blank=True, default='', max_length=150)),
                ('city', models.CharField(blank=True, default=False, max_length=100)),
                ('state', models.CharField(blank=True, default='', max_length=30)),
                ('postal_or_zip_code', models.CharField(blank=True, max_length=6)),
                ('profile_pic', models.ImageField(null=True, upload_to='images/')),
                ('signup_confirmation', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OtherInvestments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notification_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('notification_siginal', models.BooleanField(default=False)),
                ('notification_detail', models.TextField()),
                ('notification_date_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Marijuana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CrudeOil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccountUpgrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verify', models.BooleanField(blank=True, default=False, null=True)),
                ('front_page', models.FileField(default='', upload_to='docs/front-page')),
                ('back_page', models.FileField(default='', upload_to='docs/back-page')),
                ('user', models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
