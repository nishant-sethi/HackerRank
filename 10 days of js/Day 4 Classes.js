/*
 * Implement a Polygon class with the following properties:
 * 1. A constructor that takes an array of integer side lengths.
 * 2. A 'perimeter' method that returns the sum of the Polygon's side lengths.
 */
function Polygon(sides){
    this.sides=sides;
    this.perimeter=function(){
        var i;
        var a=0;
        for (i=0;i<(this.sides).length;i++){
           
            a=a+this.sides[i];
        }
        return a;
    }  
}