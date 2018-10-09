// https://www.hackerrank.com/challenges/java-factory/problem

try{
return (Food)Class.forName(order.substring(0,1).toUpperCase()+order.substring(1)).newInstance();
}catch(Exception e){System.out.println(e);return null;}