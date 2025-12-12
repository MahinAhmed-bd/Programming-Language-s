
import java.util.Arrays;

public class array {

    public static void main(String[] args) {
        int i;
        int[] array = {5, 8, 6, 10, 7, 1, 4, 3, 2, 9};
        Arrays.sort(array);
        for (i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
    }
}
