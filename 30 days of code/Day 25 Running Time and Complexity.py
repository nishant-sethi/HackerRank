import math 
def check_prime(num):
    if num==1:
        return "Not prime"
    elif num==2:
        return "Prime"
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                return "Not prime"
        return "Prime"
t=int(input())
for i in range(t):
    n=int(input())
    print(check_prime(n))
              