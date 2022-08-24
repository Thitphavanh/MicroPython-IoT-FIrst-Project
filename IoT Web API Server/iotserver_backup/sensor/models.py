from django.db import models
from django.db import models


class SensorTempHumid(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True, blank=True)
    temperature = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)
    humidity = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
