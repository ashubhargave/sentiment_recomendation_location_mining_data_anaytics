import nltk
import csv
from datetime import date
import sklearn
import random
from sklearn import svm
documents = []
reviews = []

# Generating Trainset from Yelp        
xtrain = []
ytrain = []
with open('C:\Users\AshutoshBhargave\Desktop\Courses\BigData\Project\yelp_training_set\yelp_training_set_review_sentiment.csv','rb') as csvfile:
    csvreader = csv.reader(csvfile)
    for index,row in enumerate(csvreader):
        if index<=20000:
            xtrain.append(row[0])
            ytrain.append(row[4])
            
# Created a list of 2000 most frequent words in reviews
wfeatures = list(nltk.FreqDist(w.lower() for w in list(set(nltk.word_tokenize(str(xtrain))))))[:2000]
print(len(wfeatures))
# Twitter Tweets for prediction
'''with open('D:\Downloads\\b.tsv','rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter='\t')
    for row in csvreader:
        documents.append(row[2])
'''

# Document_feature function returns a featureset list of
# a 0 or 1 value on the list of words of the review based on if it exists in the frequent words,
def document_feature(document):
    document_words = []
    document_words = set(document)
    features = []
    for word in wfeatures:
        if(word in document_words):
            features.extend('1')
        else:
            features.extend('0')
    return features

# Applying document_feature on reviews and creating our training set	
xt = []
for i in range(len(xtrain)):
    xt.append(document_feature(str.split(xtrain[i])))
    
# Initializing our svm classifier with a linear kernel and C='1'
clf = sklearn.svm.SVC(kernel='linear', C=1)

# Performing cross validation using svm classifier
score = sklearn.cross_validation.cross_val_score(clf, xt, ytrain, cv=5)
score.mean()
print(score)

# Creating classification report using SVM
predicted = sklearn.cross_validation.cross_val_predict(clf, xt, ytrain, cv=5)
sklearn.metrics.classification_report(ytrain, predicted)

# Fitting SVM on xt and ytrain
clf.fit(xt,ytrain)

# A manual way to test 
'''
check = []
check = ["camera is bad", "excellent", "camera is poor", "not waste", "awesome", "camera is great"]
tr =[]
for i in range(len(check)):
    tr.append(document_feature(str.split(check[i])))

a = clf.predict(tr)
print(a)
'''

'''m = []
for x in documents :
    if("camera" in x.lower() or "picture" in x.lower() or "image" in x.lower() or "pixel" in x.lower() or "focus" in x.lower()):
        m.append(x)
print(m[3])
xt1 = []
for i in range(len(m)):
    xt1.append(document_feature(str.split(m[i])))
a = clf.predict(xt1)   

le = len(a)
sum = 0
for i in range(le):
    sum = sum + int(a[i])

print(sum)
print(le)
print(le-sum)


# Calculated our prediction of positive and negative public opinions
# containing words related to storage
m = []
for x in documents :
    if("storage" in x.lower() or "size" in x.lower() or "capacity" in x.lower() or "gigabytes" in x.lower() or "bytes" in x.lower()):
        m.append(x)
print(len(m))
xt1 = []
for i in range(len(m)):
    xt1.append(document_feature(str.split(m[i])))
    
a = clf.predict(xt1)   
le = len(a)
sum = 0
for i in range(le):
    sum = sum + int(a[i])
print(sum)
print(le)
print(le-sum)    

'''

