from django.views import View
from django.template import loader
from django.http import HttpResponse
from site_weather.forms import AuthHoroskopForm 


class HoroskopAutorizationView(View):
    def get (self, request):
        template = loader.get_template("auth/auth_horoskop.html")
        context = {
            "form":AuthHoroskopForm()
        }
        return HttpResponse(template.render(context,request))