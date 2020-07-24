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

    board_types = (
        (1, "Beach"),
        (2, "Winter"),
        (3, "Desert"),
        (4, "Countryside")
    )
    board = models.IntegerField(choices=board_types)
