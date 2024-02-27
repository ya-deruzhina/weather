from django.views import View
from site_weather.models import HoroskopModel, User
from django.template import loader
from django.http import HttpResponse
from rest_framework.views import APIView
from site_weather.serializers import HoroskopSerializer
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

class HoroskopFirstPageView(View):
    # Первая страница авторизации
    def get (self, request):
        template = loader.get_template("auth/main_auth_page.html")
        return HttpResponse(template.render(request))
    
    
class HoroskopAll(APIView):
    # Выводит все гороскопы на экран
    permission_classes = [IsAuthenticated]
    def get (self,request,format=None):    
        user_id = request.auth['user_id']
        username = User.objects.get(id=user_id).username
        if username == 'admin':
            horoskop = HoroskopModel.objects.all()
            template = loader.get_template("horoskop/view_all.html")
            context = {
                "horoskop":horoskop
            }
            return HttpResponse(template.render(context,request))
        else:
            working_services = [HoroskopSerializer (instance=working_service).data for working_service in HoroskopModel.objects.all()]
            return Response ({'horoskop':working_services})

    

