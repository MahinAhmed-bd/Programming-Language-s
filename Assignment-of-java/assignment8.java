package assignment8;

import java.util.Scanner;

public class assignment8 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a number1 :");
        int num1 = input.nextInt();
        System.out.println("Enter a number2 :");
        int num2 = input.nextInt();
        int result = num1;
        for (int i = 0; i < num2; i++) {
            result--;
        }
        System.out.print("The Subruction is :" + result);
    }
}
