from rest_framework.test import APIRequestFactory, APITestCase
from site_weather import models
from django.urls import reverse
from rest_framework import status
from rest_framework.test import force_authenticate
from rest_framework.test import APIClient


class UserTestCase(APITestCase):
    fixtures=['dump_data'] 

    # Создание токена
    def test_post_tokens(self):
        url = reverse('token_obtain_pair')

        user = models.User.objects.get(id=13)
        user_username = user.username
        token = (self.client.post(url,data={'username':user_username, 'password':user_username})).data['access']
        self.token = token
        self.user=user
        self.username = user.username
        
        user_admin = models.User.objects.get(id=1)
        user_username_admin = user_admin.username
        token_admin = (self.client.post(url,data={'username':user_username_admin, 'password':user_username_admin})).data['access']
        self.token_admin = token_admin
        self.user_admin=user_admin
        
        
    # Тест на вывод информации "UserView" (get)
    def test_user_for_user_get(self):
        self.test_post_tokens()
        token = self.token 
        response = self.client.get(
            reverse('user-view'),
            **{'HTTP_AUTHORIZATION': f'Bearer {token}'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Тест на "UserDeleteView", (delete) return Redirect - только admin
    def test_user_delete_transit(self):
        users_first_count = len(models.User.objects.all())
        self.test_post_tokens()
        token = self.token 
        username = self.username
        response = self.client.delete(
            reverse('user-delete', kwargs = {'username':username}),
            **{'HTTP_AUTHORIZATION': f'Bearer {token}'},)

        if response.status_code == 204:
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            horoskops = models.User.objects.all()        
            assert len(horoskops) == (users_first_count-1)
        else:
            assert str(response.data) == "{'detail': ErrorDetail(string='Страница не найдена.', code='not_found')}"   

    # Тест на "UserUpdateTransitView", (get)
    def test_user_update_transit(self):
        self.test_post_tokens()
        token = self.token 
        username = self.username
        response = self.client.get(
            reverse('user-update-tranzit'),
            **{'HTTP_AUTHORIZATION': f'Bearer {token}'},)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

            # "UserUpdateView",

    def test_horoskop_update(self):
        self.test_post_tokens()
        token = self.token 
        username = self.username
        user = models.User.objects.get(username=username)
        username_1 = user.username
        password_1 = user.password
        user_zodiac_1 = user.user_zodiac
        
        response = self.client.patch(
            reverse('user-update', kwargs = {'username':username}),
            **{'HTTP_AUTHORIZATION': f'Bearer {token}'},
            data = {'user_zodiac':'ARIES'})
        user = models.User.objects.get(username=username)
        username_2 = user.username
        password_2 = user.password
        user_zodiac_2 = user.user_zodiac

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert username_1 != username_2 or password_1 != password_2 or user_zodiac_1 != user_zodiac_2