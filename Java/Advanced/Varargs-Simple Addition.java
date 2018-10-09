// https://www.hackerrank.com/challenges/simple-addition-varargs/problem

class Add{
    void add(int... x){
        int sum = 0;
        String s = "";
        for(int x1 : x){
            s += x1 + "+";
            sum += x1;
        }

        System.out.print(s.substring(0, s.length()-1) + "=" + sum);
        System.out.println();
    }
}