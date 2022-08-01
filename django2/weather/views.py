from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
# Create your views here.
def index (request):
    key = 'ea4d8017c6a8cc4cda3672d2ad69ed4b'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + key

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp' : res["main"]["temp"],
            'icon' : res["weather"][0]["icon"]
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}


    return render(request, 'weather/index.html', context)