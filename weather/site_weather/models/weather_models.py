from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Weather (models.Model):
    SUN = "SUN"
    RAIN = "RAIN"
    FOGGY = "FOGGY"

    KIND_CHOICES = [
        (SUN, "Sun"),
        (RAIN, "Rain"),
        (FOGGY, "Foggy"),
    ]

    all = "all"
    Minsk = "Minsk"
    Moscow = "Moscow"

    CITY = [
        (all,"all"),
        (Minsk,"Minsk"),
        (Moscow,"Moscow"),
        ]


    city = models.CharField(max_length=20,choices=CITY, default='all')
    date = models.DateField()
    temperature = models.IntegerField()
    pressure = models.IntegerField()
    wind = models.FloatField()
    weather = models.CharField (max_length=10,choices=KIND_CHOICES, default=SUN)

    def __str__ (self) -> str:
        return self.city    
    
@receiver (post_save, sender=Weather)
def my_handler(sender, instance, **kwargs):
    weather = Weather.objects.all().order_by('city','date')
    n = range(0,len(weather)-1)
    m = range(1,len(weather))
    for count_n,count_m in zip(n,m):
        if weather[count_n].city==weather[count_m].city and weather[count_n].date==weather[count_m].date:
                test = Weather.objects.filter(city=weather[count_n].city,date=weather[count_n].date).order_by('id').first().delete()