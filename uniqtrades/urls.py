from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView as auth_views
from django.contrib.auth import logout
from main.views import signup_view

from django.conf.urls import handler404, handler500
from main.views import error_404_view, error_500_view

# autoincrement
# from main.views import autoincrement


urlpatterns = [
    path('register/', signup_view, name='register'),
    path('login/', auth_views.as_view() , name='login'), 
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('', include('main.urls', namespace='main')),
]


handler404 = error_404_view
# handler500 = error_500_view
# autoincrement(repeat=10)