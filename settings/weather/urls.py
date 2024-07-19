from .views import search_city, history, city_autocomplete, report, last_viewed_city_view
from django.urls import path

app_name = 'weather'
urlpatterns = [
    path('search/', search_city, name='search'),
    path('history/', history, name='history'),
    path('city-autocomplete/', city_autocomplete, name='city-autocomplete'),
    path('report/', report, name='report'),
    path('last_viewed_city/', last_viewed_city_view, name='last_viewed_city_view')
]
