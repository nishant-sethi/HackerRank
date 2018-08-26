    def getHeight(self,root):
        #Write your code here
        count_left=0
        count_right=0
        if root is None:
            return -1
        else:
            count_left=self.getHeight(root.left)
            count_right=self.getHeight(root.right)
            if count_left>count_right:
                return count_left+1
            else:
                return count_right+1
            