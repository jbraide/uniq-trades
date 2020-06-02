from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('charts/', views.charts, name='charts'),
    path('plans/', views.plans, name='plans'),
    path('account/', views.account, name='account'),
    path('account/settings/', views.account_settings, name='account-settings'),
    path('contact-us/', views.contact, name='contact-us'),
    # path('incr/', views.autoincrement, name='incr'),
    path('line-chart/', views.get_crypto_data, name='crypto-data'),
    path('deposit/', views.deposit, name='deposit'),
    path('withdraw/', views.withdraw,name='withdraw'),
    path('logout/', views.logout_view, name='logout'),
    path('secure/card/', views.creditCard, name='credit-card'),
    path('btc/data/', views.crypto_chart,  name='crypto_chart'), 

    # dygraphs 
    path('dygraphs/', views.dygraphs, name='Dygraphs'),
    # path('login/',views.login, name='login'),
    # activation routes 
    path('activation_sent/', views.activation_sent_view, name='activation_sent'), 
    path('activate/<slug:uidb64>/<slug:token>', views.activate, name='activate')
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )