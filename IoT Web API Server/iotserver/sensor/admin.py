from django.contrib import admin
from .models import *

# admin.site.register(TempHumid,TempHumidAdmin)

class TempHumidAdmin(admin.ModelAdmin):
	list_display = ['id', 'code', 'title', 'temperature', 'humidity', 'timestamp']

admin.site.register(TempHumid, TempHumidAdmin)

