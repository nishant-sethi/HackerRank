'''
Created on May 25, 2018

@author: nishant.sethi
'''
n=5
p=1/3
result=0
for i in range(1,6):
    result+=(1-p)**(i-1)*p 
print(round(result,3))