'''
Created on May 21, 2018

@author: nishant.sethi
'''

import nltk
nltk.downloader()
try:
    from nltk import wordpunct_tokenize
    from nltk.corpus import stopwords
except ImportError:
    print ('[!] You need to install nltk (http://nltk.org/index.html)')
    
print(stopwords)

def _calculate_languages_ratios(text):
    languages_ratios={}
    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]
    # Compute per language included in nltk number of unique stopwords appearing in analyzed text
    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)
        if language.lower() in ["english","french","german","spanish"]:
            languages_ratios[language] = len(common_elements) # language "score"
    return languages_ratios

def detect_language(text):
    ratios = _calculate_languages_ratios(text)
    most_rated_language = max(ratios, key=ratios.get)
    return most_rated_language

text=input()
print(detect_language(text).capitalize())