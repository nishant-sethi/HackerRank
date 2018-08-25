/*  
  Reverse a linked list and return pointer to the head  
  The input list will have at least one element   
  Node is defined as   
  struct Node  
  {  
    int data;  
    struct Node *next;  
  }  
 */  
 Node* Reverse(Node *head)  
 {  
  // Complete this method  
   Node *prev = NULL;  
   Node *cur = head;  
   Node *next ;  
   while(cur!=NULL){  
     next = cur->next;  
     cur->next = prev;  
     prev = cur;  
     cur = next;  
   }  
   head = prev;  
   return head;  
 }  