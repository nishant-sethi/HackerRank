// https://www.hackerrank.com/challenges/java-generics/problem

class Printer
{
    public <T> void printArray(T[] t){
        for(T t1 : t)
            System.out.println(t1);
}

}