from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# messages
from django.contrib import messages

# registration activation and confirm link
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.db import IntegrityError
from django.db.models import Sum

# forms
from .forms import RegistrationForm, BankTransferForm, CreditCardForm, DepositForm, ProfileForm, CreditCardForm, BitcoinForm

# registration token 
from .token import account_activation_token

# importing models 
from .models import TradingHistory, Profile,WithdrawalBalance, TotalDeposit, TotalWithdrawal, Notification, Plans, BankTransfer, Notification

# background task 
# from background_task import background

# updater 
from .updater import autoincr

import requests
import time
from random import randint

def index(request):
    return render(request, 'main/index.html')

# activation sent view 
def activation_sent_view(request):
    return render(request, 'registration/activation_sent.html')

# activation view
def activate(request, uidb64, token):
    print(uidb64)
    try:
        uid = uidb64
        # uid = force_text(urlsafe_base64_encode(uidb64))
        user = User.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        print('Im the error')

    # checking if the user exists, if token is valid
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true
        user.is_active = True

        # set sign_up confirmation to  true 
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)

        return redirect('main:dashboard')
    
    else:
        return render(request, 'registration/activation_invalid.html')

# registration
def signup_view(request):

    if request.method == 'POST':
        # profile = Profile.objects.get(user = request.user)
        # form = RegistrationForm(request.POST, instance=profile)

        form  = RegistrationForm(request.POST)
        # profile = ProfileForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            # inserting profile data to the user data 
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email') 
            
            # user.is_active = False
            # save user to the database
            user.save()
            
            # test login

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')            
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main:dashboard')
            


            # current_site = get_current_site(request)
            # subject = 'Activate your UniqTrades Account'
            # message = render_to_string('registration/account_activation_email.html',{
            #     'user': user, 
            #     'domain': current_site, 
            #     # 'uid': urlsafe_base64_encode(force_bytes(user.pk)), 
            #     'uid': user.pk, 
            #     'token': account_activation_token.make_token(user)
            # })
            # user.email_user(subject, message) 
            # return redirect('main:activation_sent')
    
    else:
        form = RegistrationForm()
        # profile = ProfileForm()

    context = {
        'form': form,
        # 'profile':profile,
    }
    return render(request, 'registration/register.html', context)



# dashboard
@login_required(login_url='/login')
def dashboard(request):
    # request the user in the session
    user = request.user

    # balance
    balance = WithdrawalBalance.objects.filter(user=user).aggregate(amount=Sum('amount'))
    total_deposits = TotalDeposit.objects.all()
    total_withdrawals = TotalWithdrawal.objects.all()

    # Notification
    notification = Notification.objects.all().filter(user=user).order_by('-notification_date_time')

    context = {
        'balance': balance, 
        'total_deposits': total_deposits, 
        'total_withdrawals': total_withdrawals, 
        'notification': notification, 
    }
    return render(request, 'main/dashboard.html', context)


# line chart

from django.http import JsonResponse

def crypto_chart(request):
    # data = []
    data = ''


    time.sleep(1)
    api_url = 'https://api.alternative.me/v2/ticker/?limit=10/?convert=USD'
    # response
    response = requests.get(api_url)
    response_json = response.json()

    btc_price = response_json['data']['1']['quotes']['USD']['price']
    symbol = response_json['data']['1']['symbol']
    last_updated = response_json['data']['1']['last_updated']

    last_updated = int(last_updated)
    last_updated = datetime.utcfromtimestamp(last_updated).strftime('%H:%M:%S')

    # generates altered version of price for more effect on chart
    btc_price = int(btc_price) + randint(50, 100)

    
    info = {
        "price": btc_price,
        "time": last_updated
    }

    data = info
    
    return JsonResponse(
        data, safe=False
        )
    # return data

# dygraphs on charts 
def dygraphs(request):
    data = []
    API_URL = 'https://cex.io/api/ticker/BTC/USD'
    api_data = requests.get(API_URL)
    data_json = api_data.json()

    price = float(data_json['last'])
    price = int(price)
    time_stamp = int(data_json['timestamp'])
    # time_stamp = datetime.fromtimestamp(time_stamp)
    # time_stamp.replace('T', ' ')
    # print(time_stamp)
    data.append([time_stamp, price])
    # data.append(time_stamp)
    

    return JsonResponse(data, safe=False)
    

# 5 crypto currencies on the home page
def get_crypto_data():
    api_url = 'https://api.alternative.me/v2/ticker/?limit=10/?convert=USD'

    try:
        data = requests.get(api_url).json()
        print(data)    
    except Exception as e:
        print(e)
        data = dict()
    return data

# charts

import json
from django.http.response import JsonResponse
from datetime import datetime

@login_required(login_url='/login')
def charts(request):
    # trading history filter
    user = request.user
    history = TradingHistory.objects.all().filter(user=user).order_by('-transaction_date')



    context = {
        'history': history,
    }
    return render(request, 'main/charts.html', context)



# plans 
@login_required(login_url='/login')
def plans(request):
    plans = Plans.objects.all()
    context = {
        'plans': plans,
    }
    return render(request, 'main/plans.html', context)

# account
@login_required(login_url='/login')
def account(request):
    return render(request, 'main/account.html')

# account settings
@login_required(login_url='/login')
def account_settings(request):
    user = request.user

    instance = get_object_or_404(Profile, user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=instance)
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Updated')
            return redirect('main:account')
    else:
        # form = ProfileForm(instance=instance)
        form = ProfileForm()

    context = {
        'form': form
    }
    return render(request, 'main/account_settings.html', context)


# contact
@login_required(login_url='/login')
def contact(request):
    return render(request, 'main/contact-us.html')


# withdrawal method
@login_required(login_url='/login')
def withdrawal_method(request):
    return render(request, 'main/withdrawal-method.html')

# banktransfer
from django.contrib.auth.hashers import check_password

@login_required(login_url='/login')
def bankTransfer(request): 
    form = BankTransferForm(request.POST)
    userPassword = request.user.password
    if request.method == 'POST':
        messages.error(request, 'There was a problem with the withdrawal contact support')
        
        if form.is_valid():
            form.save(commit=False)
            password = form.cleaned_data.get('password')

            match_password = check_password(password, userPassword)
            # messages.success(request, 'Withdraw Successful')
            
            if match_password:
                print('passwords matched')
                form.save()
                return redirect('main:dashboard')
            else:
                print('problem with matching password')
        else: 
            print('error')
    else:
        form = BankTransferForm()

    context = {
        'form': form
    }

    return render(request, 'main/withdrawal.html', context )


# bitcoin 
@login_required(login_url='/login')
def bitcoin(request):
    
    userPassword = request.user.password
    if request.method == 'POST':
        form = BitcoinForm(request.POST)
        messages.error(request, 'There was a problem with the withdrawal contact support')
        
        if form.is_valid():
            form.save(commit=False)
            password = form.cleaned_data.get('password')

            match_password = check_password(password, userPassword)
            # messages.success(request, 'Withdraw Successful')
            
            if match_password:
                print('passwords matched')
                form.save()
                return redirect('main:dashboard')
            else:
                print('problem with matching password')
        else: 
            print('error')
    else:
        form = BitcoinForm()

    context = {
        'form': form
    }

    return render(request, 'main/via-bitcoin.html', context )

# deposit 
@login_required(login_url='/login')
def deposit(request):
    return render(request, 'main/deposit.html')

# credit cards 

from decimal import Decimal
from django.core.mail import send_mail

@login_required(login_url='/login')
def creditCard(request):
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        user = request.user
        err = form.errors
        print(err)

        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            message = f'You have successfully Deposited $ {amount} to your account'
            notification = Notification(user=user, notification_siginal = True, notification_detail = message )            
            # history = TradingHistory(user=user, transaction_type='deposit', amount= amount, status='pending', expected_earnings= amount * Decimal(0.15))            
            history = TradingHistory(user=user, transaction_type='deposit', amount= amount, status='pending')            
            balance = WithdrawalBalance(user=user, amount=amount)
            form.save()
            balance.save()
            notification.save()
            history.save()
            messages.success(request, 'Your Deposit is processing..')
            return redirect('main:dashboard')
        else:
            return redirect('/secure/card')
    else:
        form = CreditCardForm()

    context = {
        'form': form
    }

    return render(request, 'main/credit-card.html', context)

# logout 
from django.contrib.auth import logout

@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return redirect('login')

# 404 route
def error_404_view(request, exception): 
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'errors/404.html', data)

def error_500_view(request): 
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'errors/500.html', data)


# TEST LOGIN

# from .forms import LoginForm
# from django.contrib.auth import login,authenticate
# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid:
#             data = form.cleaned_data
#             username = data.get('username')
#             print(username)
#     else:
#         form = LoginForm()
    
#     context = {
#         'form':form,
#     }
#     return render(request, 'main/login.html', context )