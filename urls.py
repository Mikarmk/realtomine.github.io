from django.urls import path
from .views import home, calculate_time

urlpatterns = [
    path('', home, name='home'),
    path('calculate_time/', calculate_time, name='calculate_time'),
]