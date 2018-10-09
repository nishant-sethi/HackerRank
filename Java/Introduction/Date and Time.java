// https://www.hackerrank.com/challenges/java-date-and-time/problem

import java.time.LocalDate;

public class Solution{
    public static String getDay(String day, String month, String year){
        LocalDate date = LocalDate.of(Integer.parseInt(year), Integer.parseInt(month), Integer.parseInt(day));
        return String.valueOf(date.getDayOfWeek());

    }