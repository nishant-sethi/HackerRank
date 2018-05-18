import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))
no_of_apples=0
no_of_oranges=0
for i in apple:
    if i+a>=s and i+a<=t:
        no_of_apples=no_of_apples+1
        
for i in orange:
    if i+b>=s and i+b<=t:
        no_of_oranges=no_of_oranges+1

print(no_of_apples)
print(no_of_oranges)
