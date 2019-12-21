import datetime
from bs4 import BeautifulSoup
import requests
from fixture import models

#-----Current Date----------
Current_Date_Formatted = datetime.datetime.today().strftime ('%d%m%Y')
Current_Date_Formatted = Current_Date_Formatted[4:]+Current_Date_Formatted[2:4]+Current_Date_Formatted[:2]

link = "https://www.espn.in/football/fixtures/_/date/"+Current_Date_Formatted
source = requests.get(link).text
soup = BeautifulSoup(source,'lxml')

links = []
hToh = []
heading = soup.find_all("h2")
for head in heading:
    for a in head.nextSibling.find_all("span",{"class","record"}):
        links.append(a.find("a")['href'])

for link in links:
    a = link[0:10] + "matchstats" +  link[link.find("?"):]
    hToh.append("https://www.espn.in"+a)

count = 1
d = []
previousRecord = []

for link in hToh:


    source = requests.get(link).text
    soup = BeautifulSoup(source,'lxml')
    
    divHome = soup.findAll("div",{"id":"gamepackage-team-form-home"})
    divAway = soup.find("div",{"id":"gamepackage-team-form-away"})
    
    previousRecord=[]
    for tr in divHome:
        for td in tr.findAll("tr"):
            try:
                previousRecord.append(td.find("td").text)
            except:
                pass
            try:
                for team in td.findAll("span",{"class":"long-name"}):
                    previousRecord.append(team.text)
            except:
                pass
            try:
                previousRecord.append(td.find("a",{"class":"webview-internal"}).text)
            except:
                pass
            try:
                for img in td.findAll("img"):
                    previousRecord.append(img['data-default-src'])
            except:
                pass
            try:
                for team in td.findAll("span",{"class":"game-date"}):
                    previousRecord.append(team.text)
            except:
                pass
            try:
                for team in td.findAll("td",{"class":"competition"}):
                    previousRecord.append(team.text)
            except:
                pass
    d.append(previousRecord)
    try:
        previousRecord=[]
        for td in divAway.findAll("tr"):     
            try:
                previousRecord.append(td.find("td").text)
            except:
                pass
            try:
                for team in td.findAll("span",{"class":"long-name"}):
                    previousRecord.append(team.text)
            except:
                pass
            try:
                previousRecord.append(td.find("a",{"class":"webview-internal"}).text)
            except:
                pass
            try:
                for img in td.findAll("img"):
                    previousRecord.append(img['data-default-src'])
            except:
                pass
            try:
                for team in td.findAll("span",{"class":"game-date"}):
                    previousRecord.append(team.text)
            except:
                pass
            try:
                for team in td.findAll("td",{"class":"competition"}):
                    previousRecord.append(team.text)
            except:
                pass
    except:
        pass
    d.append(previousRecord)
    count+=1
    
c = []
l = []
count = 1
flag = False
for i in d:
    if(i != []):
        for j in i:
            if(len(j) == 1):
                l = [count]
                l.append(j)
            else:
                l.append(j)
            
            if(len(l) == 9):
                c.append(l)
    if(flag):
        count+=1
        flag = False
    else:
        flag = True

def DataIntoDatabase():
    for i in c:
        models.PrevRecord.objects.create(
            Number = i[0],
            Result = i[1],
            HomeTeam = i[2],
            HImage = i[5],
            Goal = i[4],
            AwayTeam = i[3],
            AImage = i[6],
            Date = i[7],
            Tournament = i[8]
        )
        

	

