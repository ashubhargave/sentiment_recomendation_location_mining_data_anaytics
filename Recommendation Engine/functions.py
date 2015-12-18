import re
import random
import numpy as np
import matplotlib.cm as cm
#import statsmodels.api as sm
#from collections import Counter
#from collections import defaultdict
from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt
#from math import sqrt
import time
import json
def find_similar(preferences,p1,p2):
    #print(preferences)
    #print("*****************************")
    #print(p1)
    #print("*****************************")
    #print(p2)
    a = [(i, preferences[p1][i], preferences[p2][i]) for i in preferences[p1] if i in preferences[p2]]
    if a and len(a) > 1:
        b = np.array(a)[:,1:].astype(float)
        return pearsonr(b[:,0], b[:,1])[0]
    else:
        return 0


def calculateSimilarItems(preferences,n=5):
    result={}
    c=0
    for item in preferences:
        c+=1
        if c%2000==0: print("%d / %d" % (c,len(preferences)))
        scores=topMatches(preferences,item,n=n,similarity=find_similar)
        result[item]=scores
    return result
    
def topMatches(preferences,p1,n=5, similarity=find_similar):
    scores=[(similarity(preferences,p1,other),other)
                   for other in preferences if other!=p1]
    scores.sort()
    scores.reverse( )
    return scores[0:n]
    
    
