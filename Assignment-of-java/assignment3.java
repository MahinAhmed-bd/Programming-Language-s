package assignment3;

/**
 *
 * @author mahin
 */
import java.util.Scanner;

public class assignment3 {

    public static void main(String[] args) {
        int a, b, c, s;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a :");
        a = input.nextInt();
        System.out.println("Enter b :");
        b = input.nextInt();
        System.out.println("Enter c :");
        c = input.nextInt();
        s = ((a + b + c) / 2);
        if (((a + b) > c) && ((b + c) > a) && ((c + a) > b)) {
            double Area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
            System.out.println("The area of triangle is :" + Area);
        } else {
            System.out.println("Trinagle is not possible");
        }
    }
}
