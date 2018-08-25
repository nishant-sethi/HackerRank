/*  
  Insert Node at a given position in a linked list   
  The linked list will not be empty and position will always be valid  
  First element in the linked list is at position 0  
  Node is defined as   
  struct Node  
  {  
    int data;  
    struct Node *next;  
  }  
 */  
 Node* InsertNth(Node *head, int data, int position)  
 {  
  // Complete this method only  
  // Do not write main function.  
   Node *cur = new Node,*temp = new Node;  
   temp->data = data;  
   temp->next = NULL;  
   if(head == NULL){  
     head = temp;  
   }else{  
     int i=0;  
     cur = head;  
     while(cur!=NULL){  
       if(position == 0){  
           temp->next = cur;  
           head= temp;  
       }  
       else if(i==position-1){  
         temp->next = cur->next;  
         cur ->next = temp;  
       }else{  
       }i++;  
       cur= cur->next;  
     }  
   }  
   return head;  
 }  