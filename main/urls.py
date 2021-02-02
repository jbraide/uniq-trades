from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'main'

urlpatterns = [
    # home page & non login information
    path('', views.index, name='index'),
    path('invest-in', views.investments, name='investments'),
    path('plans/', views.plans, name='plans'),
    path('contact-us/', views.contact, name='contact-us'),
    path('invest/marijuana/', views.marijuana, name='marijuana' ),
    path('invest/forex/', views.forex, name='forex' ),
    path('invest/commodities/', views.commodities, name='commodities' ),
    path('invest/crude-oil/', views.crudeOil, name='crude-oil' ),
    # dashboard logic
    path('account/', views.account, name='account'),
    path('account/settings/', views.account_settings, name='account-settings'),    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('charts/', views.charts, name='charts'),
    path('deposit/', views.deposit, name='deposit'),
    path('withdraw/method',views.withdrawal_method, name='withdrawal-method'),
    path('withdraw/bitcoin', views.bitcoin,name='bitcoin'),
    path('withdraw/bank-transfer', views.bankTransfer,name='withdraw'),
    path('logout/', views.logout_view, name='logout'),
    # path('secure/card/', views.creditCard, name='credit-card'),
    # path('login/',views.login, name='login'),
    # activation routes 
    path('activation_sent/', views.activation_sent_view, name='activation_sent'), 
    path('activate/<slug:uidb64>/<slug:token>', views.activate, name='activate'), 
    path('account/upgrade/', views.upgrade_account, name='upgrade')
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )