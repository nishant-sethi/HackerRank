'''
Created on Jun 1, 2018

@author: nishant.sethi
'''
import math
def rowColEntry(n,r):
    return math.factorial(n)/(math.factorial(r)*(math.factorial(n-r)))
n,l=(11,3)
lst=[]
x=1
a=n
while x!=l-1:
    lst.append(rowColEntry(a,x))
    a+=1
    x+=1
print(lst)
ans=[1]
a=1
for i in lst:
    print(a+int(i))
    ans.append(a+int(i))
    a=a+int(i)
result=''
for i in ans:
    result+=str(i)+'+'
print(result[:-1])