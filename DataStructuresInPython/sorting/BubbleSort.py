'''
Created on Jun 4, 2018

@author: nishant.sethi
'''

def bubblesort(lst):
# Swap the elements to arrange in order
    for iter_num in range(len(lst)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp