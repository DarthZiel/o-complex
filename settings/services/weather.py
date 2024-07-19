from django.contrib.auth import get_user_model
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import requests

from weather.models import SearchHistory


def city_autocomplete_service(request):
    query = request.GET.get('city', '')

    # Используйте внешний API для поиска городов
    api_url = 'https://geocoding-api.open-meteo.com/v1/search'
    params = {
        'name': query,
        'count': 10,
        'language': 'ru',
        'format': 'json'
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()
        cities = [{'name': city['name'],
                   'additional_info': city.get('admin1', '') + city.get('admin2', '') + city.get('admin3',
                                                                                                 '') + city.get(
                       'admin4', ''), 'latitude': float(city['latitude']), 'longitude': float(city['longitude'])} for
                  city in
                  data.get('results')
                  ]
        return {'cities': cities}


def history_update(request):
    email = request.user.email
    name = request.GET.get('name', '')
    additional_info = request.GET.get('additional_info', None)
    longitude = request.GET.get('longitude', '')
    latitude = request.GET.get('latitude', '')
    user_instance = get_user_model().objects.get(email=email)

    search_history_instance, created = SearchHistory.objects.get_or_create(
        name=name,
        user=user_instance,
        additional_info=additional_info,
        latitude=float(latitude.replace(',', '.')),
        longitude=float(longitude.replace(',', '.'))
    )

    if created:
        return search_history_instance.longitude, search_history_instance.latitude
    else:
        search_history_instance.counter += 1
        search_history_instance.save()
        return search_history_instance.longitude, search_history_instance.latitude


app = DjangoDash('TemperatureChart')  # идентификатор вашего Dash приложения


def get_temperature_from_api(latitude, longitude):
    api_url = 'https://api.open-meteo.com/v1/forecast'
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'hourly': 'temperature_2m'
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.json()
    return None


def build_chart(latitude, longitude):
    data = get_temperature_from_api(latitude, longitude)
    if not data:
        return None

    times = data['hourly'].get('time')
    temperatures = data['hourly'].get('temperature_2m')

    trace = go.Scatter(
        x=times,
        y=temperatures,
        mode='lines+markers',
        name='Temperature',
        marker=dict(color='blue'),
    )

    layout = go.Layout(
        title='Temperature Over Time',
        xaxis=dict(title='Date'),
        yaxis=dict(title='Temperature (°C)'),
    )

    fig = go.Figure(data=[trace], layout=layout)

    app = fig.to_html()
    return app


def last_viewed_city(request):
    user = request.user
    if user.is_authenticated:
        history_record = SearchHistory.objects.filter(user=user).last()
        return history_record
    return None

def get_history(request):
    user = request.user.id
    return SearchHistory.objects.filter(user=user)
