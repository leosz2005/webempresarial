from django.urls import path
from . import views
from .models import Services

urlpatterns = [
    path('',views.services,name='services'),
    ]

