from datetime import datetime, timedelta

from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    watering_frequency_days = models.PositiveSmallIntegerField()
    last_watered_date = models.DateField()

    @property
    def next_watering_date(self):
        return self.last_watered_date + timedelta(days=self.watering_frequency_days)

    @property
    def is_need_be_watered(self):
        return True if self.next_watering_date <= datetime.now().date() else False

    def __str__(self):
        return self.name