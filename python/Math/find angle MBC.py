import math
a=int(input())
b=int(input())
c=(a**2+b**2)**0.5
result=round(math.degrees(math.asin(a/c)))
print(str(int(result))+'°')