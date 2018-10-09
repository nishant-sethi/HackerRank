// https://www.hackerrank.com/challenges/java-arraylist/problem

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int cases = scanner.nextInt(), n = 0;
        int[][] input = new int[cases][];
        int k = 0;
        for(int i = 0; i < cases; ++ i)
        {
            n = scanner.nextInt();
            int[] array = new int[n];
            
            for(int j = 0; j  <n; ++ j)
                array[j] = scanner.nextInt();
            
            input[k ++] = array;
        }
            
        int q = scanner.nextInt(), x = 0, y = 0;
        
        for(int i = 0; i < q; ++ i)
        {
            x = scanner.nextInt() - 1;
            y = scanner.nextInt() - 1;
            
            if(x >= cases)
                System.out.println("ERROR!");
            
            else
            {
                if(input[x] == null || y >= input[x].length)
                    System.out.println("ERROR!");
                
                else
                    System.out.println(input[x][y]);
            }
        }
        
        scanner.close();
    }
}