from django.db import models



#-- News Table
class NewsFeed(models.Model):
    Heading = models.CharField(max_length=200)
    Content = models.CharField(max_length=200)
    Images = models.CharField(max_length=200)





