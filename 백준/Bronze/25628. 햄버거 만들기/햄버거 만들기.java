import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a, b;

        a = sc.nextInt();
        b = sc.nextInt();

        a /= 2;

        System.out.print(Math.min(a, b));
    }
}