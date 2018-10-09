// https://www.hackerrank.com/challenges/java-stdin-stdout/problem

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class AB {

    public static void main(String[] args) throws IOException{
        InputStreamReader r = new InputStreamReader(System.in);
        BufferedReader read = new BufferedReader(r);
        int i = Integer.parseInt(read.readLine());
        double d = Double.parseDouble(read.readLine());
        String s = read.readLine();


        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}