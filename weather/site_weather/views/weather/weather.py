from site_weather.models import Weather
from site_weather.forms import BaseChoiceForm 
from django.http import HttpResponse,HttpResponseRedirect 
from django.views import View
from django.template import loader
from datetime import datetime, timedelta
from site_weather.serializers import WeatherCommonSerializer 
from rest_framework.response import Response
from rest_framework.views import APIView
import requests



class ChoiseWeatherView(View):
    def get (self, request):
        template = loader.get_template("weathers/base_page.html")
        context = {
            "form":BaseChoiceForm()
        }
        return HttpResponse(template.render(context,request))

class WeatherView(APIView):
    #Выводит погоду из БД всю или по городу
    def post(self,request,format=None):
        city = request.POST.get('city')
        if city == 'all':
            all_weather = Weather.objects.all()
        else:
            date_first = (datetime.now()-timedelta(days=2)).__format__("%Y-%m-%d")
            all_weather = Weather.objects.filter(city=city, date__gte=date_first).order_by('date')[:5]
        template = loader.get_template("weathers/all_weather.html")
        context = {
            "many_weathers":all_weather,
        }
        return HttpResponse(template.render(context,request))


    # Работает через postman (body - без ковычек)
    def get(self,request,format=None):
        city = request.GET.get("city")
        if city == 'all':
            all_weather = Weather.objects.all()
        else:
            date_first = (datetime.now()-timedelta(days=2)).__format__("%Y-%m-%d")
            all_weather = Weather.objects.filter(city=city, date__gte=date_first).order_by('date')[:5]

        working_services = [WeatherCommonSerializer (instance=working_service).data for working_service in all_weather]
        return Response ({'weather':working_services})
    
class WeatherUpdateView(APIView):
    def post(self,request):
        try:
            response = requests.get('http://127.0.0.1:8001/news/weather/').json()
            serializer = WeatherCommonSerializer(data=response['weather'],many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return HttpResponseRedirect ("/weather/")
            
        except:
           return Response ({'status':'not updated'})