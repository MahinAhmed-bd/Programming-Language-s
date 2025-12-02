package assignment2;

import java.util.Scanner;

public class assignment2 {

    public static void main(String[] args) {
        int a, b, c;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a :");
        a = input.nextInt();
        System.out.println("Enter b :");
        b = input.nextInt();
        System.out.println("Enter c :");
        c = input.nextInt();
        if ((a > b) && (a > c)) {
            System.out.println("a is bigger then other number");
        } else if ((b > c) && (b > a)) {
            System.out.println(" b is bigger then other number");
        } else {
            System.out.println(" c is bigger then other number");
        }
    }
}
