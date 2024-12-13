from django.urls import path
from django.contrib.auth import logout

from . import views

urlpatterns = [
    path('', views.home, name='Hospital-Home'),
    path('home/', views.home, name='Hospital-Home'),
    path('entry/', views.entry, name='Hospital-Entry'),
    path('about/', views.about, name='Hospital-About'),
    path('contact/', views.contact_us, name='Hospital-Contact-Us'),
    path('insert/', views.insert, name='Hospital-Insert'),
    path('checkUser/', views.check_user, name='Hospital-Check-User'),
    path('getWorkIdes/', views.get_work_ides, name='Hospital-Get-Work-Ides'),
    path('getInstitutes/', views.get_institutes, name='Hospital-Get-Institutes'),
    path('getUsers/', views.get_users, name='Hospital-Get-Institutes'),
]
