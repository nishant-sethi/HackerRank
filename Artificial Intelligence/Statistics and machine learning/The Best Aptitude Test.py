import numpy as np
import math

def corr(x, y):
    SS = lambda x,y:(sum([i*j for (i,j) in zip(x,y)])-(sum(x)*sum(y))/len(x))
    try:
    	#computing correlation as per the formula mentioned above
        correlation = SS(x, y)/math.sqrt(abs(SS(x,x)*SS(y,y)))
    except:
        correlation = 0
    return correlation

def main():                                                                                                          
    test_cases = input()
    for e in range(0,test_cases):
        numStudents = input()
        gpa = [float(i) for i in raw_input().strip().split()]      
        corrlist = []
        for i in range(0,5):
            marks = [float(i) for i in raw_input().strip().split()]
            corrlist.append(corr(gpa, marks))      
        print np.argmax(corrlist) + 1     