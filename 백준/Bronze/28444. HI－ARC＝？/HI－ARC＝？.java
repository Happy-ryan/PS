import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h, i, a, b, c;
        h = sc.nextInt();
        i = sc.nextInt();
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();
        
        System.out.print((h * i) - (a * b * c));
    }
}