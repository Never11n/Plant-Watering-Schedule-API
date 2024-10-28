from django.db import models
from django.contrib.auth import get_user_model


class Plant(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    watering_frequency_days = models.PositiveSmallIntegerField()
    last_watered_date = models.DateField()

    def __str__(self):
        return self.name