from site_weather.models import HoroskopModel,User

from django.http import HttpResponse, JsonResponse
from django.template import loader

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class HoroskopBaseAfterAuthView(APIView):
    permission_classes = [IsAuthenticated]
    def get (self, request):
        user_id = request.auth['user_id']
        user = User.objects.get(id=user_id)
        zodiac_user = user.user_zodiac
        username = user.username
        horoskop = HoroskopModel.objects.filter(zodiac=zodiac_user)
        if len(horoskop)==0:
            return JsonResponse ({"Status": "Horoskop Not Created"})
        else:
            horoskop = horoskop[0]
            template = loader.get_template("horoskop/base_after_auth_page.html")
            context = {
                "horoskop":horoskop,
                "username":username
            }
            return HttpResponse(template.render(context,request))