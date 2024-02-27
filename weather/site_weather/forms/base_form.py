from django.forms import ModelForm
from site_weather.models import Weather


class BaseChoiceForm (ModelForm):
    class Meta:
        model = Weather
        fields = ["city"]