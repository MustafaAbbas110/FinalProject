import datetime
from bs4 import BeautifulSoup
import requests
from fixture.models import schedule 

#-----Previous and Next 7 Date Extracter----------
dateLink = []
for num in range(-7,8):
    d = datetime.datetime.today() + datetime.timedelta(days=num)
    d = d.strftime ('%d%m%Y')
    d = d[4:]+d[2:4]+d[:2]
    dateLink.append(d)


def dataExtraction(soup,d):
    mainData = []
    data = []
    index = 0
    div = soup.find("div",{"id":"sched-container"})
    tables = div.findAll("table",{"class":"schedule"})
    h2 = div.findAll("h2",{"class":"table-caption"})
    
    for table in tables:
        #--- Heading ----
        try:

            heading = h2[index].text.replace(" ","-")
            index += 1
        except:
            pass
        #--- Data Collection ---
        for tr in table:
            for tds in tr.findAll("tr"):
                data.append(heading)
                for num,td in enumerate(tds.findAll("td")):
                    if(num == 0 or num == 1):
                        for span in td.findAll("span"):
                            if(span.find("img") != None):
                                data.append(span.find("img")['src'])
                            else:
                                data.append(span.text)
                    elif(num == 2):
                        try:
                            data.append(td["data-date"][11:-1])
                        except:
                            data.append(td.text)                 
                    elif(num == 3):
                        if(td.text != ""):
                            data.append(td.text)
                        else:
                            data.append("-")
                    elif(num == 4):
                        if(td.text != ""):
                            data.append(td.text)
                        else:
                            data.append("-")
                
                if(len(data) > 1):
                    save = datetime.date(int(d[:4]),int(d[4:6]),int(d[6:]))
                    data.append(save)
                    if(len(data) != 10):
                        data.pop()
                        data.append("-")
                        data.append(save)

                    mainData.append(data)
                data = []
    
    for x in mainData:
        
        obj = schedule.objects.create(
                                    tournment = x[0],
                                    HomeTeam = x[1],
                                    HomeImage = x[2],
                                    status = x[3],
                                    AwayImage = x[4],
                                    AwayTeam = x[5],
                                    Time = x[6],
                                    Ground = x[7],
                                    Attendence = x[8],
                                    exDate  = x[9],
                                )
        obj.save()
        
    
    
for d in dateLink:
    link = "https://www.espn.in/football/fixtures/_/date/"+d
    source = requests.get(link).text
    soup = BeautifulSoup(source,'lxml')
    dataExtraction(soup,d)