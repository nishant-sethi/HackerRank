
/*
 * Create the function factorial here
 */
function factorial(n){
    let fact;
    let i;
    fact=1;
    for (i=1;i<=n;i++){
        fact=fact*i;
    }
    return fact; 
}