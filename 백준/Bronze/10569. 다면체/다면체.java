import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n, v, e;

        n = sc.nextInt();
        for(int i = 0; i < n; i++){
            v = sc.nextInt();
            e = sc.nextInt();
            System.out.println(e + 2 - v);
        }
    }
}