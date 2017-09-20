from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=30)
    city_pin_start = models.IntegerField()
    city_pin_end = models.IntegerField()
