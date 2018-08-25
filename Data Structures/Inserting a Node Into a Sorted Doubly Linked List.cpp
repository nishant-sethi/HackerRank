Node* SortedInsert(Node *head,int data)  
 {  
   // Complete this function  
   // Do not write the main method.   
   Node *temp = new Node;  
   temp->data = data;  
   temp->next = NULL;  
   temp->prev = NULL;  
   if(head == NULL){  
     head = temp;  
   }else{  
     Node *temp1 = temp;  
     temp->next = head;  
     head = temp;  
     while(temp!= NULL){  
       temp1 = temp;  
       temp = temp->next;  
       if(temp!=NULL){  
         if(temp1->data>temp->data){  
           int tdata;  
           tdata = temp1->data;  
           temp1->data = temp->data;  
           temp->data = tdata;  
         }  
       }  
     }  
   }  
   return head;  
 }  