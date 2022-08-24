from django.contrib import admin
from .models import *


class Show_data(admin.ModelAdmin):
	list_display = ['id','timestamp']

admin.site.register(SensorTempHumid, Show_data)

