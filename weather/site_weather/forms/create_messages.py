from django.forms import ModelForm
from site_weather.models import MessagesUserModel

class CreateMessageForm(ModelForm):
    class Meta:
        model = MessagesUserModel
        fields = ["message"]
        
