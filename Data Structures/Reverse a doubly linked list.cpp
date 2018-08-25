/*  
   Reverse a doubly linked list, input list may also be empty  
   Node is defined as  
   struct Node  
   {  
    int data;  
    Node *next;  
    Node *prev;  
   }  
 */  
 Node* Reverse(Node* head)  
 {  
   Node *cur = head,*temp = new Node;  
   // Complete this function  
   // Do not write the main method.   
   while(cur !=NULL){  
     temp->next = cur->next;  
     temp->prev = cur->prev;  
     cur->next = temp->prev;  
     cur->prev = temp->next;  
     cur = temp->next;  
     if(cur!=NULL){  
       head = cur;  
     }  
   }  
   return head;  
 }  