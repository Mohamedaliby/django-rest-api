from django.urls import path
from .views import UserCreateAPIView, UserLoginAPIView
from rest_framework.authtoken import views

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    # path('login/', UserLoginAPIView.as_view(), name='login'),
    path('login/', views.obtain_auth_token, name='login'),


]
