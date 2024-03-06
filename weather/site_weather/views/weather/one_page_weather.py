from site_weather.models import Weather
from site_weather.serializers import WeatherCommonSerializer 
from rest_framework import generics


# Выводит Json
class OneWeatherView(generics.RetrieveAPIView):
    weather_id = 1
    queryset = Weather.objects.all()
    serializer_class = WeatherCommonSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'weather_id'