from django.shortcuts import render
from fifaRecords import models






session = models.Results.objects.values("Session")

l = []
for i in session:
	l.append(i['Session'])
l = list(dict.fromkeys(l))








def Records(request):
    a = ["Brazil", "Italy", "Germany", "Uruguay", "Argentina", "France","England", "Spain"]
    b = [5, 4, 4, 2, 2, 2, 1, 1]
    values = (a,b)
    print(values)
    s = "2018"
    try:
        s = str(request.POST.get('Submit'))
    except:
        pass
    data = models.Results.objects.filter(Session=s)
    print(type(s))
    try:
        int(s)
        values = Top5MaxWinner(data)
    except:
        pass

    context = {
        "data":data,
        "Session":l,
        "s":s,
		"winner":values[0],
		"goals":values[1],
    }

    return render(request , "fifaRecords\Records.html",context)
	
	
def Top5MaxWinner(data):
	winner = []
	goals = []
	
	for i in data:
	    if(i.Score[0] > i.Score[2]):
		    winner.append(i.HomeTeam)
	    else:
		    winner.append(i.AwayTeam)
			
	my_dict = {i:winner.count(i) for i in winner}
	import operator
	sorted_d = sorted(my_dict.items(), key=operator.itemgetter(1),reverse=True)
	w = []
	g = []
	
	for i in sorted_d:
		w.append(i)
		
	w = w[:8]
	win = []
	goal = []
	c = 0
	for i in w:
		win.append(i[0])
		goal.append(i[1])
		
	return (win,goal)
	