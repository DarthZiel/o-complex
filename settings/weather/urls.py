from .views import search_city, history, city_autocomplete
from django.urls import path

app_name = 'weather'
urlpatterns = [
    path('search/', search_city, name='search'),
    path('history/', history, name='history'),
    path('city-autocomplete/', city_autocomplete, name='city-autocomplete'),
    ]
