from django.urls import path
from site_weather.views import *
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )


urlpatterns = [
    # Weather
    path("",ChoiseWeatherView.as_view()),
    path("<int:weather_id>/",OneWeatherView.as_view(),name='weather-one'),
    path("base/",WeatherView.as_view(),name='weather-base'),
    path("update/",WeatherUpdateView.as_view()),

    # Horoskop до авторизации
    path("horoskop/",HoroskopFirstPageView.as_view()),  

    # Registrate and Authorizate in Horoskop
    path("horoskop/autorization/",HoroskopAutorizationView.as_view()),
    path("horoskop/registration/",HoroskopRegistrationView.as_view()),

    # Autorization
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Horoskop после авторизации
    path("horoskop/base/",HoroskopBaseAfterAuthView.as_view(), name='horoskop-base'),

    # User
    path("horoskop/user_view/",UserView.as_view(),name='user-view'),
    path("horoskop/user_update/tranzit/",UserUpdateTransitView.as_view(),name='user-update-tranzit'),
    path("horoskop/user_update/<str:username>/",UserUpdateView.as_view(), name='user-update'),
    path("horoskop/user_delete/<str:username>/",UserDeleteView.as_view(),name='user-delete'),
    
    # Сообщения без авторизации, с главной
    path("horoskop/message/<str:username>/",MessageViewHTML.as_view()),
    path("horoskop/message/create/<str:username>/",MessageViewHTML.as_view(),name='message-view-post'),
    
    # Сообщения после авторизации
    path("horoskop/message/",MessageView.as_view(),name='message-view-get'),
    path("horoskop/message/create/",MessageView.as_view()),
    path("horoskop/message/delete/<int:id>/",MessageDelite.as_view(),name='message-delete'),

    # Гороскоп
    path("horoskop/all/",HoroskopAll.as_view(),name='horoskop-list'),
    path("horoskop/create/",HoroskopCreateTransit.as_view(), name='horoskop-create-transit'),
    path("horoskop/zodiac/<str:zodiac>/",HoroskopOne.as_view(), name='horoskop-one'),
    path("horoskop/zodiac/delete/<str:zodiac>/",OneHoroskopDelete.as_view(),name='horoskop-delete'),

    path("horoskop/zodiac/up_date/<str:zodiac>/",HoroskopUpdateTransit.as_view(), name='horoskop-update-transit'),
    path("horoskop/zodiac/update/<str:zodiac>/",HoroskopUpdate.as_view(),name='horoskop-update'),

   

    

]