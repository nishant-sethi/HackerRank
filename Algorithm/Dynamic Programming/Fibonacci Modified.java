import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        int i,n;
        BigInteger a,b;
        Scanner sc=new Scanner(System.in);
        a =  sc.nextBigInteger();
        b =  sc.nextBigInteger();
        n = sc.nextInt();
        BigInteger [] val = new BigInteger[n];
        val[0] = a;
        val[1] = b;
        for(i=2;i<n;i++){
            val[i]= (val[i-1].pow(2)).add(val[i-2]);
        }
        System.out.println(val[i-1]);
    
    } 
}