class Solution:
    # Write your code here
    def __init__(self):
        self.stack=[]
        self.queue=[]
    def pushCharacter(self,s):
        self.stack.append(s)
    def enqueueCharacter(self,s):
        self.queue.append(s)
    def popCharacter(self):
        return self.stack.pop()
    def dequeueCharacter(self):
        return self.queue.pop(0)