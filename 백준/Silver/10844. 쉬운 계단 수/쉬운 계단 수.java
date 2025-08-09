
import java.io.*;
import java.util.*;

class Solution {
    public long solution(int n) {

        final long mod = 1000000000;

        long[][] dp = new long[n + 1][10];

        for (int j = 1; j < 10; j++) {
            dp[1][j] = 1;
        }

        for (int i = 2; i < n + 1; i++) {
            for (int j = 0; j < 10; j++) {
                if (j == 0) {
                    dp[i][j] = dp[i - 1][j + 1] % mod;
                } else if (j == 9) {
                    dp[i][j] = dp[i - 1][j - 1] % mod;
                } else {
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % mod;
                }
            }
        }

        long val = 0;
        for (int j = 0; j < 10; j++) {
//          System.out.printf("% d", dp[i][j]);
            val += dp[n][j] % mod;
        }
//                System.out.println();
        return val % mod;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        Solution sol = new Solution();
        System.out.println(sol.solution(n));

    }
}
