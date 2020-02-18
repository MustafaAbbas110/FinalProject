from django.shortcuts import render
import datetime
from time import ctime
from fixture import models
from fixture.models import schedule

time = ctime()[11:16] == "01:00"

if(False):
	rows = schedule.objects.all()
	for row in rows:
		row.delete()
	from fixture import fixtureScraping


def DataLoadPrevRecord():
	if(False):
		from . import PrevRecordScraping
		for x in models.PrevRecord.objects.all().iterator(): 
			x.delete()
		PrevRecordScraping.DataIntoDatabase()

	number =[]
	for i in models.PrevRecord.objects.all():
		number.append(i.Number)
	number = list(dict.fromkeys(number))

	return (models.PrevRecord.objects.all(),number)



def DailyFixture(request):
	index = 0
	exDate = schedule.objects.values('exDate')
	
	eDate = []
	for i in exDate:
		x = month(str(i['exDate'])[5:7])
		eDate.append(x + "-" +  str(i['exDate'])[8:])
	eDate = list(dict.fromkeys(eDate))
	n = 0
	for i,x in enumerate(range(-7,8)):		
		try:
			num = str(request.POST.get('Submit'))
		except:
			try:
				num = str(request.POST.get('Submit'))
			except:
				break

		if(eDate[i] == num):
			index = i
			n = x
			break

	if(n == 0):
		record = DataLoadPrevRecord()		
	else:
		record = ["-","-"]
	
	d = datetime.datetime.today() + datetime.timedelta(days=n)
	d = d.strftime ('%d%m%Y')
	save = datetime.date(int(d[4:]),int(d[2:4]),int(d[:2]))

	
	tournment = schedule.objects.filter(exDate=save).values('tournment')
	
	tournList = []
	for i in tournment:
		tournList.append(i['tournment'])
	tournList = list(dict.fromkeys(tournList))

	
	
	context={
		"Data":schedule.objects.filter(exDate=save),
		"Tourn":tournList,
		"eDate":eDate,
		'currentDate':eDate[index],
		"record":record[0],
		"number":record[1],
	}

	return render(request,"fixture/index.html",context)


def month(x):
	x = int(x)
	if(x == 1):
		return "JAN"
	elif(x == 2):
		return "FEB"
	elif(x == 3):
		return "MAR"
	elif(x == 4):
		return "APR"
	elif(x == 5):
		return "MAY"
	elif(x == 6):
		return "JUN"
	elif(x == 7):
		return "JUL"
	elif(x == 8):
		return "AUG"
	elif(x == 9):
		return "SEP"
	elif(x == 10):
		return "OCT"
	elif(x == 11):
		return "NOV"
	elif(x == 12):
		return "DEC"