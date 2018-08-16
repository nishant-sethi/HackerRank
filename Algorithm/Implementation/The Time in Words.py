#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    h=str(h)
    m=str(m)
    dct={
    '0' : '',
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine',
    '10' : 'ten',
    '11' : 'eleven',
    '12' : 'twelve',
    '13' : 'thirteen',
    '14' : 'fourteen',
    '15' : 'fifteen',
    '16' : 'sixteen',
    '17' : 'seventeen',
    '18' : 'eighteen',
    '19' : 'nineteen',
    '20' : 'twenty',
    '30' : 'thirty',
    '40' : 'forty',
    '50' : 'fifty',
    '60' : 'sixty',
    '70' : 'seventy',
    '80' : 'eighty',
    '90' : 'ninety'
}
    minute=int(m)
    if int(m)>30:
        x=60-int(m)
        if x>20:
            minute=dct[str(x-x%10)]+" "+dct[str(x%10)]
        else:
            minute=dct[str(x)]
        h=str(int(h)+1)
        hour=dct[h]
    else:
        if int(m)==30: 
            pass 
        elif int(m)>20:
            minute=dct[str(int(m)-int(m)%10)]+" "+dct[str(int(m)%10)]
        else:
            minute=dct[m]
        hour=dct[h]
    
    result='' 
    if int(m)==0:
        result=hour+' o\' clock'
    if int(m)>0 and int(m)<30:
        if int(m)==15:
            result='quarter past '+hour
        else:
            if minute=='one':
                result=minute+' minute past '+hour
            else:
                result=minute+' minutes past '+hour
    if int(m)==30:
        result='half past '+hour
    if int(m)>30:
        print(int(m))
        if int(m)==45:
            result='quarter to '+hour
        else:
            if minute=='one':
                result=minute+' minute to '+hour
            else:
                result=minute+' minutes to '+hour
         

    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
