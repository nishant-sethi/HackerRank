from collections import defaultdict

stw = ['i',
 'me',
 'my',
 'myself',
 'we',
 'our',
 'ours',
 'ourselves',
 'you',
 'your',
 'yours',
 'yourself',
 'yourselves',
 'he',
 'him',
 'his',
 'himself',
 'she',
 'her',
 'hers',
 'herself',
 'it',
 'its',
 'itself',
 'they',
 'them',
 'their',
 'theirs',
 'themselves',
 'what',
 'which',
 'who',
 'whom',
 'this',
 'that',
 'these',
 'those',
 'am',
 'is',
 'are',
 'was',
 'were',
 'be',
 'been',
 'being',
 'have',
 'has',
 'had',
 'having',
 'do',
 'does',
 'did',
 'doing',
 'a',
 'an',
 'the',
 'and',
 'but',
 'if',
 'or',
 'because',
 'as',
 'until',
 'while',
 'of',
 'at',
 'by',
 'for',
 'with',
 'about',
 'against',
 'between',
 'into',
 'through',
 'during',
 'before',
 'after',
 'above',
 'below',
 'to',
 'from',
 'up',
 'down',
 'in',
 'out',
 'on',
 'off',
 'over',
 'under',
 'again',
 'further',
 'then',
 'once',
 'here',
 'there',
 'when',
 'where',
 'why',
 'how',
 'all',
 'any',
 'both',
 'each',
 'few',
 'more',
 'most',
 'other',
 'some',
 'such',
 'no',
 'nor',
 'not',
 'only',
 'own',
 'same',
 'so',
 'than',
 'too',
 'very',
 's',
 't',
 'can',
 'will',
 'just',
 'don',
 'should',
 'now']

def train(sentences):
    global stw
    features = []
    for sentence in sentences:
        tokens = sentence.lower().split()
        tokens = [word.strip('''!@#$%^&*()[]{};:"'/<>\\''') for word in tokens if word not in stw]
        feat = defaultdict(lambda : 0)
        for token in tokens:
            feat[token] += 1
        features.append(feat)
    return features

def classify(features, sentences):
    global stw
    sc = []
    for feat in features:
        tsc = []
        for sentence in sentences:
            tokens = sentence.lower().split()
            tokens = [word.strip('''!@#$%^&*()[]{};:"'/<>\\''') for word in tokens if word not in stw]
            
            t = 0
            for token in tokens:
                t += feat[token]
            tsc.append(t)
        sc.append(tsc)
    for score in sc:
        i = score.index(max(score))
        print i+1


if __name__ == '__main__':
    a = []
    b = []
    n = int(raw_input())
    for i in range(n):
        a.append(raw_input())
    raw_input()
    for i in range(n):
        b.append(raw_input())
    features = train(a)
    classify(features, b)