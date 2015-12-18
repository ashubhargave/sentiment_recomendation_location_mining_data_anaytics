import nltk
import csv
from datetime import date
#import matplotlib.pyplot as plt
from nltk import *
from nltk.corpus import stopwords
from nltk.corpus import wordnet
#import sklearn
import codecs
documents = []
genuine_reviews = []
reviews = []
#List of words related to "restaurant" to find out reviews from the csv file only about the restaurants category and no others.
restaurant_words = ["restaurant", "food" , "hotel","breakfast" , "lunch","dinner", "brunch" ,"appetizers"]
     
#List of words related to "dirty" keyword
dirty_words = ['dirty', 'soiled', 'grimy', 'grubby', 'filthy', 'mucky', 'stained', 'unwashed','greasy','smeared', 'smeary', 'spotted', 'smudged', 'cloudy', 'muddy', 'dusty', 'sooty']

#Used wordnet library in NLTK to find the synonyms of "dirty" keyword and append it to the list of dirty keyword.
for syn in wordnet.synsets("dirty"):
    for l in syn.lemmas():
        dirty_words.append(l.name())

print(dirty_words)
dirty_words = list(set(dirty_words))
#open the reviews file where yelp reviews are stored.
#Sequence of infor retrieved :('user_id', 'review_id', 'text', 'votes.cool', 'business_id', 'votes.funny','stars', 'date', 'type') 
#yelp_training_set/yelp_training_set/yelp_training_set_review.csv
with codecs.open("Desktop/Courses/BigData/Project/yelp_dataset_challenge_academic_dataset_1/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.csv", 'r',encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for index,row in enumerate(csvreader):
            if(index==10000):
                print("One lakh done")
            #Find only those reviews related to the keyword "Restaurant" category.
            for s in restaurant_words:
                #Consider only those reviews whose rating is less than 3. 
                if(s in row[2].lower() and int(row[6])<=3):
                    #Append the "review" and "business_id" of the particular review in list named documents.
                    documents.append((row[2].encode('utf-8'),row[4].encode('utf-8')))
                    break
#Control Panel\All Control Panel Items\Power Options\Edit Plan Settings
#Function to check the words in the review are related to "dirty" and include only those in further experiment.
def check_dirt_words(document):
    for m in dirty_words:
        if m in document:
            return document
    else:
        return 0
fp=open("Desktop\Courses\Bigdata\Project\\reviews.tsv",'a' ) 
headers = ['business_id' ,'bad_reviews_size' ,'city' ,'name','longitude' ,'latitude','state' ]
for a in headers:
        fp.write(a)
        fp.write('\t')
fp.write('\n')
new_documents = []
restaurant_reviews = {}
#Iterate over all the reviews in document and insert those to the the new list new_documents
for i in range(len(documents)):
    a = check_dirt_words(documents[i][0])
    if(a is not 0):
        new_documents.append((a,documents[i][1]))
        if restaurant_reviews.has_key(documents[i][1]):
            restaurant_reviews[documents[i][1]]= int(restaurant_reviews[documents[i][1]])+1
        else:
            restaurant_reviews[documents[i][1]]= 1

#print((restaurant_reviews))
fp=open("Desktop\Courses\Bigdata\Project\\reviews.tsv",'a' ) 
headers = ['business_id' ,'bad_reviews_size' ,'city' ,'name','longitude' ,'latitude','state' ]
for a in headers:
        fp.write(a)
        fp.write('\t')
fp.write('\n')
print(len(restaurant_reviews))
print("Started working on biz file")
for key, value in restaurant_reviews.iteritems():    
    with codecs.open("C:/Users/AshutoshBhargave/Desktop/Courses/BigData/Project/yelp_dataset_challenge_academic_dataset_1/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.csv", 'r',encoding='utf-8') as csvfile:
        business_file_reader = csv.reader(csvfile)
        for index,row in enumerate(business_file_reader): 
            if(str(key)==str(row[16])):
                h = [str(row[16]),int(value),str(row[61]),str(row[22]),str(row[74]),str(row[10]),str(row[39])]
                for a in h:
                    if(a is not None):
                        #print(a)
                        fp.write(str(a))
                    fp.write('\t')
                fp.write('\n')
                #break        
fp.close()

#for key, value in restaurant_reviews.iteritems():
    
'''print(len(new_documents))
exc = ["!","@","(",")",".",",","\\\\","\\'","\\n"]
all_words = nltk.FreqDist(w.lower() for w in list(set(word_tokenize(str(new_documents)))) if w.lower() not in exc)
print("The length of all words is "+" "+str(len(all_words)))
wfeatures = list(all_words)[:1000]
print(wfeatures[:20])'''