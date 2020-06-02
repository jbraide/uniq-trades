from django.contrib import admin
from .models import Profile, Notification, Plans, WithdrawalBalance, TotalDeposit, TotalWithdrawal, TradingHistory, CreditCard

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # list_display = ['date_of_birth', 'country']
    list_display = ['first_name',]

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['notification_date_time', ]

@admin.register(Plans)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['plan_name', ]

@admin.register(WithdrawalBalance)
class Admin(admin.ModelAdmin):
    list_display = ['amount', ]

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
    # list_display = ['card_name', 'card_number', 'month', 'year', 'cvv']
    list_display = ['card_name', 'card_number', 'cvv']
