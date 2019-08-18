from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Club(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100, default = '')
    city = models.CharField(max_length = 50, default = '')
    website = models.CharField(max_length = 50, default = '')
    phone = models.IntegerField(default = 0)


class Deals(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    description = models.CharField(max_length = 255, default = '')
    startTime = models.DateTimeField(default = timezone.now)
    endTime = models.DateTimeField()
    code = models.CharField(max_length = 15, default = '')
