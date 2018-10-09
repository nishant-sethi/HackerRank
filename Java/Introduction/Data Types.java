// https://www.hackerrank.com/challenges/java-datatypes/problem

import java.util.Scanner;

class Solution{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i=0;i<n;i++){

            try {
                long l = sc.nextLong();
                System.out.println(l + " can be fitted in:");
                if (l >= -128 && l <= 127)
                    System.out.println("* byte");

                if (l >= Short.MIN_VALUE && l <= Short.MAX_VALUE) {
                    System.out.println("* short");
                }
                if (l >= Integer.MIN_VALUE && l <= Integer.MAX_VALUE) {
                    System.out.println("* int");
                }
                if (l >= Long.MIN_VALUE && l <= Long.MAX_VALUE) {
                    System.out.println("* long");
                }
            }
            catch (Exception e){
                System.out.println(sc.next()+" can't be fitted anywhere.");
            }


        }
    }
}