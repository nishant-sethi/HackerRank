import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Arrays;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int cases = in.nextInt();
        double[] numbers = new double[cases];
        for(int i = 0; i < cases; i++) {
            numbers[i] = in.nextDouble();
        }
        in.close();
        double mean = calculateMean(numbers);
        double median = calculateMedian(numbers);
        double mode = calculateMode(numbers);
        double sd = calculateStandardDeviation(numbers, mean);
        
        System.out.println(mean);
        System.out.println(median);
        System.out.println((int) mode);
        DecimalFormat decimalFormat = new DecimalFormat("0.#");
        System.out.println(decimalFormat.format(sd));
        double lenght = (double) numbers.length;
        double lower = mean - 1.96*sd/Math.pow(lenght, 0.5);
        double upper = mean + 1.96*sd/Math.pow(lenght, 0.5);
        System.out.println(decimalFormat.format(lower) + " " + decimalFormat.format(upper));

    }
    
    public static double calculateStandardDeviation(double[] numbers, double mean) {
        double result = 0.0;
        int length = numbers.length;
        for(int i = 0; i < length; i++) {
            // += (c-m)^2
            result += Math.pow((numbers[i] - mean),2);
        }
        result /= length;
        result = Math.pow(result, 0.5);
        return result;
    }
    
    public static double calculateMode(double[] numbers) {
        double result = numbers[0];
        Arrays.sort(numbers);
        int modeCount = 0;
        int greatestModeCount = 0;
        double lastDigit = 0.0;
        for(int i = 0; i < numbers.length; i++) {            
            if(lastDigit == numbers[i]) {
                modeCount++;
            } else {
                if(modeCount > greatestModeCount) {
                   greatestModeCount = modeCount;	
                   result = lastDigit;
                }
                modeCount = 0;
            }
            lastDigit = numbers[i];
        }
        return result;
    }
    
    public static double calculateMedian(double[] numbers) {
        double result = 0.0;
        int length = numbers.length;
        Arrays.sort(numbers);
        if(length % 2 == 0) {
            int i = length/2;
            result = (numbers[i] + numbers[i - 1])/2;
        } else {
            int i = (length - 1)/2;
            result = numbers[i];
        }
        return result;
    }
    
    public static double calculateMean(double[] numbers) {
        double result = 0.0;
        int length = numbers.length;
        for(int i = 0; i < length; i++) {
            result += numbers[i];
        }
        result /= length;
        return result;
    }
}