from site_weather.models import HoroskopModel
from site_weather.serializers import HoroskopSerializer
from site_weather.forms import CreateHoroskopForm,UpdateHoroskopForm

from django.http import HttpResponse,HttpResponseRedirect 
from django.views import View
from django.template import loader

from rest_framework import generics
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Страничка гороскопа
class HoroskopOne (generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = HoroskopModel.objects.all()
    serializer_class = HoroskopSerializer
    lookup_field = 'zodiac'
    lookup_url_kwarg = 'zodiac'

# Создать новый гороскоп
class HoroskopCreateTransit(APIView):
    permission_classes = [IsAdminUser]
    def get (self, request):
        template = loader.get_template("horoskop/create_horoskop.html")
        context = {
            "form":CreateHoroskopForm()
        }
        return HttpResponse(template.render(context,request))
    
    def post(self,request):
        # import pdb; pdb.set_trace()
        serializer = HoroskopSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponseRedirect ("/weather/horoskop/all/")

# Обновление description гороскопа
# Работает через Постмэн и запрос Patch  
class HoroskopUpdate(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = HoroskopModel.objects.all()    
    serializer_class = HoroskopSerializer
    lookup_field = 'zodiac'
    lookup_url_kwarg = 'zodiac'

# Транзит для Update
class HoroskopUpdateTransit(View):
    permission_classes = [IsAdminUser]
    def get (self,request,zodiac):
        horoskop = HoroskopModel.objects.get(zodiac=zodiac)
        template = loader.get_template("horoskop/horoskop_update.html")
        context = {
            "horoskop":horoskop,
            "form":UpdateHoroskopForm()
        }
        return HttpResponse(template.render(context,request))
    

# Удаление одной карточки - через Постмэн
class OneHoroskopDelete (generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = HoroskopModel.objects.all()    
    serializer_class = HoroskopSerializer
    lookup_field = 'zodiac'
    lookup_url_kwarg = 'zodiac'