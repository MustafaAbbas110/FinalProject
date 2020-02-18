from django.shortcuts import render
from prediction import predic
from sklearn.linear_model import LogisticRegression
from sklearn.tree  import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.calibration import CalibratedClassifierCV
from sklearn.svm import LinearSVC



data=predic.ModelSelection(RandomForestClassifier)


def matchPred(request):	
	'''
	try:
		MLmodel = str(request.POST.get('Submit'))
		data = predic.ModelPass(MLmodel)
	except:	
		data = predic.ModelPass(RandomForestClassifier)
	'''
	context={
		"data":data,
	}
	
	
	
	return render(request,"prediction/Records.html",context)
	
