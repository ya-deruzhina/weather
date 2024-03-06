from django.forms import ModelForm
from site_weather.models import HoroskopModel


class CreateHoroskopForm (ModelForm):
    class Meta:
        model = HoroskopModel
        fields = ["zodiac","description"]