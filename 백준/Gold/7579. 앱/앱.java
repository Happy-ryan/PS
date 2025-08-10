import java.io.*;
import java.util.*;

class Solution {
    public long solution(int N, int M, int[] memories, int[] costs) {
        // 냅색
        // item : 앱
        // 행 : i번째 앱
        // 열 : 메모리.. > 열이 10억... > 반대로 생각해야함..
        // dp에 들어가는 값 : 비용의 최소...> 열 : 비용 / dp : 메모리
        // dp[i][j] = i번째 앱 고려했을 때 비용이 j일 때 확보할 수 있는 메모리..

        long inf = (long) 1e18;

        long[][] dp = new long[N + 1][100 * 100 + 1];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < 100 * 100 + 1; j++) {
                dp[i][j] = -inf; // 메모리 M이상 확보
            }
        }

        dp[0][0] = 0;

        for (int i = 1; i < N + 1; i++) {
            int c =  costs[i - 1]; // w(열)
            int m =   memories[i - 1];// v(가치)
            for (int j = 0; j < 100 * 100 + 1; j++) {
                dp[i][j] = dp[i - 1][j];
                if (j - c >= 0) {
                    dp[i][j] = Math.max(dp[i][j], dp[i - 1][j - c] + m);
                }
            }
        }

//        // 비용(열) / 메모리(M이상)
//        for (int i = 1; i < N; i++) {
//            for (int j = 0; j < 10; j++) {
//                if (dp[i][j]  < 0) {
//                    System.out.printf("- ", dp[i][j]);
//                }
//                else {
//                    System.out.printf("%d ", dp[i][j]);
//                }
//            }
//            System.out.println();
//        }

        for(int j = 0; j < 100 * 100 + 1; j++){
            if (dp[N][j] >= M) {
                return j;
            }
        }
        return -1;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());  // 물품의 수
        int M = Integer.parseInt(st.nextToken());  // 배낭의 최대 무게

        int[] memories = new int[N];
        int[] costs = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            memories[i] = Integer.parseInt(st.nextToken());  // 무게
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            costs[i] = Integer.parseInt(st.nextToken());  // 가치
        }

        Solution sol = new Solution();
        System.out.println(sol.solution(N, M, memories, costs));

    }
}