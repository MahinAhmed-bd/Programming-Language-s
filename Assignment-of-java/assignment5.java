package assignment5;

import java.util.Scanner;

public class assignment5 {

    public static void main(String[] args) {
        int mark;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter your mark :");
        mark = input.nextInt();
        String grade;
        switch (mark / 10) {
            case 10:
            case 9:
            case 8:
                grade = "A+";
                break;
            case 7:
                grade = "A-";
                break;
            case 6:
                grade = "B";
                break;
            case 5:
                grade = "C";
                break;
            case 4:
                grade = "D";
                break;
            default:
                grade = "F";
        }
        System.out.println("The Student Garde is :" + grade);
    }
}
