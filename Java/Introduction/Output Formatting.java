// https://www.hackerrank.com/challenges/java-output-formatting/problem

import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            System.out.println("================================");
            for(int i=0;i<3;i++) {
            String s2 = sc.next();
            int n = sc.nextInt();
            String s=addWhiteSpaces(s2);
            String s1;
                if(n<100) {
                    if(n<10)
                        s1 = "00" + n;
                    else
                        s1 = "0" + n;
                System.out.println(s+s1);
            }
              
            
            if(n>=100)
                System.out.println(s+n);

        }
            System.out.println("================================");

    }
    static String addWhiteSpaces(String s){
        if(s.length()<15)
            for(int i=s.length();i<15;i++)
                s = s+" ";
        return s;
    }
}



