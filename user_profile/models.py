from django.db import models
from scenarios.models import Scenario, Expansion
from django.contrib.auth.models import User
from django.utils import timezone

from datetime import timedelta


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    scenarios_played = models.IntegerField(default=0)

    def get_num_scenarios_last_week(self):
        one_week_ago = timezone.now().date() - timedelta(days=7)
        tommorow = timezone.now().date() + timedelta(days=7)
        # Use tomorrow because the bound is "0am on the given date"
        return len(self.loggedplay_set.filter(date__range=(one_week_ago, tommorow)))

    def get_num_scenarios_this_month(self):
        return len(self.loggedplay_set.filter(date__month=timezone.now().month))

    def get_num_scenarios_this_year(self):
        return len(self.loggedplay_set.filter(date__month=timezone.now().year))

    def get_list_expansions_completed(self):
        expansions_completed = []
        for expansion in Expansion.objects.all():
            # Check if the number of scenarios the user has played for an expansion equals the total scenarios for
            # that expansion
            if len(self.loggedplay_set.filter(scenario__expansion=expansion)) == len(expansion.scenario_set.all()):
                expansions_completed.append(expansion)
        return expansions_completed

    def get_list_expansions_uncompleted(self):
        expansions_uncompleted = []
        for expansion in Expansion.objects.all():
            expansion_plays = len(self.loggedplay_set.filter(scenario__expansion=expansion))
            expansion_scenarios = len(expansion.scenario_set.all())
            if expansion_plays != expansion_scenarios:
                expansions_uncompleted.append(expansion.name + " (" + str(expansion_plays) + "/" + str(expansion_scenarios) + ")")
        return expansions_uncompleted


class LoggedPlay(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
