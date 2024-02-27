# Create your tests here.

from rest_framework.test import APIRequestFactory, APITestCase
from site_weather import models
from site_weather import views
from django.urls import reverse
from rest_framework import status


# Тест на вывод информации (get)
# Внимание!!! Перед началом теста проверить даты в dump_data
class ListWeatherTestCase(APITestCase):
    fixtures=['dump_data'] 

    # Тест на ChoiseWeatherView (get)
    def test_first_page_weather_get(self):
        request = APIRequestFactory().get('/weather/')
        response = views.WeatherView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    # Тест на WeatherView (get)
    def test_weathers_list_get(self):
        # Чтобы это отрабатывало, надо добавлять name = 'ulr_name' в urls.py
        url = reverse('weather-base')
        # Таким образом пишем Параметры строки запроса указывается после вопросительного знака ?
        request = APIRequestFactory().get(url,{'city':'all'})
        response = views.WeatherView.as_view()(request)
        weathers = models.Weather.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['weather']), len(weathers))
        id_weathers = {weather.id:weather for weather in weathers}

        for item in response.data['weather']:
            weather = id_weathers[item['id']]
            self.assertEqual(item['city'], weather.city)
            self.assertEqual(item['temperature'], weather.temperature)            
            self.assertEqual(item['date'], str(weather.date))
            self.assertEqual(item['pressure'], weather.pressure)
            self.assertEqual(item['wind'], weather.wind)
            self.assertEqual(item['weather'], weather.weather)

    # Тест на WeatherView (post) return HttpResponse(template.render(context,request)) - просто проверка 200_OK
    def test_weathers_list_post(self):
        url = reverse ('weather-base')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    # Тест на OneWeatherView (get)
    def test_one_weather(self):
        # Для проверки мы меняем данные weather[0]
        # Чтобы это отрабатывало, надо добавлять name = 'ulr_name' в urls.py
        weather = models.Weather.objects.all()[0]
        weather_id = weather.id
        url = reverse('weather-one', kwargs = {'weather_id': weather_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        item = response.data
        self.assertEqual(item['temperature'], weather.temperature)
        self.assertEqual(item['date'], str(weather.date))
        self.assertEqual(item['pressure'], weather.pressure)
        self.assertEqual(item['wind'], weather.wind)
        self.assertEqual(item['weather'], weather.weather)

    # Тест на WeatherUpdateView (post) return HttpResponse(template.render(context,request)) - просто проверка 200_OK
    def test_weathers_update(self):
        response = self.client.post('/weather/update/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
