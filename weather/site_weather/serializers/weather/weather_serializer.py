from rest_framework import serializers
from site_weather.models import Weather


class WeatherCommonSerializer(serializers.Serializer):
    id = serializers.IntegerField (read_only = True)
    KIND_CHOICES = ['SUN','RAIN','FOGGY']
    city = serializers.CharField(max_length=20)
    date = serializers.DateField()
    temperature = serializers.IntegerField()
    pressure = serializers.IntegerField()
    wind = serializers.FloatField()
    weather = serializers.ChoiceField (choices= KIND_CHOICES, default='SUN')

    def create (self,validated_data):
        return Weather.objects.create(**validated_data)