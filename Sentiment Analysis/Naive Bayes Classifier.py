import nltk
import csv
from datetime import date
#import matplotlib.pyplot as plt
from nltk import *
from nltk.corpus import stopwords
#import sklearn
import codecs
documents = []
genuine_reviews = []
reviews = []
#List of words related to "restaurant" to find out reviews from the csv file only about the restaurants category and no others.
restaurant_words = ["restaurant", "food" , "hotel","breakfast" , "lunch","dinner", "brunch" ,"appetizers"]
 
with open("Courses/BigData/Project/yelp_training_set/yelp_training_set/yelp_training_set_review.csv","rt") as csvfile:
    csvreader = csv.reader(csvfile)
    for index,row in enumerate(csvreader):
        if(index<12000):
            #The below code is commented. If the reviews need to be checked only on restaurants then this needs to be uncommented 
			#for s in restaurant_words:
            #if(s in row[2].lower()):
            documents.append((row[0],row[4]))

print(len(documents))
exc = ["!","@","(",")",".",",","\\\\","\\'","\\n"]
all_words = nltk.FreqDist(w.lower() for w in list(set(word_tokenize(str(documents)))) if w.lower() not in exc)
print("The length of all words is "+" "+str(len(all_words)))
wfeatures = list(all_words)[:1000]
print(wfeatures[:20])

stopwords = nltk.corpus.stopwords.words('english')
#print(stopwords)
exc = ["!","@","(",")","4g","internet", "4g internet"]
all_bigrams = nltk.FreqDist(" ".join(w).lower() for w in list(nltk.bigrams((word_tokenize(str(documents))))))# if " ".join(w).lower() not in stopwords or " ".join(w).lower() not in exc )
#print(list(all_bigrams)[:10])
# [(i,j) in all_bigrams]
bigram_feature_words = list(all_bigrams)[:500]

def document_feature(document):
    document_words = set(document)
    features = {}
    for word in wfeatures:
        features['contains(%s)' % word] = (word in document_words)
    return features

def bigram_feature(document):
    bigram_words = []
    #for item in nltk.bigrams(str.split(document)):
    #       bigram_words.append(" ".join(item))
   # bigram_words = set(bigram_words)#
    for item in nltk.bigrams((word_tokenize(str(document)))):
           bigram_words.append(" ".join(item))
    bigram_words = set(bigram_words)
    bigram_features = {}
    for word in bigram_feature_words:
        bigram_features['contains(%s)' % word] = (word in bigram_words)
    return bigram_features

featuresets = []
q = []
#len(documents)
for i in range(len(documents)):
    #print(list(nltk.bigrams(str.split(documents[i][0])))[0:3])
    #print(type(str.split(documents[i][0])))
    a = document_feature(str.split(documents[i][0]))
    #b = bigram_feature(str.split(documents[i][0]))
    #b.update(a)
#     q.append(b)
    featuresets.append((a,documents[i][1]))

#a.append(b)
print(len(a))
print("Length of featurewsets")
print(len(featuresets))
#featuresets.append((b,documents[i][1]))
train_set, test_set = featuresets[:2000], featuresets[2051:2500]
#filter = ['camera' , 'flash', 'image', 'picture', 'megapixel', 'pixel','size']
#print(test_set)
#if any(word in row[1] for word in filter):
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set))

classifier.show_most_informative_features(20)
split_words = str.split("Worst Restaurant in Arizona State")
print(split_words)
x = document_feature(split_words)
#print(x)
print(classifier.classify(x))
