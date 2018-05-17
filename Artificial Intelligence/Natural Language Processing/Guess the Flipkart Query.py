from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer,TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC
import re
import numpy as np

x_train=[]
y_train=[]

def words(text):
    return re.findall(r'(?:[a-zA-Z]+[a-zA-Z\'\-]?[a-zA-Z]|[a-zA-Z]+)',text)

count=0
with open('training.txt', 'r') as f:
    for line in f:
        count+=1
        if count==1:
            continue
        x=[a for a in line.rstrip().split("\t")]
        sen=" ".join(word for word in words(x[0]))
        x_train.append(sen)
        y_train.append(x[1])

x=np.array(x_train)
y=np.array(y_train)
text_clf=Pipeline([('vect',CountVectorizer()),
                   ('tfidf',TfidfTransformer()),
                   ('clf', LinearSVC())])
text_clf.fit(x,y)

test=[]
for i in range(int(input())): 
    x=input()
    sen=" ".join(word for word in words(x))
    test.append(x)
predicted=text_clf.predict(np.array(test))
for i in predicted:
    print(i)