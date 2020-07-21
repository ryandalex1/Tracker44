from django.db import models


class Scenario(models.Model):
    name = models.CharField(max_length=50)
    expansion = models.CharField(max_length=15)
    number = models.CharField(max_length=15)

    board_types = (
        (1, "Beach"),
        (2, "Winter"),
        (3, "Desert"),
        (4, "Field")
    )
    board = models.IntegerField(choices=board_types)
