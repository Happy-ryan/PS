import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //2^32
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        System.out.print(pow(a, b, c));

    }
    private static long pow(int n, int k, int mod) {
        if (k == 1) {
            return  n % mod;
        }

        long x = pow(n, k / 2, mod);

        if (k % 2 != 0) {
            return  (n * ((x * x) % mod)) % mod ;
        }
        else {
            return  (x * x) % mod;
        }
    }
}