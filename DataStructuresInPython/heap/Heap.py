'''
Created on Jun 4, 2018

@author: nishant.sethi
'''

import heapq
class Heap:
    def __init__(self,lst=None):
        if lst is None:
            self.lst=[]
        self.lst=lst
    
    def create(self):
        heapq.heapify(self.lst)
    
    def insert(self,item):
        heapq.heappush(self.lst, item)
        
    def remove(self):
        heapq.heappop(self.lst)
    
    def replace(self,item):
        heapq.heapreplace(self.lst, item) 
    
    