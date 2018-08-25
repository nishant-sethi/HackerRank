/*  
  Delete Node at a given position in a linked list   
  Node is defined as   
  struct Node  
  {  
    int data;  
    struct Node *next;  
  }  
 */  
 Node* Delete(Node *head, int position)  
 {  
  // Complete this method  
   Node *cur;  
   cur = head;  
   if(position == 0){  
     head = head->next;  
   }else{  
     int i = 0;  
     while(cur!= NULL){  
       if(i == (position)-1){  
         cur -> next = (cur->next)->next;  
         break;  
       }else{  
       cur = cur->next;  
       }  
       i++;  
     }  
   }  
   return head;  
 }  