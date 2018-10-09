// https://www.hackerrank.com/challenges/java-loops/problem

import java.util.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            
            for(int j=0;j<n;j++){
                System.out.print(a+calcPower(j)*b+" ");
            }
            System.out.println();
        }

    }
    static int calcPower(int n){
        int n1 = 0;
        for(int i=0;i<=n;i++)
            n1 = (int) (n1 + Math.pow(2,i));
        return n1;
    }
}