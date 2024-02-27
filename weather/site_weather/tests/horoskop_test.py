from rest_framework.test import APIRequestFactory, APITestCase
from site_weather import models
from django.urls import reverse
from rest_framework import status
from rest_framework.test import force_authenticate
from rest_framework.test import APIClient


class HoroskopTestCase(APITestCase):
    fixtures=['dump_data'] 

    # Создание токена
    def test_post_tokens(self):
        url = reverse('token_obtain_pair')

        user = models.User.objects.get(id=13)
        user_username = user.username
        token = (self.client.post(url,data={'username':user_username, 'password':user_username})).data['access']
        self.token = token
        self.user=user
        
        user_admin = models.User.objects.get(id=1)
        user_username_admin = user_admin.username
        token_admin = (self.client.post(url,data={'username':user_username_admin, 'password':user_username_admin})).data['access']
        self.token_admin = token_admin
        self.user_admin=user_admin
        
        
    # Тест на вывод информации "HoroskopBaseAfterAuthView" (get)
    def test_horoskop_for_user_get(self):
        self.test_post_tokens()
        token = self.token 
        response = self.client.get(
            reverse('horoskop-base'),
            **{'HTTP_AUTHORIZATION': f'Bearer {token}'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Тест на вывод информации "HoroskopAll" (get) - не админ (список)
    def test_list_horoskop (self):
        self.test_post_tokens()
        token = self.token 
        response = self.client.get(
            reverse('horoskop-list'),
            **{'HTTP_AUTHORIZATION': f'Bearer {token}'}
        )

        horoskops = models.HoroskopModel.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['horoskop']), len(horoskops))
        zodiac_horoskops = {horoskop.zodiac:horoskop for horoskop in horoskops}

        for item in response.data['horoskop']:
            horoskop = zodiac_horoskops[item['zodiac']]
            # Дату не вывожу, потому что в сериалайзере она не обрабатывается
            self.assertEqual(item['description'], horoskop.description)            

    # Тест на вывод информации "HoroskopAll" (get) - админ
    def test_list_horoskop_admin (self):
        self.test_post_tokens()
        token = self.token_admin 
        response = self.client.get(
            reverse('horoskop-list'),
            **{'HTTP_AUTHORIZATION': f'Bearer {token}'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Тест на показ одного Гороскопа Json "HoroskopOne"
    def test_one_horoskop (self):
        zodiac = "TAURUS"
        self.test_post_tokens()
        token = self.token 
        response = self.client.get(
            reverse('horoskop-one', kwargs = {'zodiac':zodiac}),
            **{'HTTP_AUTHORIZATION': f'Bearer {token}'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        horoskop = models.HoroskopModel.objects.get(zodiac = zodiac)
        item = response.data
        self.assertEqual(item['description'], horoskop.description)    

    # Тест на "HoroskopCreateTransit" (get) просто проверка 200_OK - только admin
    def test_horoskop_create_transit(self):
        self.test_post_tokens()
        token_admin = self.token_admin 
        response = self.client.get(
            reverse('horoskop-create-transit'),
            **{'HTTP_AUTHORIZATION': f'Bearer {token_admin}'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # Тест на "HoroskopCreateTransit" (post) return Redirect - только admin
    def test_horoskop_create(self):
        self.test_post_tokens()
        token_admin = self.token_admin 
        horoskop_first_count = len(models.HoroskopModel.objects.all())        
        # zodiac = "ARIES"
        zodiac = "TAURUS"
        response = self.client.post(
            reverse('horoskop-create-transit'),
            **{'HTTP_AUTHORIZATION': f'Bearer {token_admin}'},
            data={"zodiac":zodiac,"description":"new"}, 
        )

        if response.status_code == 302:
            self.assertEqual(response.status_code, status.HTTP_302_FOUND )
            horoskops = models.HoroskopModel.objects.all()        
            assert len(horoskops) == (horoskop_first_count+1)
            assert horoskops.get(zodiac=zodiac).description == "new"
        else:
            assert str(response.data['zodiac']) == "[ErrorDetail(string='horoskop model с таким zodiac уже существует.', code='unique')]"    

    # Тест на "HoroskopUpdateTransit", (get) только admin
    def test_horoskop_update_transit(self):
        zodiac = "TAURUS"
        self.test_post_tokens()
        token_admin = self.token_admin 
        response = self.client.get(
            reverse('horoskop-update-transit', kwargs = {'zodiac':zodiac}),
            **{'HTTP_AUTHORIZATION': f'Bearer {token_admin}'},)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Тест на "HoroskopUpdate", (patch) только admin
    def test_horoskop_update(self):
        zodiac = "TAURUS"
        self.test_post_tokens()
        desc_1 = models.HoroskopModel.objects.get(zodiac=zodiac).description
        token_admin = self.token_admin 
        response = self.client.patch(
            reverse('horoskop-update', kwargs = {'zodiac':zodiac}),
            **{'HTTP_AUTHORIZATION': f'Bearer {token_admin}'},
            data = {'description':'new description'})
        # import pdb; pdb.set_trace()
        desc_2 = models.HoroskopModel.objects.get(zodiac=zodiac).description
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert desc_1 != desc_2


    # Тест на "OneHoroskopDelete", (delete) return Redirect - только admin
    def test_horoskop_update_transit(self):
        zodiac = "TAURUS1"
        horoskop_first_count = len(models.HoroskopModel.objects.all())
        self.test_post_tokens()
        token_admin = self.token_admin 
        response = self.client.delete(
            reverse('horoskop-delete', kwargs = {'zodiac':zodiac}),
            **{'HTTP_AUTHORIZATION': f'Bearer {token_admin}'},)

        if response.status_code == 204:
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            horoskops = models.HoroskopModel.objects.all()        
            assert len(horoskops) == (horoskop_first_count-1)
        else:
            assert str(response.data) == "{'detail': ErrorDetail(string='Страница не найдена.', code='not_found')}"

