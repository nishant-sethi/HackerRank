// https://www.hackerrank.com/challenges/java-negative-subarray/problem

import java.util.*;

public class Solution {
        static int count = 0;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int arr[] = new int[n];
        for(int i=0; i<n; i++)
            arr[i] = scanner.nextInt();

        for(int i=0; i<arr.length; i++){
            int sum = 0;
            for(int j=i; j<arr.length; j++){


                sum += arr[j];
                if (sum < 0) {
                    count++;
                }


            }

        }
        System.out.println(count);

    }
}