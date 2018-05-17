import random
# assume sum of bias is 1
def roll(massDist):
    randRoll = random.random() # in [0,1)
    sum = 0
    result = 1
    for mass in massDist:
        sum += mass
        if randRoll < sum:
            return result
        result+=1
T=int(input())
for x in range(0,T):
    sampleMassDist = [float(a) for a in input().split(",")]
    no_of_ladders,no_of_snakes=map(int,input().split(","))
    ladders=[a.split(",") for (a) in input().split()]
    ladder_start=[]
    ladder_end=[]
    for i in ladders:
        ladder_start.append(int(i[0]))
        ladder_end.append(int(i[1]))
    snakes=[a.split(",") for (a) in input().split()]
    snake_start=[]
    snake_end=[]
    for i in snakes:
        snake_start.append(int(i[0]))
        snake_end.append(int(i[1])) 
    moves_result=[]
    total=0
    for j in range(5000):
        moves=0
        start=1
        win=True
        while win:
            dice_result=roll(sampleMassDist)
            if not(start+dice_result>100):
                start+=dice_result
            moves+=1
            if start in ladder_start:
                start=ladder_end[ladder_start.index(start)]
            if start in snake_start:
                start=snake_end[snake_start.index(start)]
            if start==100:
                win=False
                total+=1
            if moves==1000:
                break
        moves_result.append(moves)
    print(round(sum(moves_result)/total))