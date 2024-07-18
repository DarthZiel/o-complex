import requests


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
                       'admin4', '')} for city in data.get('results')]
        return {'cities': cities}
