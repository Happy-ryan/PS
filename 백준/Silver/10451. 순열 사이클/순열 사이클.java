import java.io.*;
import java.util.*;

class Solution {
    static int N;
    static int cnt;
    static  boolean[] visited;
    static List<List<Integer>> adj;
    public static int solution(int N, int[] nums) {
        Solution.N = N;
        Solution.cnt = 0;
        Solution.visited = new boolean[N + 1];
        // dfs - 인접행렬
        Solution.adj = new ArrayList<>();
        // ArrayList 초기화 <- 필수!
        for (int i = 0; i < N + 1; i++) {
            adj.add(new ArrayList<>());
        }
        // 인접 리스트 구성
        for (int i = 1; i < N + 1; i++) {
            adj.get(i).add(nums[i - 1]); // nums 는 1base
        }

        List<Integer> cnts = new ArrayList<>();
        for (int node = 1; node < N + 1; node++) {
            cnt = 0;
            dfs(node);
            if (cnt != 0) {
                cnts.add(cnt);
            }
        }

        return cnts.size();

    }

    static void dfs(int node) {
        // 방문 이력 존재 -> 종료
        if (visited[node]) {
            return;
        }
        // 방문 이력 없을시 방문, 카운팅
        visited[node] = true;
        cnt++;
        // 인접 노트 방문
        for (int x : adj.get(node)) {
            dfs(x);
        }

    }

}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine()); // 테스트 케이스 개수

        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());

            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] nums = new int[N];

            for (int i = 0; i < N; i++) {
                nums[i] = Integer.parseInt(st.nextToken());
            }

            System.out.println(Solution.solution(N, nums));
        }

        br.close();

    }
}
