// https://www.hackerrank.com/challenges/java-string-tokens/problem

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        String arr[] = s.split("[!,?._'@\\s]+");
        for(String s1: arr)
            list.add(s1);
        list.removeAll(Arrays.asList("", null));
        System.out.println(list.size());
        for(String s1: list)
            System.out.println(s1);
        scan.close();
    }
}