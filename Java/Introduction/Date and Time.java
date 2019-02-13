// https://www.hackerrank.com/challenges/java-date-and-time/problem

import java.time.LocalDate;

public class Solution{
    public static String getDay(String day, String month, String year){
        LocalDate date = LocalDate.of((year),(month),(day));
        return String.valueOf(date.getDayOfWeek());

    }
