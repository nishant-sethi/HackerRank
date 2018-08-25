/*  
  Get Nth element from the end in a linked list of integers  
  Number of elements in the list will always be greater than N.  
  Node is defined as   
  struct Node  
  {  
    int data;  
    struct Node *next;  
  }  
 */  
 int GetNode(Node *head,int positionFromTail)  
 {  
  // This is a "method-only" submission.   
  // You only need to complete this method.   
   int n = 0;  
  Node *cur = head;  
   while(cur!=NULL){  
     n++;  
     cur = cur->next;  
   }  
    n --;  
   cur = head;  
   while(cur!=NULL){  
     if(n == positionFromTail){  
       return cur->data;  
     }  
     n--;  
     cur = cur ->next;  
   }  
   return 0;  
 }  