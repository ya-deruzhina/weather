from django.views import View
from django.template import loader
from django.http import HttpResponse
from site_weather.forms import UpdateUserForm 
from site_weather.models import User
from site_weather.serializers import RegisterUserSerializer
from rest_framework import generics
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

# View
class UserView(APIView):
    permission_classes = [IsAuthenticated]
    def get (self,request):
        user_id = request.auth['user_id']
        user = User.objects.get(id=user_id)
        template = loader.get_template("user/user.html")
        context = {
            "user" : user
        }
        return HttpResponse(template.render(context,request))

# Transit Update
class UserUpdateTransitView(APIView):
    permission_classes = [IsAuthenticated]
    def get (self, request):
        user_id = request.auth['user_id']
        user = User.objects.get(id=user_id).username
        template = loader.get_template("user/user_update.html")
        context = {
            "form":UpdateUserForm(),
            "username" : user
        }
        return HttpResponse(template.render(context,request))


# Update - работает через постман и запрос patch
# возвращает username, password и user_zodiac (потому что эти данные можно менять)
class UserUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()    
    serializer_class = RegisterUserSerializer
    lookup_field = 'username'
    lookup_url_kwarg = 'username'

# Delete - работает через постман с запросом delete
class UserDeleteView (generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()    
    serializer_class = RegisterUserSerializer
    lookup_field = 'username'
    lookup_url_kwarg = 'username'
