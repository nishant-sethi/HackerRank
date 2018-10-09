// https://www.hackerrank.com/challenges/phone-book/problem

import java.io.*;
import java.util.*;

public class Solution {

    static HashMap<String, String> map = new HashMap<String, String>();
    
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine();
        for (int i = 0; i < n; i++) {
            map.put(scanner.nextLine(), scanner.nextLine());
        }
        while (scanner.hasNext()) {
            String name = scanner.nextLine();
            if (map.containsKey(name))
                System.out.println(name + "=" + map.get(name));
            else
                System.out.println("Not found");
        }
    }
}