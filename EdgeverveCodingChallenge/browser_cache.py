'''
Created on Jun 1, 2018

@author: nishant.sethi
'''
from collections import deque

def process_text(l,text):
    lst=deque()
    result=''
    for i in text:
        if len(lst)==l:
            if i!='!':
                lst.popleft()
                lst.append(i)
            else:
                a=''
                for i in lst:
                    if i not in list(a):
                        a+=i
                result+=a
                result+=' '      
                
        else:
            if i!='!':
                lst.append(i)
            else:
                a=''
                for i in lst:
                    if i not in list(a):
                        a+=i
                result+=a
                result+=' ' 
    return result[0:len(result)]
inp=input().split()
l=int(inp[0])
'''ABC CDEAF DEAFB'''
text=inp[1]
print(process_text(5,text)) 