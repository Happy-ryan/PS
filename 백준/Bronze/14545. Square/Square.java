import java.io.*;

class Solution {
    public long solution(int N) {
        long res = 0;
        for (int i = 1; i <= N; i++) {
            res += (long) i * i;
        }
        return res;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine()); // 테스트 케이스 개수
        Solution sol = new Solution();

        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());
            System.out.println(sol.solution(N));
        }
    }
}