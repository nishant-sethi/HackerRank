/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    let s1=new Set(['a','e','i','o','u']);
    let s2=new Set(['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']);
    var i,j;
    for(i=0;i<=s.length;i++){
        if(s1.has(s[i])){
            console.log(s[i]);
        }
        
    }
    for(j=0;j<=s.length;j++){
        if(s2.has(s[j])){
            console.log(s[j]);
        }
        
    }  
}