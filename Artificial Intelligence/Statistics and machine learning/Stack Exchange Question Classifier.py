import json
import re
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer,TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
count=0
topic=[]
question=[]
excerpt=[]
def words(text):
    return re.findall(r'(?:[a-zA-Z]+[a-zA-Z\'\-]?[a-zA-Z]|[a-zA-Z]+)',text)

with open('training.json', 'r') as f:
    for line in f:
        count+=1
        if count==1:
            continue
        post = json.loads(line)
        topic.append(post["topic"])
        abc=post["question"]+"\r\n"+post["excerpt"]
        sen="".join(word for word in words(abc))
        excerpt.append(abc)


x_train=np.array(excerpt)

y_train=topic

txt_clf=Pipeline([('vect',CountVectorizer()),
                  ('tfidf',TfidfTransformer()),
                  ('clf',LinearSVC())])
txt_clf.fit(x_train, y_train)
_test=[]
for i in range(int(input())):
	h=json.loads(input())
	_test.append(h['question']+"\r\n"+h['excerpt'])
predicted=txt_clf.predict(_test)
for i in predicted:
    print(i)
