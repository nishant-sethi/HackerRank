/*  
  Print elements of a linked list in reverse order as standard output  
  head pointer could be NULL as well for empty list  
  Node is defined as   
  struct Node  
  {  
    int data;  
    struct Node *next;  
  }  
 */  
 void ReversePrint(Node *head)  
 {  
  // This is a "method-only" submission.   
  // You only need to complete this method.   
   int a[100],i=0;  
   while(head!=NULL){  
     a[i] = head->data;  
     i++;  
     head = head->next;  
   }  
   for(int j = i-1;j>=0;j--){  
     cout<<a[j]<<endl;  
   }  
 }  