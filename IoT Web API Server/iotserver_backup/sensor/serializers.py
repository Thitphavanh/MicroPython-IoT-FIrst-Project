from rest_framework import serializers
from .models import *

class SensorTempHumidSerializer(serializers.ModelSerializer):
	class Meta:
		model = SensorTempHumid
		fields = ('id','code','name','temperature','humidity')