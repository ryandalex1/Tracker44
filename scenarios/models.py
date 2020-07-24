from django.db import models


class ExpansionManager(models.Manager):
    def get_by_natural_key(self, abbreviation):
        return self.get(abbreviation=abbreviation)


class SubExpansionManager(models.Manager):
    def get_by_natural_key(self, abbreviation):
        return self.get(abbreviation=abbreviation)


class Expansion(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=25, unique=True)

    objects = ExpansionManager()


class SubExpansion(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=25, unique=True)
    parent = models.ForeignKey(Expansion, on_delete=models.CASCADE)

    objects = SubExpansionManager()


class Scenario(models.Model):
    name = models.CharField(max_length=50)
    expansion = models.ForeignKey(Expansion, on_delete=models.CASCADE)
    sub_expansion = models.ForeignKey(SubExpansion, on_delete=models.CASCADE, blank=True, null=True)
    number = models.CharField(max_length=15)
    date = models.CharField(max_length=25)

    class BoardTypes(models.IntegerChoices):
        COUNTRYSIDE = 1
        WINTER = 2
        DESERT = 3
        BEACH = 4

    board = models.IntegerField(choices=BoardTypes.choices)

    class ScenarioTypes(models.IntegerChoices):
        STANDARD = 1
        OVERLORD = 2
        BREAKTHROUGH = 3
        BREAKLORD = 4

    scenario_type = models.IntegerField(choices=ScenarioTypes.choices)
