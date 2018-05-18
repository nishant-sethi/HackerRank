import sys

from fractions import gcd
def lcm(a,b):
    return (a*b)/gcd(a, b)

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))
count=0
lcm=reduce(lcm, a)
gcd=reduce(gcd, b)
lcm_copy = lcm
while(lcm<=gcd):
    if gcd%lcm==0:
        count=count+1
    lcm=lcm+lcm_copy
print(count)
