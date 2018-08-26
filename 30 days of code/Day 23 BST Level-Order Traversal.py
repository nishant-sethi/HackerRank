    def levelOrder(self,root):
        #Write your code here
        h = self.height(root)
        for i in range(1, h+1):
            self.printGivenLevel(root, i)
    
    def height(self,node):
        if node is None:
            return 0
        else :
            # Compute the height of each subtree 
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            #Use the larger one
            if lheight > rheight :
                return lheight+1
            else:
                return rheight+1
    def printGivenLevel(self,root ,level):
        if root is None:
            return
        if level == 1:
            print(root.data,end=" ")
        elif level > 1 :
            self.printGivenLevel(root.left , level-1)
            self.printGivenLevel(root.right , level-1)