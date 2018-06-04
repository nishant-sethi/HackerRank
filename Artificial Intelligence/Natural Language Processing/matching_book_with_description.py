'''
Created on Jun 4, 2018

@author: nishant.sethi
'''
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np
n=int(input())
train_lines = [input() for i in range(n)]
input()
test_lines = [input() for i in range(n)] 
text_clf=Pipeline([('vect',CountVectorizer()),
                   ('tfidf',TfidfTransformer()),
                   ('clf',MultinomialNB())])
y=np.arange(n)
text_clf.fit(train_lines, y) 

result=text_clf.predict(test_lines)
for i in result:
    print(i+1)