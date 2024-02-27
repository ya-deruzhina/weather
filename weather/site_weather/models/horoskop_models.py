from django.db import models

# Create your models here.

class HoroskopModel (models.Model):
    ARIES = "ARIES"
    TAURUS = "TAURUS"
    GEMINI = "GEMINI"
    CANCER = "CANCER"
    LEO = "LEO"
    VIRGO = "VIRGO"
    LIBRA = "LIBRA"
    SCORPIO = "SCORPIO"
    SAGITTARIUS = "SAGITTARIUS"
    CAPRICORN = "CAPRICORN"
    AQUARIUS = "AQUARIUS"
    PISCES = "PISCES"

    KIND_ZODIACS = [
        (ARIES, "Aries"),
        (TAURUS, "Taurus"),
        (GEMINI, "Gemini"),
        (CANCER, "Cancer"),
        (LEO, "Leo"),
        (VIRGO, "Virgo"),
        (LIBRA, "Libra"),
        (SCORPIO, "Scorpio"),
        (SAGITTARIUS, "Sagittarius"),
        (CAPRICORN, "Capricorn"),
        (AQUARIUS, "Aquarius"),
        (PISCES, "Pisces"),

    ]

    zodiac = models.CharField (choices=KIND_ZODIACS,primary_key=True)
    description = models.CharField()
    date_create_zodiac = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.zodiac