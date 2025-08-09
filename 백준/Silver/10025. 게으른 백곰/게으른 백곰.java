import java.io.*;
import java.util.*;

class Solution {
    public static int solution(int N, int K, int[][] pos) {
        // 최적위치 +/- K 일 때 얼음합의 최대 값
        // K 라는 고종 사이즈가 존재 > 슬라이딩 윈도우 의심!!
        int maxN = 1000000;
        int maxP = 0;
        int[] grid = new int[maxN + 1]; // 0base
        for (int[] p : pos) {
            int g = p[0];
            int x = p[1];
            maxP = Math.max(maxP, x);
            grid[x] = g;
        }

//        for (int i = 0; i < 20; i++) {
//            System.out.printf("%d ", grid[i]);
//        }
//        System.out.println();

        int initValue = 0;
        // 0base!!
        // K에서 시작... 1 ~ K - 1(K개)  + K + K(1개) + 1 + 2 * K (K개) = 2K + 1 (총)
        // K 2,00,000 이므로 여기서 out난 것...
        for (int i = 0; i < Math.min(2 * K + 1, maxN); i++){
            initValue += grid[i]; // 1base
        }
        int val = initValue;
        // i가 maxN까지 나면 index out 될 것!! <- 주의
        for (int i = K + 1; i < maxN - K + 1; i++) {
            val -= grid[i - K - 1]; // 있던 값 제외
            val += grid[i + K]; // 새로운 값 추가
            initValue = Math.max(val, initValue);
//            System.out.printf("s : %d, e : %d, val: %d", i - K, i + K, val);
//            System.out.println();
        }

        return initValue;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 양동이 개수
        int K = Integer.parseInt(st.nextToken()); // 백곰이 닿을 수 있는 거리

        int[][] buckets = new int[N][2];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int g = Integer.parseInt(st.nextToken()); // 얼음 양
            int x = Integer.parseInt(st.nextToken()); // 좌표
            buckets[i][0] = g; // 좌표
            buckets[i][1] = x; // 얼음 양
        }

        System.out.println(Solution.solution(N, K, buckets));
        br.close();
    }
}