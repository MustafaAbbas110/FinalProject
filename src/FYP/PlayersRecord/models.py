from django.db import models

class PlayersStats(models.Model):
	playerImage = models.CharField(max_length=200)
	playerFlag = models.CharField(max_length=200)
	playerName = models.CharField(max_length=200)
	country = models.CharField(max_length=200)
	goalScored = models.CharField(max_length=200)
	attempts = models.CharField(max_length=200)
	matchPlayed = models.CharField(max_length=200)
	totalPasses = models.CharField(max_length=200)
	yellowCards = models.CharField(max_length=200)
	RedCards = models.CharField(max_length=200)