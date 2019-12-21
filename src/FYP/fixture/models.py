from django.db import models

class schedule(models.Model):
    tournment = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    HomeTeam = models.CharField(max_length=200)
    AwayTeam = models.CharField(max_length=200)
    HomeImage = models.CharField(max_length=200)
    AwayImage = models.CharField(max_length=200)
    Date = models.CharField(max_length=200)
    Time = models.CharField(max_length=200)
    Ground = models.CharField(max_length=200)
    Attendence = models.CharField(max_length=200)
    exDate = models.DateField()

class PrevRecord(models.Model):
	Number = models.CharField(max_length=50)
	Result = models.CharField(max_length=50)
	HomeTeam = models.CharField(max_length=50)
	HImage = models.CharField(max_length=50)
	Goal = models.CharField(max_length=50)
	AwayTeam = models.CharField(max_length=50)
	AImage = models.CharField(max_length=50)
	Date = models.CharField(max_length=10)
	Tournament = models.CharField(max_length=100)
	