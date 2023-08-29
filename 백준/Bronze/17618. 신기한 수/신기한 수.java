import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] dp = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            if (solution(i)) {
                dp[i] = dp[i - 1] + 1;
            } else {
                dp[i] = dp[i - 1];
            }
        }

        System.out.println(dp[n]);
    }

    public static boolean solution(int i) {
        boolean flag = false;
        int x = i;
        int sum = 0;

        while (true) {
            if (i / 10 == 0) {
                sum += i % 10;
                break;
            }
            sum += i % 10;
            i /= 10;
        }

        if (x % sum == 0) {
            flag = true;
        }
        return flag;
    }
}