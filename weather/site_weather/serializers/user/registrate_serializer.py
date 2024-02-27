from rest_framework import serializers
from site_weather.models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password","user_zodiac"]

    def create(self, validated_data):
        return User.objects.create(**validated_data)
       
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    