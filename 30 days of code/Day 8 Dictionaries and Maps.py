dct={}
n=int(input())
for i in range(n):
    name,phn=input().split()
    dct.update({name:phn})
for i in range(n):
    x=input()
    if x in dct.keys():
        print(x+"="+dct[x])
    else:
        print("Not found")