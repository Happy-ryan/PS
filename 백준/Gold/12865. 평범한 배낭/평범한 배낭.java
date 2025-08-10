import java.io.*;
import java.util.*;

class Solution {
    public long solution(int n, int k, int[][] infos) {
        // 냅색
        // item : 가방
        // 행 : i번째 가방
        // 열 : 무게(제한있는거고)
        // dp에 들어가는 값 : 가치
        // dp[i][j] = i번째 가방을 고려햇을 때 무게 j일때 최고
        long[][] dp = new long[n + 1][k + 1];
        long inf = (long) 1e18;

        for(int i = 0; i < n + 1; i++) {
            for (int j = 0; j < k + 1; j++) {
                dp[i][j] = -inf;
            }
        }

        dp[0][0] = 0;

        for (int i = 1; i < n + 1; i++) {
            int w = infos[i - 1][0];
            int v = infos[i - 1][1];
            for (int j = 0; j < k + 1; j++) {
                // i번째 가방 고려...그 전 선택한 가방에서 j무게일 떼 최고가치
                dp[i][j] = dp[i - 1][j];
                // i 선택 + w만큼 채우기..
                if (j - w >= 0) {
                    dp[i][j] = Math.max(dp[i][j], dp[i - 1][j - w] + v);
                }
            }
        }

        long answer = -inf;

        for (int j = 0; j < k + 1; j++) {
            answer = Math.max(answer, dp[n][j]);
        }

        return answer;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());  // 물품의 수
        int k = Integer.parseInt(st.nextToken());  // 배낭의 최대 무게

        int[][] infos = new int[n][2];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            infos[i][0] = Integer.parseInt(st.nextToken());  // 무게
            infos[i][1] = Integer.parseInt(st.nextToken());  // 가치
        }

        Solution sol = new Solution();
        System.out.println(sol.solution(n, k, infos));

    }
}