    def removeDuplicates(self,head):
        #Write your code here
        x=head
        while x.next is not None:
            if x.data==x.next.data:
                x.next=x.next.next
            else:
                x=x.next
        return head