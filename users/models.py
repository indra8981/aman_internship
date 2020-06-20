from datetime import datetime

from django.db import models


# Create your models here.


class ActivityPeriod(models.Model):
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)


class User(models.Model):
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=200)
    activity_periods = models.ManyToManyField(ActivityPeriod)



