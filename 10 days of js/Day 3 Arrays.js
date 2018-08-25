/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function
    var y=nums.sort(function(a, b){return a - b});
    var x=y.reverse();
    
        
    let i;
    for (i=0;i<=nums.length;i++){
        if (parseInt(x[i])>parseInt(x[i+1])){
           return x[i+1]; 
        }
        
    } 
}