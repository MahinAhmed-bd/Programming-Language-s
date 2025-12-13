// assignment number 11

import java.util.Scanner;

public class assignment11 {

    String Name;
    int Roll;

    constructor() {
        Scanner inp = new Scanner(System.in);
        System.out.println("Enter Your Name :");
        Name = inp.nextLine();
        System.out.println("Enter Your Roll :");
        Roll = inp.nextInt();
    }

    void Display() {
        System.out.println("Your Name is :" + Name);
        System.out.println("Your Roll is :" + Roll);
    }

    public static void main(String[] args) {
        constructor d = new constructor();
        d.Display();
    }
}
