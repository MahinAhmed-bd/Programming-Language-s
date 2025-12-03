package com.mycompany.alltest;

import java.util.Scanner;

public class AllTEST {

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
