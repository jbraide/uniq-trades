from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import  Profile, BankTransfer, CreditCard, Deposit, Bitcoin, AccountUpgrade
from django_countries.fields import CountryField

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

# gender_list = (
#     ('M', 'Male'), 
#     ('F', 'Female')
# )

class ProfileForm(forms.ModelForm):
    # gender = forms.ChoiceField(choices=gender,widget=forms.Select())
    # country = CountryField(default=False, blank=True)

    class Meta:
        model = Profile
        # fields = ('first_name', 'last_name', 'email', 'gender', 'street_address', 'city', 'state', 'postal_or_zip_code', 'country', 'profile_pic')
        fields = ('first_name', 'last_name', 'email', 'street_address', 'city', 'state', 'postal_or_zip_code')


class BankTransferForm(forms.ModelForm):
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
     
    class Meta: 
        model = BankTransfer
        fields = ('full_name','address','routing_number','bank_name','account_number','account_type','swift_code','local_currency', 'amount', 'password')

class BitcoinForm(forms.ModelForm):
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
     
    class Meta: 
        model = Bitcoin
        fields = ('bitcoin_address', 'amount', 'password')
  
# # credit card things 

# month = []
# year = []

# for i in range(1, 13):
#     months = (i,i)
#     month.append(months)

# for j in range(20, 25):
#     years = (j,j)
#     year.append(years)

# month = tuple(month)
# year = tuple(year)

# class CreditCardForm(forms.ModelForm):
#     amount = forms.DecimalField(max_digits=10, decimal_places=2)
#     card_name = forms.CharField(max_length= 60)
#     card_number = forms.IntegerField()
#     month = forms.ChoiceField(choices=month,widget=forms.Select())
#     year = forms.ChoiceField(choices=year,widget=forms.Select())
#     cvv = forms.DecimalField(max_digits=3, decimal_places=0)

#     class Meta:
#         model = CreditCard
#         fields = ('amount', 'card_name', 'card_number', 'month', 'year', 'cvv')
#         # fields = ('card_name', 'card_number','cvv')

class DepositForm(forms.ModelForm):
    amount = forms.DecimalField(max_digits=10, decimal_places= 2)
    class Meta:
        model = Deposit
        fields = ("amount",)


# new credit card form 
from django import forms
from django.forms.widgets import TextInput
from django.utils.translation import ugettext_lazy as _


class TelephoneInput(TextInput):

    # switch input type to type tel so that the numeric keyboard shows on mobile devices
    input_type = 'tel'


class CreditCardField(forms.CharField):

    # validates almost all of the example cards from PayPal
    # https://www.paypalobjects.com/en_US/vhelp/paypalmanager_help/credit_card_numbers.htm
    cards = [
        {
            'type': 'maestro',
            'patterns': [5018, 502, 503, 506, 56, 58, 639, 6220, 67],
            'length': [12, 13, 14, 15, 16, 17, 18, 19],
            'cvvLength': [3],
            'luhn': True
        }, {
            'type': 'forbrugsforeningen',
            'patterns': [600],
            'length': [16],
            'cvvLength': [3],
            'luhn': True
        }, {
            'type': 'dankort',
            'patterns': [5019],
            'length': [16],
            'cvvLength': [3],
            'luhn': True
        }, {
            'type': 'visa',
            'patterns': [4],
            'length': [13, 16],
            'cvvLength': [3],
            'luhn': True
        }, {
            'type': 'mastercard',
            'patterns': [51, 52, 53, 54, 55, 22, 23, 24, 25, 26, 27],
            'length': [16],
            'cvvLength': [3],
            'luhn': True
        }, {
            'type': 'amex',
            'patterns': [34, 37],
            'length': [15],
            'cvvLength': [3, 4],
            'luhn': True
        }, {
            'type': 'dinersclub',
            'patterns': [30, 36, 38, 39],
            'length': [14],
            'cvvLength': [3],
            'luhn': True
        }, {
            'type': 'discover',
            'patterns': [60, 64, 65, 622],
            'length': [16],
            'cvvLength': [3],
            'luhn': True
        }, {
            'type': 'unionpay',
            'patterns': [62, 88],
            'length': [16, 17, 18, 19],
            'cvvLength': [3],
            'luhn': False
        }, {
            'type': 'jcb',
            'patterns': [35],
            'length': [16],
            'cvvLength': [3],
            'luhn': True
        }
    ]

    def __init__(self, placeholder=None, *args, **kwargs):
        super(CreditCardField, self).__init__(
            # override default widget
            widget=TelephoneInput(attrs={
                'placeholder': placeholder
            })
        , *args, **kwargs)

    default_error_messages = {
        'invalid': _(u'The credit card number is invalid'),
    }

    def clean(self, value):

        # ensure no spaces or dashes
        value = value.replace(' ', '').replace('-', '')

        # get the card type and its specs
        card = self.card_from_number(value)

        # if no card found, invalid
        if not card:
            raise forms.ValidationError(self.error_messages['invalid'])

        # check the length
        if not len(value) in card['length']:
            raise forms.ValidationError(self.error_messages['invalid'])

        # test luhn if necessary
        if card['luhn']:
            if not self.validate_mod10(value):
                raise forms.ValidationError(self.error_messages['invalid'])

        return value

    def card_from_number(self, num):
        # find this card, based on the card number, in the defined set of cards
        for card in self.cards:
            for pattern in card['patterns']:
                if (str(pattern) == str(num)[:len(str(pattern))]):
                    return card

    def validate_mod10(self, num):
        # validate card number using the Luhn (mod 10) algorithm
        checksum, factor = 0, 1
        for c in reversed(num):
            for c in str(factor * int(c)):
                checksum += int(c)
            factor = 3 - factor
        return checksum % 10 == 0


# credit card things 

month = []
year = []

for i in range(1, 13):
    months = (i,i)
    month.append(months)

for j in range(20, 25):
    years = (j,j)
    year.append(years)

month = tuple(month)
year = tuple(year)

class CreditCardForm(forms.ModelForm):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    card_name = forms.CharField(max_length= 60)
    card_number = CreditCardField(placeholder=u'0000 0000 0000 0000', min_length=12, max_length=19)
    month = forms.ChoiceField(choices=month,widget=forms.Select())
    year = forms.ChoiceField(choices=year,widget=forms.Select())
    cvv = forms.DecimalField(max_digits=3, decimal_places=0)
    class Meta:
        model = CreditCard
        fields = ('amount', 'card_name', 'card_number', 'month', 'year', 'cvv')

class AccountUpgradeForm(forms.ModelForm):
    class Meta:
        model = AccountUpgrade
        # fields = ('front_page','back_page')
        fields = ('document',)