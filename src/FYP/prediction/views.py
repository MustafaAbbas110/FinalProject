from django.shortcuts import render
from prediction import predic
from sklearn.linear_model import LogisticRegression
from sklearn.tree  import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier




data=predic.ModelSelection(RandomForestClassifier)




def matchPred(request):	
	'''
	data=predic.ModelSelection(RandomForestClassifier)
	MLmodel = None
	try:
		MLmodel = str(request.POST.get('Submit'))
		if(MLmodel == None):
			raise ValueError("Erorr")
		if(MLmodel == "LogisticRegression"):
			data = data1
		elif(MLmodel == "RandomForestClassifier"):
			data = data2
	except:	
		data = data2
	'''
	
	context={
		"data":data,
	}
	
	
	
	return render(request,"prediction/Records.html",context)
	
