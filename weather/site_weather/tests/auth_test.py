# Create your tests here.

from rest_framework.test import APIRequestFactory, APITestCase
from site_weather import models
from site_weather import views
from rest_framework import status

class FirstPageAuthTestCase(APITestCase):
    fixtures=['dump_data'] 

    # Тест на HoroskopFirstPageView (get)
    def test_first_page_auth_get(self):
        request = APIRequestFactory().get('/weather/horoskop/')
        response = views.WeatherView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Тест на транзитную страницу HoroskopRegistrationView (get)
    def test_register_tranzit_get(self):
        request = APIRequestFactory().get('/weather/horoskop/registration/')
        response = views.HoroskopRegistrationView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Тест на страницу регистрации HoroskopRegistrationView (post)
    def test_register_post(self):
        # Можно менять значение переменной username
        username = password = 'username'

        url = '/weather/horoskop/registration/'
        user_first_count = len(models.User.objects.all())
        request = APIRequestFactory().post(url,{"username":username,"password":password,"user_zodiac":"ARIES"})
        response = views.HoroskopRegistrationView.as_view()(request)
        if response.status_code == 302:
            assert response.status_code == 302
        else:
            assert str(response.data['username']) == "[ErrorDetail(string='Пользователь с таким именем уже существует.', code='unique')]"    
        users = models.User.objects.all()        
        assert len(users) == (user_first_count+1)
        id_user = users.get(username=username).id

        assert users.get(id=id_user).username == username
        assert users.get(id=id_user).user_zodiac == "ARIES"

    # Тест на HoroskopAutorizationView (get)
    def test_auth_get(self):
        request = APIRequestFactory().get('/weather/horoskop/autorization/')
        response = views.WeatherView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
