import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        for (int i = 1; i <= t; i++) {
            int n = scanner.nextInt();
            int s = scanner.nextInt();
            int d = scanner.nextInt();
            int ans = 0;

            for (int j = 0; j < n; j++) {
                int a = scanner.nextInt();
                int b = scanner.nextInt();
                if (s * d >= a) {
                    ans += b;
                }
            }

            System.out.println("Data Set " + i + ":\n" + ans + "\n");
        }
    }
}
