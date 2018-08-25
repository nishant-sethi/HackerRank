/*
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) {
    var s1="";
    var s2="";
    var i;
    try{
        var x=s.split("");
        var y=x.reverse();
        for (i=0;i<=(y.length)-1;i++){
            s1=s1+y[i];
            
        }
        s2=s1.trim();
        
    }
    catch(err){
        console.log(err.message);
    }
    finally {
        if (s2!=""){
            console.log(s2);        
        }
        else{
            console.log(s);
        }
    } 
}