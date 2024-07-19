from django.shortcuts import render
from django.views.decorators.http import require_GET
from services.weather import city_autocomplete_service, history_update, build_chart


# Create your views here.


def search_city(requests):
    return render(requests, 'weather/search.html')


def history(requests):
    return render(requests, 'weather/history.html')


def report(requests):
    longitude, latitude = history_update(requests)
    chart = build_chart(latitude=latitude, longitude=longitude)
    return render(requests, 'weather/report.html', context={'chart': chart})


@require_GET
def city_autocomplete(request):
    context = city_autocomplete_service(request)
    return render(request, 'weather/autocomplete.html', context)
