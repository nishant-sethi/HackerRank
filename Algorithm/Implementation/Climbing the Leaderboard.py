#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    score=list(set(scores))
    score=sorted(score,reverse=True)
    min_score=score[0]
    max_score=score[len(score)-1]
    results=[] 
    index=len(score)-1
    print(score)
    for i in range(len(alice)):        
        while(1):
            print(index)
            if score[index]>=alice[i] or index<0:
                if score[index]==alice[i]:
                    results.append(index+1)
                else:
                    results.append(index+2)
                break
            else:
                index-=1
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
