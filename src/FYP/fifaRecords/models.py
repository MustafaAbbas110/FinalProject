from django.db import models

class Results(models.Model):
    HomeTeam = models.CharField(max_length=200)
    HomeImage = models.CharField(max_length=200)
    AwayTeam = models.CharField(max_length=200)
    AwayImage = models.CharField(max_length=200)
    Score = models.CharField(max_length=200)
    Venue = models.CharField(max_length=200)
    Group = models.CharField(max_length=200)
    Session = models.CharField(max_length=200)