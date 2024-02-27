from django.forms import ModelForm
from site_weather.models import HoroskopModel
from django import forms

class UpdateHoroskopForm (forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['description'].required=True
    class Meta:
        model = HoroskopModel
        fields = ["description"]