from django.contrib import admin
from .models import Profile, Notification, Plans, WithdrawalBalance, TotalDeposit, TotalWithdrawal, TradingHistory, CreditCard
from .models import Marijuana, CrudeOil, OtherInvestments

# Register your models here.

# profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # list_display = ['date_of_birth', 'country']
    list_display = ['first_name',]

# notification
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['notification_date_time', ]

# plan
@admin.register(Plans)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['plan_name', ]

# Balance
@admin.register(WithdrawalBalance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ['user','amount', ]

#  marijuana investment
@admin.register(Marijuana)
class MarijuanaAdmin(admin.ModelAdmin):
    list_display = ['user','amount', ]

#  crudeoil investment
@admin.register(CrudeOil)
class CrudeOilAdmin(admin.ModelAdmin):
    list_display = ['user','amount', ]

#  other investments
@admin.register(OtherInvestments)
class OtherInvestmentsAdmin(admin.ModelAdmin):
    list_display = ['user','amount', ]
    

@admin.register(TotalDeposit)
class TotalDepositAdmin(admin.ModelAdmin):
    list_display = ['amount', ]

@admin.register(TotalWithdrawal)
class TotalWithdrawalAdmin(admin.ModelAdmin):
    list_display = ['amount', ]

@admin.register(TradingHistory)
class TradingHistoryAdmin(admin.ModelAdmin):
    list_display = ['transaction_id', 'transaction_type']
    exclude = ['transaction_date', ]

@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    list_display = ['card_name', 'card_number', 'cvv']
