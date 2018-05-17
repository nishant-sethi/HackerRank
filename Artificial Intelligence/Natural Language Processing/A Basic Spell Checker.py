import re
from collections import Counter
from string import ascii_lowercase


def words(text):
    return re.findall(r'(?:[a-z]+[a-z\'\-]?[a-z]|[a-z]+)', text.lower())

def create_vocabulary():
    v = Counter(words(open('corpus.txt').read()))
    return v

def sub_candidates(word):
    lst=[]
    for i in ascii_lowercase:
        for j in range(len(word)):
            lst.append(word[:j]+i+word[j+1:])
    return lst

def add_candidates(word):
    lst=[]
    for i in ascii_lowercase:
        for j in range(len(word)+1):
            lst.append(word[:j]+i+word[j:])
    return lst

def swap_candidates(word):
    lst=[]
    for i in range(1,len(word)):
        lst.append(word[:i-1]+word[i]+word[i-1]+word[i+1:]) 
    return lst

def del_candidates(word):
    lst=[]
    for i in range(len(word)):
        lst.append(word[:i]+word[i+1:])
    return lst

def candidate_words(word):
    return add_candidates(word)+sub_candidates(word)+del_candidates(word)+swap_candidates(word)

def valueOf(word):
    return Vocabulary[word]

def spelled_word(word):
    suggestions=set(candidate_words(word)).intersection(set(Vocabulary))
    if len(suggestions)>0:
        maxScoreWord = max(suggestions, key=valueOf)
        return sorted([w for w in suggestions if Vocabulary[w] == Vocabulary[maxScoreWord]])[0]
    return (word)

Vocabulary=create_vocabulary()
for i in range(int(input())):
    word=input().strip().lower()
    if word in Vocabulary:
        output=word
    else:
        output=spelled_word(word)
    print(output)