#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef struct a{
    char a[1000];
    int top;
}stack;
void createstack(stack *s){
    s->top=-1;
}
int isEmpty(stack *s){
    if(s->top==-1)
        return 1;
    else return 0;
}
void push(stack *s, char c){
    if(s->top==-1)
        s->top=0;
    else s->top++;
    s->a[s->top]=c;
}
char peek(stack *s){
    return s->a[s->top];
}
void pop(stack *s){
    s->top--;
}
void deletestack(stack *s){
    s->top=-1;
}
int isBalanced(char str[],stack *s){
    int i;
    char c;
    for(i=0;i<strlen(str);i++){
        if(str[i]=='(' || str[i]=='{' || str[i]=='[')
            push(s,str[i]);
        else{
            c=peek(s);
            if(str[i]==')'){
                if(c=='(' && !isEmpty(s))
                    pop(s);
                else return 0;
            }
            else if(str[i]=='}'){
                if(c=='{' && !isEmpty(s))
                    pop(s);
                else return 0;
            }
            else if(str[i]==']'){
                if(c=='[' && !isEmpty(s))
                    pop(s);
                else return 0;
            }
        }
    }
     if(isEmpty(s))
            return 1;
     else return 0;
}
int main(){
    int n,i;
    char str[1000];
    scanf("%d",&n);
    stack s;
    for(i=0;i<n;i++){
        scanf("%s",str);
        createstack(&s);
        if(strlen(str)==1)
            printf("NO\n");
        else if(isBalanced(str,&s))
            printf("YES\n");
        else
            printf("NO\n");
        deletestack(&s);
    }
    return 0;
}
