/*  
  Remove all duplicate elements from a sorted linked list  
  Node is defined as   
  struct Node  
  {  
    int data;  
    struct Node *next;  
  }  
 */  
 Node* RemoveDuplicates(Node *head)  
 {  
  // This is a "method-only" submission.   
  // You only need to complete this method.   
   Node *cur = head;  
   while(cur->next!=NULL){  
     if(cur->data == cur->next->data)  
       cur->next = cur->next->next;   
     else  
     cur = cur->next;  
   }  
   return head;  
 }  
