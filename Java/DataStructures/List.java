// https://www.hackerrank.com/challenges/java-list/problem

import java.util.*;

public class Solution {
        static List<Integer> list = new ArrayList<>();
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for(int i=0; i<n; i++){
            list.add(scanner.nextInt());
        }

        int x = scanner.nextInt();
        int arr[] = new int[2];
        for(int i=0; i<x; i++){
            String query = scanner.next();


            if(query.equals("Insert")) {
                for(int j=0; j<2; j++)
                    arr[j] = scanner.nextInt();
                list.add(arr[0], arr[1]);
            }
            if(query.equals("Delete")){
                int y = scanner.nextInt();
                list.remove(y);
            }

        }
        for(int i=0; i<list.size(); i++)
            System.out.print(list.get(i) + " ");

    }
}