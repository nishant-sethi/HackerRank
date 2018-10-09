// https://www.hackerrank.com/challenges/java-end-of-file/problem

import java.io.BufferedInputStream;
import java.util.Scanner;

class Solution{
    public static void main(String[] args) {
        Scanner stdin = new Scanner(new BufferedInputStream(System.in));
        int i = 1;
        while (stdin.hasNext()) {
            System.out.println(i + " " + stdin.nextLine());
            i++;
        }
    }
}