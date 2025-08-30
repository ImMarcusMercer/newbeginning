# backend/api/urls.py
from django.urls import path
from .user_api import UserLoginAPIView  # Ensure you're importing the right view

urlpatterns = [
    path('users/login/api/', UserLoginAPIView.as_view(), name='user-login'),
]
