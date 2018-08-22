#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    double mealcost,tip,tax,totalcost,result;
    int tip_per,tax_per;
    scanf("%lf%d%d",&mealcost,&tip_per,&tax_per);
    tip=(mealcost*tip_per)/100;
    tax=(mealcost*tax_per)/100;
    totalcost=mealcost+tip+tax;
    if(totalcost-(int)totalcost>0.5)
        totalcost++;
    printf("The total meal cost is %d dollars.",(int)totalcost);
    return 0;
}
