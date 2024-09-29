# myapp/urls.py

from django.urls import path
from .views import UserRegistrationView

urlpatterns = [
    path('submit/', UserRegistrationView.as_view(), name='user_register'),
]
