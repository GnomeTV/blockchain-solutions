from django.db import models


class Block(models.Model):
    height = models.IntegerField()
    hash = models.TextField()
    time = models.DateTimeField()
    miner = models.TextField()
    transactions = models.IntegerField()
