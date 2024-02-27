from rest_framework import serializers
from site_weather.models import HoroskopModel


class HoroskopSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoroskopModel
        fields = ["zodiac","description"]

    def create(self, validated_data):
        return HoroskopModel.objects.create(**validated_data)
       
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
