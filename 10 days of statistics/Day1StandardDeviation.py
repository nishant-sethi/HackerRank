'''
Created on May 22, 2018

@author: nishant.sethi
'''
n=int(input())
num=[int(x) for x in input().split()]
mean=sum(num)/n
var=0
for i in num:
    var+=(i-mean)**2
var=var/n
std=round(var**0.5,1)
print(std)