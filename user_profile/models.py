from django.db import models
from scenarios.models import Scenario
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    scenarios_played = models.IntegerField(default=0)


class LoggedPlay(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
