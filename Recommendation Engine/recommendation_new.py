import re
import random
import numpy as np
from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt
#from math import sqrt
import time
import json
import functions as fnx
import open_json_files as ojf
# main dataset
user_data_dictionary={}
business_data_dictionary={}
with open('Desktop/Courses/BigData/Project/yelp_training_set/yelp_training_set/yelp_training_set_review.json') as f:
    for line in f:
        line = json.loads(line)
        user = str(line['user_id'])
        business = str(line['business_id'])
        rate = line['stars']
        if business not in business_data_dictionary:
            business_data_dictionary[business]={}
        else:
            business_data_dictionary[business][user]=rate
        if user not in user_data_dictionary:
            user_data_dictionary[user]={}
        else:
            user_data_dictionary[user][business]=rate

#prepare item similarity matrix, this may take a while
itemsim=fnx.calculateSimilarItems(business_data_dictionary)

#hot businesses to be recommended when there is no record
topshops={}
for i in business_data_dictionary:
    rates=business_data_dictionary[i].values()
    mean=np.mean(rates)
    if mean ==5:
        topshops[i]=len(rates)
topshops = [(score,item) for item,score in topshops.items()]
topshops.sort()
topshops.reverse()
topshops = [(5.0,j) for i,j in topshops[:5]]

#match user and business information
B = ojf.OpenBizFile()
U = ojf.OpenUserFile()


def Recommendation(preferences,itemMatch,user):
    userRatings=preferences[user]
    scores={}
    totalSim={}
    # Loop over items rated by this user
    for (item,rating) in userRatings.items():
             # Loop over items similar to this one
             for (similarity,item2) in itemMatch[item]:
                    # Ignore if this user has already rated this item
                    if item2 in userRatings: continue
                    # Weighted sum of rating times similarity
                    scores.setdefault(item2,0)
                    scores[item2]+=similarity*rating
                    # Sum of all the similarities
                    totalSim.setdefault(item2,0)
                    totalSim[item2]+=similarity
    # Divide each total score by total weighting to get an average 
    rankings=[(score/totalSim[item],item) for item,score in scores.items() if score>0]
    # Return the rankings from highest to lowest 
    rankings.sort( )
    rankings.reverse( )
    if rankings:
        return  [(i,B[j],j) for i,j in rankings[:5]]
    else:
        return  [(i,B[j],j) for i,j in topshops]

#demo
x = (random.sample(user_data_dictionary.keys(),1)[0])
q = Recommendation(user_data_dictionary,itemsim,x)#random.sample(user_data_dictionary.keys(),1)[0]) 
print("The recommendation for user id %s is as follows",str(x))
for z in q:
    print(z)
