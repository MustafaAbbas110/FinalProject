from bs4 import BeautifulSoup
import requests
from . import models as database

class NewsScraping:
    def __init__(self):
        link = "https://www.fifa.com/news/"
        source = requests.get(link).text
        self.soup = BeautifulSoup(source,'lxml')
        
    def Scraping(self):
        self.images = []
        self.captionContent = []
        self.captionHeading = []

        span = self.soup.findAll("span", {"class": "fmi__image"})
        for image in span:
            self.images.append(image.find("source")['data-srcset'])
        hList = []
        span = self.soup.findAll("span", {"class": "fmi__caption"})
        for caption in span:
            hList.append(caption.text.strip())
            self.captionHeading.append(caption.find("strong").text.strip())
        
        for i in hList:
            self.captionContent.append(i[i.find("\n")+6:].strip())
            
    def Data(self):
        newsData = {}
        newsData["Heading"] = []
        newsData["Content"] = []
        newsData["Images"] = []
        for i in range(len(self.captionContent)):
            newsData["Heading"].append(self.captionHeading[i])
            newsData["Content"].append(self.captionContent[i])
            newsData["Images"].append(self.images[i])
            
        return newsData



def NewsCollection():   
    obj = NewsScraping()
    obj.Scraping()
    #-- News Scraping --#
    NewsData = obj.Data()

    #-- Delete Previous Record--#
    for x in database.NewsFeed.objects.all().iterator(): 
	    x.delete()

    #-- Insert into Databae --# 
    for index in range(len(NewsData["Heading"])):
        database.NewsFeed.objects.create(Heading = NewsData["Heading"][index],
                            Content = NewsData["Content"][index],
                            Images = NewsData["Images"][index],)

   
