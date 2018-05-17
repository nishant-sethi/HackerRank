import operator
x=[]
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    x.append([name,score])
x.sort(key=operator.itemgetter(1,0))
a=[i for i in x if i[1]==x[1][1]]
a.sort(key=operator.itemgetter(0))
for i in a:
    print i[0]