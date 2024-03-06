from site_weather.views.weather.weather import WeatherView, ChoiseWeatherView, WeatherUpdateView
from site_weather.views.weather.one_page_weather import OneWeatherView
from site_weather.views.horoskop.horoskop import HoroskopFirstPageView, HoroskopAll
from site_weather.views.user_for_horoskop.autorization import HoroskopAutorizationView
from site_weather.views.user_for_horoskop.registration import HoroskopRegistrationView
from site_weather.views.user_for_horoskop.user import UserUpdateView, UserView,UserDeleteView,UserUpdateTransitView
from site_weather.views.horoskop.horoskop_for_one import HoroskopOne,HoroskopCreateTransit,HoroskopUpdate,HoroskopUpdateTransit,OneHoroskopDelete
from site_weather.views.horoskop.horoskop_after_auth import HoroskopBaseAfterAuthView
from site_weather.views.messages.message import MessageView,MessageDelite, MessageViewHTML
 

all = (
    "WeatherView",
    "OneWeatherView",
    "ChoiseWeatherView",
    "HoroskopFirstPageView",
    "HoroskopAutorizationView",
    "HoroskopRegistrationView",
    "UserUpdateView",
    "HoroskopAll",
    "HoroskopCreateTransit",
    "HoroskopUpdate",
    "HoroskopUpdateTransit",
    "HoroskopOne",
    "OneHoroskopDelete",
    "HoroskopBaseAfterAuthView",
    "UserView",
    "UserDeleteView",
    "MessageView",
    "MessageDelite",
    "WeatherUpdateView",
    "MessageViewHTML",
    "UserUpdateTransitView",
)
