from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home-page'),
    path('about/', About, name='about-page'),
    path('sensor/', Sensor, name='sensor-page'),
    path('history/', History, name='history-page'),
    path('contact/', Contact, name='contact-page'),
    path('api', api_post_sensor),
    path('test-sensor/', TestShowSensor),
    path('sensor-list/', Sensor_list),
    path('sensor-list-data/', Sensor_list_data),
    path('sensor-current-single/<str:CODE>/', Senor_current_single),
    path('sensor-current-multiple/<str:CODE>/',Sensor_current_multiple),
    path('sensor-current-multiple-post/<str:CODE>', Senor_current_multiple_post),

]
