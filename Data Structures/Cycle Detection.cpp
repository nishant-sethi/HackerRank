/*  
  Detect loop in a linked list   
  List could be empty also  
  Node is defined as   
  struct Node  
  {  
    int data;  
    struct Node *next;  
  }  
 */  
 int HasCycle(Node* head)  
 {  
   // Complete this function  
   // Do not write the main method  
   Node* fast = head, *slow = head;  
   while(fast!= NULL){  
     fast = fast->next->next;  
     slow = slow->next;  
     if(fast == slow){  
       return 1;  
     }  
   }return 0;  
 }  