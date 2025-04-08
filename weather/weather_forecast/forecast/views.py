from django.shortcuts import render
from django.db.models import Q
import requests
from .models import City
from .forms import CityForm
from django.views.generic import ListView
from datetime import datetime
from django.utils import timezone


# Create your views here.

def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=385f1b098173657db729e61e4c744c87'

    current_datetime = datetime.now() # to get the current date

    cities = City.objects.all()

    mycities = City.objects.all().values()

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()


    '''Below is to convert timestamp to readable time for my sunrise and sunset functionality '''
    
    timestamp = city_weather['sys']['sunrise']
    real_time = datetime.fromtimestamp(timestamp, tz = timezone.get_current_timezone())
    sunrise = real_time.strftime('%H:%M')
    
    ''' this is for the sunset '''
    timestamps = city_weather['sys']['sunset']
    real_times = datetime.fromtimestamp(timestamps, tz = timezone.get_current_timezone())
    sunset = real_times.strftime('%H:%M')

    weather = {
            'city': city,
            'temperature': round((city_weather['main']['temp'] - 32) / 1.8),
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
            'cloud': city_weather['clouds']['all'],
            'humidity': city_weather['main']['humidity'],
            'pressure': city_weather['main']['pressure'],
            'longitude': str(city_weather['coord']['lon']),
            'latitude': str(city_weather['coord']['lat']),
            'windspeed': city_weather['wind']['speed'],
            'wind_dir': city_weather['wind']['deg'],
            'visibility': city_weather.get('visibility'),
            'timezone': city_weather.get('timezone'),
            'sunrise': sunrise,
            'sunset': sunset,
            }
    weather_data.append(weather)

    current_hour = datetime.now().hour
    


    context = {
        'weather_data': weather_data,
        'form': form,
        'current_datetime': current_datetime,
        'mycities': mycities,
        'current_hour': current_hour,
        'title': 'Weather Now: Know Before You Go',
    }

    return render(request, 'user/weather.html', context)

''' Below is for the search part, that is to query data from the db. '''
class SearchResultsView(ListView):
    model = City
    template_name = 'user/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('search_field')
        object_list = City.objects.filter(
                Q(name__icontains = query)
                )
        return object_list
