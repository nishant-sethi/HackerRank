
/*The tree node has data, left child and right child 
struct node
{
    int data;
    node* left;
    node* right;
};

*/
int height(node * root)
{
    int lh,rh;
    if(root==NULL)
        return 0;
    else{
        lh=height(root->left);
        rh=height(root->right);
        if(lh>rh)
            return ++lh;
        else
            return ++rh;
    }
  
}
  
