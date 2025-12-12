package assignment6;

public class assignment6 {

    public static void main(String[] args) {
        int i, sum = 0;
        for (i = 1; i <= 99; i++) {
            sum = sum + (i * i);
        }
        System.out.println("The sum of series is: " + sum);
    }
}
