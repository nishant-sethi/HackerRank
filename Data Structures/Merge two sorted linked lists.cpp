/*  
  Merge two sorted lists A and B as one linked list  
  Node is defined as   
  struct Node  
  {  
    int data;  
    struct Node *next;  
  }  
 */  
 Node* MergeLists(Node *headA, Node* headB)  
 {  
  // This is a "method-only" submission.   
  // You only need to complete this method   
   Node *head=NULL, *cur,*prev = NULL;  
   Node *curA,*curB;  
   head = headA;  
   cur = head;  
   curB = headB;  
   while(curB !=NULL){  
     if(cur== NULL){  
       head = headB;  
       break;  
     }else{    if(cur->data > curB->data){  
       curA = curB;  
       curB = curB->next;  
       curA->next = cur;  
       if(prev == NULL){  
         head = curA;  
       }else{  
         prev->next = curA;  
       }  
       prev = cur;  
       cur = cur->next;  
     }else{  
       if(cur->next !=NULL){  
         prev = cur;  
         cur = cur->next;  
       }else{  
         cur->next = curB;  
         break;  
       }  
     }}  
   }return head;  
 }  