import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB,GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import HashingVectorizer
import numpy as np


if sys.version_info[0]>=3: raw_input=input
transformer=HashingVectorizer(stop_words='english')

_train=[]
train_label=[]
f=open('trainingdata.txt')
for i in range(int(f.readline())):
    s=f.readline().rstrip()
    idx=s.find(' ')
    _train.append(s[idx+1:])
    train_label.append(int(s[:idx]))
f.close()
# train = transformer.fit_transform(_train)
# svm=LinearSVC()
# svm.fit(train,train_label)
text_clf=Pipeline([('vect',CountVectorizer()),
                   ('tfidf',TfidfTransformer()),
                   ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                           alpha=1e-3, random_state=42,
                                           max_iter=5, tol=None))])
text_clf.fit(_train,train_label)
test_data=[]
for i in range(int(input())):
    test_data.append(input())
    for j in text_clf.predict(test_data):
        print(j)
    test_data=[]
'''Strings in python cannot be modified once created, so essentially  creates a new string instance with the 
stripped content. The  removes characters from the right based on the argument specifying the set of characters 
to be removed.''