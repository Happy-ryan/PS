import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n, price, sum = 0;

        n = sc.nextInt();
        for(int i = 1; i <= n; i++){
            price = sc.nextInt();
            sum += price;
        }
        System.out.print(sum);
    }
}