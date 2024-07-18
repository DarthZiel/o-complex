from django.shortcuts import render
from django.views.decorators.http import require_GET
from services.weather import city_autocomplete_service

# Create your views here.


def search_city(requests):
    return render(requests, 'weather/search.html')


def history(requests):
    return render(requests, 'weather/history.html')




@require_GET
def city_autocomplete(request):
    context = city_autocomplete_service(request)
    return render(request, 'weather/autocomplete.html', context)
