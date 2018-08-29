def levelOrder(self,root):
    #Write your code here
    queue=[]
    not_visited=[root]
    while len(not_visited)!=0:
        x=not_visited.pop(0)
        queue.append(x)
        if x.left is not None:
            not_visited.append(x.left)
        if x.right is not None:
            not_visited.append(x.right)
    for i in queue:
        print(i.data,end=" ")
