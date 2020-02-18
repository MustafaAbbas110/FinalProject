#!/usr/bin/env python
# coding: utf-8

# In[555]:

def ModelSelection(MLmodel):
	import pandas as pd
	import numpy as np
	from sklearn.model_selection import train_test_split


	# In[556]:


	#load data 
	results = pd.read_csv('datasets/results.csv')



	# In[557]:


	winner = []
	for i in range (len(results['home_team'])):
		if int(results ['home_score'][i]) > int(results['away_score'][i]):
			winner.append(results['home_team'][i])
		elif int(results['home_score'][i]) < int(results ['away_score'][i]):
			winner.append(results['away_team'][i])
		else:
			winner.append('Draw')
	results['winning_team'] = winner

	#adding goal difference column
	results['goal_difference'] = np.absolute(results['home_score'] - results['away_score'])

	results.head()


	# In[558]:


	results = results.drop(['date', 'home_score', 'away_score', 'city', 'goal_difference'], axis=1)
	results.head()


	# In[559]:


	results = results.reset_index(drop=True)
	results.loc[results.winning_team == results.home_team,'winning_team']=2
	results.loc[results.winning_team == 'Draw', 'winning_team']=1
	results.loc[results.winning_team == results.away_team, 'winning_team']=0

	results.head()


	# In[560]:


	#convert home team and away team from categorical variables to continous inputs 
	# Get dummy variables
	final = pd.get_dummies(results, prefix=['home_team', 'away_team'], columns=['home_team', 'away_team'])

	# Separate X and y sets
	X = final.drop(['winning_team'], axis=1)
	y = final["winning_team"]
	y = y.astype('int')

	# Separate train and test sets
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)


	# In[561]:


	final.tail()


	# In[ ]:





	# In[ ]:





	# In[ ]:






	# In[ ]:





	# In[ ]:





	# In[ ]:





	# In[ ]:





	# In[ ]:





	# In[ ]:





	# In[ ]:





	# In[580]:


	from sklearn.linear_model import LogisticRegression
	from sklearn.tree  import DecisionTreeClassifier
	from sklearn.ensemble import RandomForestClassifier
	from sklearn.naive_bayes import GaussianNB
	from sklearn.calibration import CalibratedClassifierCV
	from sklearn.svm import LinearSVC


	# In[581]:


	pred = MLmodel()
	pred.fit(X_train, y_train)
	score = pred.score(X_train, y_train)
	score2 = pred.score(X_test, y_test)

	print("Training set accuracy: ", '%.3f'%(score))
	print("Test set accuracy: ", '%.3f'%(score2))


	# In[582]:


	#adding Fifa rankings
	#the team which is positioned higher on the FIFA Ranking will be considered "favourite" for the match
	#and therefore, will be positioned under the "home_teams" column
	#since there are no "home" or "away" teams in World Cup games. 

	# Loading new datasets
	ranking = pd.read_csv('datasets/fifa_rankings.csv') 
	fixtures = pd.read_csv('datasets/fixtures.csv')

	# List for storing the group stage games
	pred_set = []


	# In[583]:


	# Create new columns with ranking position of each team
	fixtures.insert(1, 'first_position', fixtures['Home Team'].map(ranking.set_index('Team')['Position']))
	fixtures.insert(2, 'second_position', fixtures['Away Team'].map(ranking.set_index('Team')['Position']))

	# We only need the group stage games, so we have to slice the dataset
	fixtures = fixtures.iloc[:48, :]
	print(fixtures)


	# In[584]:


	# Loop to add teams to new prediction dataset based on the ranking position of each team
	for index, row in fixtures.iterrows():
		if row['first_position'] < row['second_position']:
			pred_set.append({'home_team': row['Home Team'], 'away_team': row['Away Team'], 'winning_team': None})
		else:
			pred_set.append({'home_team': row['Away Team'], 'away_team': row['Home Team'], 'winning_team': None})
			
	pred_set = pd.DataFrame(pred_set)
	backup_pred_set = pred_set
	
	df = pd.DataFrame()
	df['away_team'] = pred_set['away_team']
	df['home_team'] = pred_set['home_team']
	df['winning_team'] = pred_set['winning_team']
	pred_set = df
	backup_pred_set = df

	
	print(pred_set)


	# In[585]:


	# Get dummy variables and drop winning_team column
	pred_set = pd.get_dummies(pred_set, prefix=['home_team', 'away_team'], columns=['home_team', 'away_team'])

	# Add missing columns compared to the model's training dataset
	missing_cols = set(final.columns) - set(pred_set.columns)
	for c in missing_cols:
		pred_set[c] = 0
	pred_set = pred_set[final.columns]

	# Remove winning team column
	pred_set = pred_set.drop(['winning_team'], axis=1)

	pred_set.head()


	# In[586]:


	backup_pred_set


	# In[590]:

	data = []
	matchResult = []
	predictions = pred.predict(pred_set)
	for i in range(fixtures.shape[0]):
		d = []
		d.append(backup_pred_set.iloc[i, 1]) 
		d.append(backup_pred_set.iloc[i, 0])
		if predictions[i] == 2:
			matchResult.append(backup_pred_set.iloc[i, 1])
			d.append("Winner: " + backup_pred_set.iloc[i, 1])
		elif predictions[i] == 1:
			d.append("Draw")
			if(pred.predict_proba(pred_set)[i][2] > pred.predict_proba(pred_set)[i][0]):
				matchResult.append(backup_pred_set.iloc[i, 1])
			else:
				matchResult.append(backup_pred_set.iloc[i, 0])
		elif predictions[i] == 0:
			d.append("Winner: " + backup_pred_set.iloc[i, 0])
			matchResult.append(backup_pred_set.iloc[i, 0])
		d.append('%.3f'%(pred.predict_proba(pred_set)[i][2]))
		d.append('%.3f'%(pred.predict_proba(pred_set)[i][1]))
		d.append('%.3f'%(pred.predict_proba(pred_set)[i][0]))
		data.append(d)


	group = []
	f = pd.read_csv('datasets/fixtures.csv')

	c = 0
	for i in f.Group:
		group.append(str(i) +","+ str(c))
		c+=1
		
	group = sorted(group)
	GroupMatch = [matchResult,group]
		
	allD = []
	for i in range(48):
		d = []
		d.append(GroupMatch[0][int(GroupMatch[1][i].split(",")[1])])
		d.append(GroupMatch[1][i].split(",")[0])
		allD.append(d)
			
		
	def topTwo(x):
		from collections import Counter
		a = dict(Counter(x))
		a = sorted(a.items(), key = 
					lambda kv:(kv[1], kv[0]))

		return (a[len(a)-1],a[len(a)-2])
			
	GroupCompleted = []
	l = []
	for i in range(49):
		if(i%6==0 and i != 0):
			GroupCompleted.append(topTwo(l))
			l=[]
				
		if(i < 48):
			l.append(allD[i][0])
			
	A = (GroupCompleted[0][0][0],GroupCompleted[1][1][0])
	B = (GroupCompleted[0][1][0],GroupCompleted[1][0][0])

	C = (GroupCompleted[2][1][0],GroupCompleted[3][0][0])
	D = (GroupCompleted[2][0][0],GroupCompleted[3][1][0])

	E = (GroupCompleted[4][0][0],GroupCompleted[5][1][0])
	F = (GroupCompleted[4][1][0],GroupCompleted[5][0][0])

	G = (GroupCompleted[6][0][0],GroupCompleted[7][1][0])
	H = (GroupCompleted[6][1][0],GroupCompleted[7][0][0])

	# In[571]:


	#List of tuples before 
	#List of tuples before 
	group_16 = [A,B,C,D,E,F,G,H]


	# In[572]:

	matchResult = []
	def clean_and_predict(matches, ranking, final, pred):

		# Initialization of auxiliary list for data cleaning
		positions = []

		# Loop to retrieve each team's position according to FIFA ranking
		for match in matches:
			positions.append(ranking.loc[ranking['Team'] == match[0],'Position'].iloc[0])
			positions.append(ranking.loc[ranking['Team'] == match[1],'Position'].iloc[0])
		
		# Creating the DataFrame for prediction
		pred_set = []

		# Initializing iterators for while loop
		i = 0
		j = 0

		# 'i' will be the iterator for the 'positions' list, and 'j' for the list of matches (list of tuples)
		while i < len(positions):
			dict1 = {}

			# If position of first team is better, he will be the 'home' team, and vice-versa
			if positions[i] < positions[i + 1]:
				dict1.update({'home_team': matches[j][0], 'away_team': matches[j][1]})
			else:
				dict1.update({'home_team': matches[j][1], 'away_team': matches[j][0]})

			# Append updated dictionary to the list, that will later be converted into a DataFrame
			pred_set.append(dict1)
			i += 2
			j += 1

		# Convert list into DataFrame
		pred_set = pd.DataFrame(pred_set)
		backup_pred_set = pred_set
		df = pd.DataFrame()
		
		# Get dummy variables and drop winning_team column
		pred_set = pd.get_dummies(pred_set, prefix=['home_team', 'away_team'], columns=['home_team', 'away_team'])

		# Add missing columns compared to the model's training dataset
		missing_cols2 = set(final.columns) - set(pred_set.columns)
		for c in missing_cols2:
			pred_set[c] = 0
		pred_set = pred_set[final.columns]

		# Remove winning team column
		pred_set = pred_set.drop(['winning_team'], axis=1)

		# Predict!
		predictions = pred.predict(pred_set)
		for i in range(len(pred_set)):
			d = []
			d.append(backup_pred_set.iloc[i, 1]) 
			d.append(backup_pred_set.iloc[i, 0])
			if predictions[i] == 2:
				matchResult.append(backup_pred_set.iloc[i, 1])
				d.append("Winner: " + backup_pred_set.iloc[i, 1])
			elif predictions[i] == 1:
				d.append("Draw")
				if(pred.predict_proba(pred_set)[i][2] > pred.predict_proba(pred_set)[i][0]):
					matchResult.append(backup_pred_set.iloc[i, 1])
				else:
					matchResult.append(backup_pred_set.iloc[i, 0])
			elif predictions[i] == 0:
				matchResult.append(backup_pred_set.iloc[i, 0])
				d.append("Winner: " + backup_pred_set.iloc[i, 0])
			d.append('%.3f'%(pred.predict_proba(pred_set)[i][2]))
			d.append('%.3f'%(pred.predict_proba(pred_set)[i][1]))
			d.append('%.3f'%(pred.predict_proba(pred_set)[i][0]))
			data.append(d)


	# In[573]:


	clean_and_predict(group_16, ranking, final, pred)


	# In[574]:
	
	A = (matchResult[0],matchResult[2])
	B = (matchResult[1],matchResult[3])
	C = (matchResult[4],matchResult[6])
	D = (matchResult[5],matchResult[7])

	# List of matches
	quarters = [A,B,C,D]


	# In[575]:


	clean_and_predict(quarters, ranking, final, pred)


	# In[576]:
	
	A = (matchResult[len(matchResult)-1],matchResult[len(matchResult)-3])
	B = (matchResult[len(matchResult)-2],matchResult[len(matchResult)-4])

	# List of matches
	semi = [A,B]


	# In[577]:


	clean_and_predict(semi, ranking, final, pred)


	# In[578]:


	# Finals
	finals = [(matchResult[len(matchResult)-1],matchResult[len(matchResult)-2])]


	# In[579]:


	clean_and_predict(finals, ranking, final, pred)


	# In[ ]:





	# In[ ]:





	# In[ ]:

	return data


