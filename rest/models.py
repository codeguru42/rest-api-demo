from django.contrib.auth.models import User
from django.db import models
from django.db.models import DO_NOTHING


class BaseballCard(models.Model):
    autographed = models.BooleanField(default=False)
    condition = models.CharField(max_length=32)
    brand = models.CharField(max_length=32)
    year = models.IntegerField()
    number = models.CharField(max_length=32)
    value = models.DecimalField(null=True, max_digits=20, decimal_places=2)
    quantity = models.IntegerField()
    player = models.CharField(max_length=32)
    team = models.CharField(max_length=32)
    position = models.CharField(max_length=32)
