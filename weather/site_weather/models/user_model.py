from django.db import models
from site_weather.models import HoroskopModel
from django.contrib.auth.models import AbstractUser

    

class User(AbstractUser):
    KIND_ZODIACS = HoroskopModel.KIND_ZODIACS
    user_zodiac = models.CharField (choices=KIND_ZODIACS)
    def __str__(self):
        return self.username
    