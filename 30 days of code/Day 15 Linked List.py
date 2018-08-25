    def insert(self,head,data): 
        new_node=Node(data)
        if head is None:
            head=new_node
            return head
        else:
            x=head
            while x.next:
                x=x.next
            x.next=new_node
            return head