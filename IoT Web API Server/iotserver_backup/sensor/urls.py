from django.urls import path
from .views import *

urlpatterns = [
    path('', Home),
    path('sensor-post',api_post_sensortemphumid)
]
