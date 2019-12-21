from django.shortcuts import render
from fifaRecords import models






session = models.Results.objects.values("Session")
l = []
for i in session:
	l.append(i['Session'])
l = list(dict.fromkeys(l))









def Records(request):

    s = "2018"
    try:
        s = str(request.POST.get('Submit'))
    except:
        pass
    data = models.Results.objects.filter(Session=s)
    print(s)
    context = {
        "data":data,
        "Session":l,
        "s":s,
    }

    return render(request , "fifaRecords\Records.html",context)