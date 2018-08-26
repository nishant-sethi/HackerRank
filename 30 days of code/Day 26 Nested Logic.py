da,ma,ya=map(int,input().split())
de,me,ye=map(int,input().split())
fine=0
if ya>ye:
    fine=10000
else:
    if ma>me:
        if ma==12 and ya<ye:
            pass
        else:
            fine=500*(ma-me)
    else:
        if da>de and ma==me:
            fine=15*(da-de)
        else:
            fine=0
print(fine)