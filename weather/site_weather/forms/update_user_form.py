from django.forms import ModelForm
from site_weather.models import User
from django import forms

class UpdateUserForm (forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].required=False
        self.fields['password'].required=False
        self.fields['user_zodiac'].required=False
    class Meta:
        model = User
        fields = ['username','password','user_zodiac']