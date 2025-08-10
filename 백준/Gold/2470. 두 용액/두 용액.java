import java.io.*;
import java.util.*;

class Solution {
    public String solution(int N, int[] A) {
        List<Integer> squid = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            squid.add(A[i]);
        }
        Collections.sort(squid);

        int inf = Integer.MAX_VALUE;
        int r = N - 1;
        int answer = -inf;
        Result res = new Result(0, 0, -inf);

        // 1) sum <= 0 중 가장 큰 값
        for (int l = 0; l < N; l++) {
            while (l < r && squid.get(l) + squid.get(r) > 0) {
                r--;
            }

            if (l < r) {
                int sum = squid.get(l) + squid.get(r);
                if (sum <= 0 && sum > answer) {
                    answer = sum;
                    res = new Result(squid.get(l), squid.get(r), sum);
                }
            }
        }

        // 2) sum >= 0 중 가장 작은 값
        int l = 0;
        int answer1 = inf;
        Result res1 = new Result(0, 0, inf);

        for (r = N - 1; r > 0; r--) {
            while (l < r && squid.get(l) + squid.get(r) < 0) {
                l++;
            }

            if (l < r) {
                int sum = squid.get(l) + squid.get(r);
                if (sum >= 0 && sum < answer1) {
                    answer1 = sum;
                    res1 = new Result(squid.get(l), squid.get(r), sum);
                }
            }
        }

        // 절댓값이 더 작은 것을 선택
        if (Math.abs(res.answer) <= Math.abs(res1.answer)) {
            return res.num1 + " " + res.num2;
        } else {
            return res1.num1 + " " + res1.num2;
        }
    }

    class Result {
        int num1, num2, answer;

        public Result(int num1, int num2, int answer) {
            this.num1 = num1;
            this.num2 = num2;
            this.answer = answer;
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] A = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        Solution sol = new Solution();
        System.out.println(sol.solution(N, A));
    }
}