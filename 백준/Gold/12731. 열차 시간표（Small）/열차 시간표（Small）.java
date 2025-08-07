import java.io.*;
import java.util.*;

class Solution {
    public static String solution(int tc, int N, int T, int NA, int NB, String[][] plans) {
        int[][] answer = {};

        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));

        for (int i = 0; i < N; i++) {
            int s = calSecond(plans[i][0]);
            int e = calSecond(plans[i][1]);
            heap.offer(new int[] {s, e, i});
        }

        int cntA = 0, cntB = 0;
        PriorityQueue<Integer> A = new PriorityQueue<>();
        PriorityQueue<Integer> B = new PriorityQueue<>();

        while (!heap.isEmpty()) {
            int[] cur = heap.poll();
            int s = cur[0], e = cur[1], idx = cur[2];
            // A에서 출발!
            if (idx < NA) {
                // A역이 비어있으면
                if(A.isEmpty()) {
                    cntA++;
                }
                // A역에 기차 존재
                else {
                    int ready = A.poll();
                    // 준비된 기차 없음! -> 다시 A역 대기실로 컴백
                    if (s < ready) {
                        cntA++;
                        A.offer(ready);
                    }

                }
                // A에서 출발하면 반드시 B로 도착.
                B.offer(e + T * 60);
            }
            else {
                // B역이 비어져있으면
                if(B.isEmpty()) {
                    cntB++;
                }
                // B역에 기차가 있는데..
                else {
                    int ready = B.poll();
                    // 못쓰는 기차...출발시켜야한다!
                    if (s < ready) {
                        cntB++;
                        B.offer(ready);

                    }
                }
                A.offer(e + T * 60);
            }
        }

        return "Case #" + (tc + 1) + ": " + cntA + " " + cntB;
    }
    public static int calSecond(String time) {
        String[] t = time.split(":");
        // 문자열 -> 정수 Integer,parseInt
        int h = Integer.parseInt(t[0]);
        int m = Integer.parseInt(t[1]);

        return h * 3600 + m * 60;

    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Solution sol = new Solution();

        int TCs = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < TCs; tc++) {
            int T = Integer.parseInt(br.readLine());

            StringTokenizer st = new StringTokenizer(br.readLine());
            int NA = Integer.parseInt(st.nextToken());
            int NB = Integer.parseInt(st.nextToken());
            int N = NA + NB;

            String[][] plans = new String[N][2];
            for (int i = 0; i < N; i++) {
                String[] line = br.readLine().split(" ");
                plans[i][0] = line[0]; // departure
                plans[i][1] = line[1]; // arrival
            }

            String result = Solution.solution(tc, N, T, NA, NB, plans);
            System.out.println(result);
        }
    }
}