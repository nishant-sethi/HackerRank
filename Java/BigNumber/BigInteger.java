// https://www.hackerrank.com/challenges/java-biginteger/problem

import java.math.BigInteger;
import java.util.Scanner;

public class Solution{

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        String x = scanner.next();
        String y = scanner.next();
        
        BigInteger b = new BigInteger(x);
        BigInteger b1 = new BigInteger(y);

        System.out.println(b.add(b1));
        System.out.println(b.multiply(b1));
        

    }

}