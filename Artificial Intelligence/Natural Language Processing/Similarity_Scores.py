'''
Created on Jun 4, 2018

@author: nishant.sethi
'''

import math

d = list()
d.append('An apple a day keeps the doctor away'.lower().split(' '))
d.append('Never compare an apple to an orange'.lower().split(' '))
d.append('I prefer scikit-learn to orange'.lower().split(' '))
compDoc = "I'd like an apple".split(' ')

terms = set()
tf = list()
temp = dict()
for doc in d:
    for item in doc:
        temp[item] = doc.count(item)/len(doc)
        terms.add(item)
    tf.append(temp)
    temp = dict()

idf = dict()
temp = dict()
for term in terms:
    temp[term] = 0
    for doc in d:
        if term in doc:
            temp[term]+=1
    idf[term] = 1+math.log(3/temp[term])
#print("idf:\n",idf)
    
tfidf = [0, 0, 0]
for term in compDoc:
    for i in range(len(d)):
        if term in d[i]:
            tfidf[i]+= tf[i][term]*idf[term]
print(tfidf.index(max(tfidf))+2)