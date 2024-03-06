from site_weather.models import MessagesUserModel,User
from site_weather.serializers import MessagesSerializer
from site_weather.forms import CreateMessageForm

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Посмотреть все (рядом удалить)
# Написать новое
# Авторизованные
class MessageView(APIView):
    # Страница со всеми сообщения + оставить новое
    permission_classes = [IsAuthenticated]
    def get(self,request):
        id_user = request.auth['user_id']
        username = User.objects.get(id=id_user).username
        message = MessagesUserModel.objects.filter(user_page_id=id_user).order_by('date_create')
        template = loader.get_template("message/messages_main.html")
        context = {
            "messages":message,
            "form":CreateMessageForm(),
            "username":username
        }
        return HttpResponse(template.render(context,request))
   
    def post(self,request):
        id_user = request.auth['user_id']
        username = User.objects.get(id=id_user).username
        message = request.POST.get('message')
        author_message=request.POST.get('author_message',username)
        messages = MessagesUserModel(message=message, user_page_id = id_user,author_message=author_message)
        messages.save()
        return HttpResponseRedirect ("")

class MessageViewHTML(APIView):
    # Страница со всеми сообщения + оставить новое
    def get(self,request,username):
        id_user = User.objects.get(username=username).id
        message = MessagesUserModel.objects.filter(user_page_id=id_user).order_by('date_create')
        template = loader.get_template("message/messages_main_html.html")
        context = {
            "messages":message,
            "form":CreateMessageForm(),
            "username":username
        }
        return HttpResponse(template.render(context,request))
   
    def post(self,request,username):
        id_user = User.objects.get(username=username).id
        message = request.POST.get('message')
        author_message=request.POST.get('autor_message',username)
        messages = MessagesUserModel(message=message, user_page_id = id_user,author_message=author_message)
        messages.save()
        return HttpResponseRedirect ("")
    

# Удаление одной карточки - через Постмэн
# Здесь нету авторизации, потому что можно перейти с главной тоже
class MessageDelite (generics.DestroyAPIView):
    queryset = MessagesUserModel.objects.all()    
    serializer_class = MessagesSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'