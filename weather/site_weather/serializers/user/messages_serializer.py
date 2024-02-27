from rest_framework import serializers
from site_weather.models import MessagesUserModel



class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagesUserModel
        fields = ["message","user_page_id","autor_message"]
