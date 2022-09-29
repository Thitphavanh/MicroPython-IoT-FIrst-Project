from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home-page'),
    path('about/', About, name='about-page'),
    path('sensor/', Sensor, name='sensor-page'),
    path('history/', History, name='history-page'),
    path('contact/', Contact, name='contact-page'),
    path('api', api_post_sensor)
]
