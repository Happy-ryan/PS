import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int i = 1; i <= t; i++) {
            int num = scanner.nextInt();
            System.out.println("Case #" + i + ": " + checkRound(num));
        }
        scanner.close();
    }

    public static String checkRound(int num) {
        if (num <= 25) {
            return "World Finals";
        }
        if (num <= 1000) {
            return "Round 3";
        }
        if (num <= 4500) {
            return "Round 2";
        }
        return "Round 1";
    }
}