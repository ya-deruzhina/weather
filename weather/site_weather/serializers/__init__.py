from site_weather.serializers.weather.weather_serializer import WeatherCommonSerializer
from site_weather.serializers.user.registrate_serializer import RegisterUserSerializer
from site_weather.serializers.horoskop.horoskop_serializer import HoroskopSerializer
from site_weather.serializers.user.messages_serializer import MessagesSerializer

all = (
    "WeatherCommonSerializer",
    "RegisterUserSerializer",
    "HoroskopSerializer",
    "MessagesSerializer",
)