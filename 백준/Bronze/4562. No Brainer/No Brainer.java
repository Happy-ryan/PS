import java.util.*;

public class Main {
    private static int n;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            if (x >= y) {
                System.out.println("MMM BRAINS");
            }
            else{
                System.out.println("NO BRAINS");
            }
        }
    }
}