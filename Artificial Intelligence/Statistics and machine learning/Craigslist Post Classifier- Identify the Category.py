from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB,GaussianNB
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.svm import LinearSVC
import numpy as np
import json
import re

def my_preprocessor(string):
    return re.sub('[-@~%^&*+#$/\.?!<>;:,\'\"\\(){}]', ' ', string).lower()

data = []
category = []
with open('training.json', 'r') as f:
    for line in f:
        if len(re.findall("\\d", line))>0:
            continue
        post = json.loads(line)
        data.append(post['heading'])
        category.append(post['category'])
test_data = []
# with open('sample-test.in.json', 'r') as f:
#     for line in f:
#         if len(re.findall("\\d", line))>0:
#             continue
#         post = json.loads(line)
#         test_data.append(post['heading'])
vectorizer = TfidfVectorizer(stop_words='english', min_df=0, max_df=.2, ngram_range=(1, 2), max_features=9000, preprocessor=my_preprocessor)
train = vectorizer.fit_transform(data)
clf = LinearSVC()
category = np.array(category)
clf.fit(train, category)
labels = ['activities', 'appliances', 'artists', 'automotive', 'cell-phones', 'childcare', 'general', 'household-services', 'housing', 'photography', 'real-estate', 'shared', 'temporary', 'therapeutic', 'video-games', 'wanted-housing']
n=int(input())
sections=[]
for i in range((n)):
    json.loads(input())
    test_data.append(post['heading'])
    sections.append(post['section'])
test_data=vectorizer.transform(test_data)
confidence = clf.decision_function(test_data)
output = []
for i in range(n):
    section = sections[i]
    if section == 'for-sale':
        vals = confidence[i, [1, 4, 9, 14]]
        m = max(vals)
        fields = np.array(['appliances', 'cell-phones', 'photography', 'video-games'])
        output.append(fields[vals==m][0])
    elif section == 'housing':
        vals = confidence[i, [8, 11, 12, 15]]
        m = max(vals)
        fields = np.array(['housing', 'shared', 'temporary', 'wanted-housing'])
        output.append(fields[vals==m][0])
    elif section == 'community':
        vals = confidence[i, [0, 2, 5, 6]]
        m = max(vals)
        fields = np.array(['activities', 'artists', 'childcare', 'general'])
        output.append(fields[vals==m][0])
    elif section == 'services':
        vals = confidence[i, [3, 7, 10, 13]]
        m = max(vals)
        fields = np.array(['automotive', 'household-services', 'real-estate', 'therapeutic'])
        output.append(fields[vals==m][0])
for i in output:
    print(i)