#!/usr/bin/py
import numpy as np
import math
def printTransactions(m, k, d, name, owned, prices):
    slope_list=[]
    for i in range(k):
        x=np.array([1.0,2.0,3.0,4.0,5.0])
        y= np.array(prices[i])
        A = np.vstack([x, np.ones(len(x))]).T
        slope, constat = np.linalg.lstsq(A, y)[0]
        slope_list.append(slope)
        
    sort_slope = sorted(slope_list)
    amount_remaining= m
    trans={}
    for j in reversed(range(k)):
        index_slope = slope_list.index(sort_slope[j])
        if sort_slope[j]<=0 and amount_remaining>=prices[index_slope][-1]:
            #print prices[index_slope][-1]
            num_stock =math.floor(amount_remaining/prices[index_slope][-1])
            amount_remaining = amount_remaining - prices[index_slope][-1]*num_stock
            trans[name[index_slope]] = names[index_slope]+' BUY ' + str(int(num_stock))
            
        
    for j in range(k):
        index_slope = slope_list.index(sort_slope[j])
        if sort_slope[j]>0 and owned[index_slope]>0:
            trans[name[index_slope]] = names[index_slope]+' SELL ' + str(owned[index_slope]) 
            
    print len(trans.keys())
    for x in trans:
        print trans[x]
        
if __name__ == '__main__':
    m, k, d = [float(i) for i in raw_input().strip().split()]
    k = int(k)
    d = int(d)
    names = []
    owned = []
    prices = []
    for data in range(k):
        temp = raw_input().strip().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(i) for i in temp[2:7]])

    printTransactions(m, k, d, names, owned, prices)