from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid


from decimal import Decimal
# Create your models here.

gender_list = (
    ('M', 'Male'), 
    ('F', 'Female')
)

type_list = (
    ('Deposit', 'deposit'),
    ('Withdraw', 'Withdraw')
)

status_list = (
    ('Approved', 'approved'), 
    ('Pending', 'pending'), 
    ('Declined', 'declined')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=23, default='', blank=True)
    last_name = models.CharField(max_length=23, default='', blank=True)
    email = models.EmailField(max_length=50)
    street_address = models.CharField(max_length=150, default='', blank=True)
    city =  models.CharField(max_length = 100, default=False, blank=True)
    state = models.CharField(max_length=30, default= '', blank=True)
    postal_or_zip_code = models.CharField(max_length=6, blank=True)
    profile_pic = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None, null=True)
    signup_confirmation = models.BooleanField(default=False)
    # gender = models.CharField(max_length=10, default = 'Select a gender', blank=True)
    # date_of_birth = models.DateField()
    # phone_number = models.IntegerField(blank=True)
    # country = models.CharField(max_length=13)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        message = 'Thank you for Joining Us, Here is your promised $ 50 !'
        balance = WithdrawalBalance(user=instance, amount=50)
        notification = Notification(user=instance, notification_siginal=True, notification_detail=message)
        balance.save()
        notification.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance,**kwargs):
    instance.profile.save()

class Plans ( models.Model):
    plan_name = models.CharField(max_length=40)
    plan_amount = models.PositiveIntegerField(default='')


class Notification(models.Model):
    notification_id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    notification_siginal = models.BooleanField(default=False)
    notification_detail = models.TextField()
    notification_date_time = models.DateTimeField(auto_now_add=True)
    # optional_amount = models.BigIntegerField(default='')

class WithdrawalBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(default = 0.00, decimal_places=2, max_digits=10)

class TotalDeposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(default = 0.00, decimal_places=2, max_digits=10)

class TotalWithdrawal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.DecimalField(default = 0.00, decimal_places=2, max_digits=10)

class TradingHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_id  = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False)
    transaction_type = models.CharField(max_length=15, choices=type_list)
    amount = models.DecimalField(default = 0.00, decimal_places=2, max_digits=10)
    transaction_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=status_list)  
    # amount_earned = models.PositiveIntegerField(default='233.65')


# credit card
month = []
year = []

for i in range(1, 13):
    months = (i,i)
    month.append(months)

for j in range(20, 25):
    years = (j,j)
    year.append(years)



class BankTransfer(models.Model):
    full_name = models.CharField(max_length=50, default='')
    address = models.TextField()
    routing_number = models.PositiveIntegerField()
    bank_name = models.CharField(max_length=100)
    account_number = models.PositiveIntegerField()
    account_type = models.CharField(max_length=20, help_text='Savings, current, etc')
    swift_code = models.CharField(max_length=15)
    local_currency = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)    
    password = models.CharField(max_length=30, default = '')

class Bitcoin(models.Model):
    bitcoin_address = models.CharField(max_length=40)
    amount = models.DecimalField(max_digits=10, decimal_places=2)    
    password = models.CharField(max_length=30, default = '')


card_brand = (
    ('Master', 'Master'),
    ('Visa', 'Visa'), 
    ('Maestro', 'Maestro'),
    ('Others', 'Others'),
)

card_type = (
    ('Debit', 'Debit'),
    ('Credit', 'Credit')
)
class CreditCard(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    card_name = models.CharField(max_length= 50, default='')
    card_number = models.BigIntegerField()
    card_type = models.CharField(max_length=10, choices=card_type)
    card_company = models.CharField(max_length=25, choices = card_brand)
    month = models.IntegerField(choices=month)
    year = models.IntegerField(choices=year)
    expiry_date = models.IntegerField()
    cvv = models.BigIntegerField()

class Deposit(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Marijuana(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(default = 0.00, decimal_places=2, max_digits=10)

class CrudeOil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(default = 0.00, decimal_places=2, max_digits=10)

class OtherInvestments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(default = 0.00, decimal_places=2, max_digits=10)

class AccountUpgrade(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=True)
    verify = models.BooleanField(default=False, null=True, blank=True)
    front_page  = models.FileField(upload_to='docs/front-page', max_length=100, default='')
    back_page = models.FileField(upload_to='docs/back-page', max_length=100, default='')
