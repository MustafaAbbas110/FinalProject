from django.shortcuts import render
from PlayersRecord.models import PlayersStats 

import pandas as pd


data = PlayersStats.objects.all()


country=[]
flag= []
for i in data:
	flag.append(i.playerFlag)
	country.append(i.country)


flag = list(dict.fromkeys(flag))
country = list(dict.fromkeys(country))



	

def PlayersRecord(request):
	s = "Argentina"


	s = str(request.POST.get('Submit'))
	print(s)
	dataCountry = PlayersStats.objects.filter(country=s)
	print(dataCountry)
	temp = Top5MaxWinner(data)

	values = Top5MaxWinner(dataCountry)
	a = ([],[])
	if(values == a):
		values = temp

	context = {
	"data":data,
	"flag":flag,
	"country":country,
	"dataCountry":dataCountry,
	"s":s,
	"players":values[0],
	"goals":values[1],
}
	


	return render(request , "PlayersRecord\Players.html",context)
	
	
def Top5MaxWinner(data):
	players = []
	goals = []
	
	for i in data:
		goals.append(i.goalScored)
		players.append(i.playerName)
			
	dataPlayer = {}
	c = 0
	
	for i in players:
		dataPlayer[i] = goals[c]
		c+=1
	
	import operator
	sorted_d = sorted(dataPlayer.items(), key=operator.itemgetter(1),reverse=True)

	w = []
	g = []
	
	for i in sorted_d:
		w.append(i)
		
	w = w[:5]
	win = []
	goal = []
	c = 0
	for i in w:
		win.append(i[0])
		goal.append(i[1])
		
	return (win,goal)
	