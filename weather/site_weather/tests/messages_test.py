from rest_framework.test import APIRequestFactory, APITestCase
from site_weather import models
from django.urls import reverse
from rest_framework import status
from rest_framework.test import force_authenticate
from rest_framework.test import APIClient

class MessageTestCase(APITestCase):
    fixtures=['dump_data'] 

    # Создание токена
    def test_post_tokens(self):
        url = reverse('token_obtain_pair')

        user = models.User.objects.get(id=13)
        user_username = user.username
        token = (self.client.post(url,data={'username':user_username, 'password':user_username})).data['access']
        self.token = token
        self.user=user
        self.username = user_username
        
        user_admin = models.User.objects.get(id=1)
        user_username_admin = user_admin.username
        token_admin = (self.client.post(url,data={'username':user_username_admin, 'password':user_username_admin})).data['access']
        self.token_admin = token_admin
        self.user_admin=user_admin
        

# "MessageView",
#     "",
#     "MessageViewHTML",


    # Тест на "MessageDelite", (delete)
    def test_user_delete_transit(self):
        message_first_count = len(models.MessagesUserModel.objects.all())
        self.test_post_tokens()
        token = self.token 
        response = self.client.delete(
            reverse('message-delete', kwargs = {'id':1}),
            **{'HTTP_AUTHORIZATION': f'Bearer {token}'},)

        if response.status_code == 204:
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            messages = models.MessagesUserModel.objects.all()        
            assert len(messages) == (message_first_count-1)
        else:
            assert str(response.data) == "{'detail': ErrorDetail(string='Страница не найдена.', code='not_found')}"  

            # message-view-get# "MessageView

    # Тест на "MessageView" (get) 
    def test_message_view_transit(self):
        self.test_post_tokens()
        token_admin = self.token_admin 
        response = self.client.get(
            reverse('message-view-get'),
            **{'HTTP_AUTHORIZATION': f'Bearer {token_admin}'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Тест на "MessageView" (post)
    def test_message_create(self):
        self.test_post_tokens()
        token = self.token 
        username = self.username
        message_first_count = len(models.MessagesUserModel.objects.all())        
        # author_message = 'admin'
        response = self.client.post(
            reverse('message-view-post', kwargs = {'username':username}),
            **{'HTTP_AUTHORIZATION': f'Bearer {token}'},
            data={'message':'new'}, 
        )
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_302_FOUND )
        messages = models.MessagesUserModel.objects.all()        
        assert len(messages) == (message_first_count+1)
        
