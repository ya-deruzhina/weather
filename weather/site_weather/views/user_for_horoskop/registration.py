from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from site_weather.forms import RegisterHoroskopForm 
from site_weather.serializers import RegisterUserSerializer
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from site_weather.models import User



class HoroskopRegistrationView(APIView):
    def get (self, request):
        template = loader.get_template("auth/register_horoskop.html")
        context = {
            "form":RegisterHoroskopForm()
        }
        return HttpResponse(template.render(context,request))

    def post(self,request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get (username = request.data['username'])
        pas = request.data['password']
        passw = make_password(pas)
        user.password = passw
        user.save() 
        return HttpResponseRedirect ("/weather/horoskop/")