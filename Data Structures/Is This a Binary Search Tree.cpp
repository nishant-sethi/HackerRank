/* Hidden stub code will pass a root argument to the function below. Complete the function to solve the challenge. Hint: you may want to write one or more helper functions.  

The Node struct is defined as follows:
   struct Node {
      int data;
      Node* left;
      Node* right;
   }
*/
   bool checkBST(Node* root) {
      return isBST(root,-1,100001);
   }
    bool isBST(Node *root,int min,int max){
        if(root==NULL)
            return true;
        if(root->data<min || root->data>max)
            return false;
        return isBST(root->left,min,root->data-1) && isBST(root->right,root->data+1,max);
    }
