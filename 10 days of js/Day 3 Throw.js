/*
 * Complete the isPositive function.
 * If 'a' is positive, return "YES".
 * If 'a' is 0, throw an Error with the message "Zero Error"
 * If 'a' is negative, throw an Error with the message "Negative Error"
 */
function isPositive(a) {
    if (Math.sign(a)==1){
            return "YES";}
        
        else if(Math.sign(a)==0){
            throw new Error("Zero Error");
        }
        else{
            throw new Error("Negative Error");
        } 
}