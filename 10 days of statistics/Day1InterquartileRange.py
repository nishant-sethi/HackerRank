'''
Created on May 22, 2018

@author: nishant.sethi
'''
n=int(input())
num=[int(x) for x in input().split()]
freq=[int(x) for x in input().split()]
data=[]
for i in range(len(num)):
    for j in range(freq[i]):
        data.append(num[i])
data.sort()    
total=sum(freq)
mid=total//2
s1=[]
s2=[]
if total%2!=0:
    s1=data[0:mid]
    s2=data[mid+1:]
else:
    s1=data[0:mid]
    s2=data[mid:]
if len(s1)%2==0:
    mid=(len(s1)//2)-1
    result=s1[mid]+s1[mid+1]
    x=round(result/2,1)
else:
    x=round(float(s1[len(s1)//2]),1)

if len(s2)%2==0:
    mid=(len(s2)//2)-1
    result=s2[mid]+s2[mid+1]
    y=round(result/2,1)
else:
    y=round(float(s2[len(s2)//2]),1)

print(y-x)