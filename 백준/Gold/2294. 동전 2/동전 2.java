import java.io.*;
import java.util.*;

class Solution {
    public int solution(int N, int K, int[] moneys) {
        // 무제한 + 순서 문제 없음 <- 해당 유형
        // 무제한 + 순서 문제
        // 제한 + 순서 문제 없음
        // 제한 + 순서 문제

        // dp[i][j] = i반째 동전을 고려했을 때... j라는 가치 / dp[i][j] = 동전의 개수
        int[][] dp = new int[N + 1][K + 1];
        int inf = (int) 1e9;
        for (int i = 0; i < N + 1; i++) {
            for (int j = 0; j < K + 1; j++) {
                dp[i][j] = inf;
            }
        }
        dp[0][0] = 0;
        for(int i = 1; i < N + 1; i++) {
            for (int j = 0; j < K + 1; j++) {
                dp[i][j] = dp[i - 1][j];
                if (j - moneys[i - 1] >= 0) {
                    dp[i][j] = Math.min(dp[i][j], dp[i][j - moneys[i - 1]] + 1);
                }
            }
        }

//        for (int i = 1; i < N + 1; i++) {
//            for (int j = 0; j < K + 1; j ++) {
//                if (dp[i][j] < 0) {
//                    System.out.printf("- ");
//                }
//                else {
//                    System.out.printf("%d ", dp[i][j]);
//                }
//            }
//            System.out.println();
//        }

        if (dp[N][K] >= inf){
            return -1;
        }
        return dp[N][K];
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());  // 동전 종류
        int K = Integer.parseInt(st.nextToken());  // 목표 금액

        int[] moneys = new int[N];
        for (int i = 0; i < N; i++) {
            moneys[i] = Integer.parseInt(br.readLine());  // 각 동전의 가치
        }

        Solution sol = new Solution();
        System.out.println(sol.solution(N, K, moneys));

    }
}