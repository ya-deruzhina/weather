# Register your models here.
from django.contrib import admin
from .models import *


class MessageInline(admin.TabularInline):
    model = MessagesUserModel
    list_display = ["author_message", "message"]
    ordering = ["-date_create"]

@admin.register(User)
class UserAdmin (admin.ModelAdmin):
    fields = ["username","user_zodiac"]
    list_display = ["username", "user_zodiac","new_message"]
    search_fields = ["username"]
    ordering = ["username"]
    list_filter = ["user_zodiac"] 
    inlines = [MessageInline]

    def new_message (self,obj:User):
        message = MessagesUserModel.objects.filter(user_page_id=obj.id)
        mes = message.filter(new=True)
        return len(mes)



@admin.register(Weather)
class WeatherAdmin (admin.ModelAdmin):
    list_display = ["city", "date"]
    ordering = ["city","-date"]
    list_filter = ["city", "date"] 

@admin.register(HoroskopModel)
class HoroskopModelAdmin (admin.ModelAdmin):
    list_display = ["zodiac", "description", "date_create_zodiac"]
    ordering = ["zodiac"]