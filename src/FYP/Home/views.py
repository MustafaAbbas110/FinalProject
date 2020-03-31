from django.shortcuts import render
from Home import NewsScraping
from Home import models

#-- News Data Collection --#
NewsScraping.NewsCollection()
NewsData = models.NewsFeed.objects.all()


Context = {
    "NewsData":NewsData,
}


def Home(request):
    return render(request , "Home/index.html",Context)
