import fileinput
import string
import re
### Stop words list
stop=[u'i', u'me', u'my', u'myself', u'we', u'our', u'ours', u'ourselves', u'you', u'your', u'yours', u'yourself', u'yourselves', u'he', u'him', u'his', u'himself', u'she', u'her', u'hers', u'herself', u'it', u'its', u'itself', u'they', u'them', u'their', u'theirs', u'themselves', u'what', u'which', u'who', u'whom', u'this', u'that', u'these', u'those', u'am', u'is', u'are', u'was', u'were', u'be', u'been', u'being', u'have', u'has', u'had', u'having', u'do', u'does', u'did', u'doing', u'a', u'an', u'the', u'and', u'but', u'if', u'or', u'because', u'as', u'until', u'while', u'of', u'at', u'by', u'for', u'with', u'about', u'against', u'between', u'into', u'through', u'during', u'before', u'after', u'above', u'below', u'to', u'from', u'up', u'down', u'in', u'out', u'on', u'off', u'over', u'under', u'again', u'further', u'then', u'once', u'here', u'there', u'when', u'where', u'why', u'how', u'all', u'any', u'both', u'each', u'few', u'more', u'most', u'other', u'some', u'such', u'no', u'nor', u'not', u'only', u'own', u'same', u'so', u'than', u'too', u'very', u's', u't', u'can', u'will', u'just', u'don', u'should', u'now']

questions_word=['which','what','who','how']
stop.extend(questions_word)

#### Find the ratio of count of commen words between sentence1 and sentence2 to count of words in sentence2 
def similarity(sentence1,sentence2):
    sentence1_set = set(sentence1.split(" "))
    sentence2_set = set(sentence2.split(" "))
    score = float(len(sentence1_set.intersection(sentence2_set)))/len(sentence2_set)
    return score

##### Extract sentences, questions, answers
i=-1
questions=[]
for line in fileinput.input():
    if i==-1:
        sentences =[x.replace("\n","").lower() for x in line.split(".")]
        i=i+1
    else:
        questions.append(line.replace("\n","").lower())
answer_set_orginal = questions[-1]
questions.remove(answer_set_orginal)
answer_set = answer_set_orginal.split(";")

#####process the question, answers by removing stop words and punctuations
processed_questions=[]
processed_answers=[]
for each_question in questions:
    processed_string = " ".join([x.lower() for x in each_question.split(" ") if x.lower() not in stop])
    processed_questions.append(re.sub("[^a-zA-Z]"," ",processed_string))

for each_answer in answer_set:
    processed_answer = " ".join([x.lower() for x in each_answer.split(" ") if x.lower() not in stop])
    processed_answers.append(re.sub("[^a-zA-Z]"," ",processed_answer))

##### Find the matching pair of questions with high similarity    
exact_match={}
for i in range(len(processed_questions)):
    max_sim=0;
    for j in range(len(processed_answers)):
        for each_sentence in sentences:
            # similarity is calculated by product of similarity(sentence,question) and similarity(sentence,answer)
            sim = similarity(each_sentence,processed_questions[i])*similarity(each_sentence,processed_answers[j])
            if sim > max_sim:
                max_sim=sim
                exact_match[i]=j
    
    
##### print the exact match    
for i in range(len(questions)):
    print(answer_set[exact_match[i]])