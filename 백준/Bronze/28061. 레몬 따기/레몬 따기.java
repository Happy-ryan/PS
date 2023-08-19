// 4
// 100 97 90 12

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, a, ans, max;

        n = sc.nextInt();
        
        String check = "";

        max = 0;
        for(int i = 1; i <= n;i++){
            a = sc.nextInt();
            ans = a - (n + 1 - i);
            max = Math.max(max, ans);
        }
    System.out.print(max);
    }
}