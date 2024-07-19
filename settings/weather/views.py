from django.shortcuts import render
from django.views.decorators.http import require_GET
from services.weather import city_autocomplete_service, history_update, build_chart, last_viewed_city, get_history


# Create your views here.


def search_city(request):
    return render(request, 'weather/search.html')


def history(request):
    history = get_history(request)
    context = {'history_list': history}
    return render(request, 'weather/history.html', context=context)


def report(requests):
    longitude, latitude = history_update(requests)
    chart = build_chart(latitude=latitude, longitude=longitude)
    return render(requests, 'weather/report.html', context={'chart': chart})


@require_GET
def city_autocomplete(request):
    context = city_autocomplete_service(request)
    return render(request, 'weather/autocomplete.html', context)


def last_viewed_city_view(request):
    last_city = last_viewed_city(request)
    context = {'last_city': last_city}
    return render(request, 'weather/last_viewed_city.html', context=context)