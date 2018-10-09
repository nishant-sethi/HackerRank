// https://www.hackerrank.com/challenges/prime-checker/problem

import static java.lang.System.*;
class Prime {
    void checkPrime(int... numbers) {  
        for (int number : numbers) {            
            if (BigInteger.valueOf(number).isProbablePrime(5)) {
                System.out.print(number + " ");
            }
        }
        System.out.println();
    }  
}