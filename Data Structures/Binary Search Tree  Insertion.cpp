/*
Node is defined as 

typedef struct node
{
   int data;
   node * left;
   node * right;
}node;

*/
node* newNode(int value){
    node *ptr;
    ptr=(node*)malloc(sizeof(node));
    ptr->data=value;
    ptr->left=ptr->right=NULL;
    return ptr;
}

node * insert(node * root, int value)
{
    if(root==NULL || root->data==value)
        return newNode(value);
    else if(root->data>value)
        root->left=insert(root->left,value);
    else
        root->right=insert(root->right,value);

   return root;
}
