// https://www.hackerrank.com/challenges/java-exception-handling-try-catch/problem

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
        try{
            int x = sc.nextInt();
            int y = sc.nextInt();
            
            System.out.println(x/y);
        }
        catch(InputMismatchException e){
            System.out.println(e.getClass().toString().substring(6));
        }
        catch(Exception e){
            System.out.println(e);
        }
    }
}