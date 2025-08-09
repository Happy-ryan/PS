import java.io.*;
import java.util.*;

class Solution {
    // 팀 결성 -> union find / (너비, 깊이) 탐색
    // 방향성 존재 -> union find 제거
    int n;
    int[] students;
    int[] visited;
    List<List<Integer>> adj = new ArrayList<>();
    List<List<Integer>> cycles = new ArrayList<>();
    List<Integer> path = new ArrayList<>();

    public int solution(int n, int[] students) {
        this.n = n;
        this.students = students;
        this.visited = new int[n + 1];
        // adj 초기화
        for (int i = 0; i < n + 1; i++) {
            adj.add(new ArrayList<>());
            ;
        }
        // 인접 리스트 구성
        for (int i = 1; i < n + 1; i++) {
            adj.get(i).add(students[i]);
        }
        // dfs  순회하며 팀 체크
        for (int cur = 1; cur < n + 1; cur++) {
            if (visited[cur] == 0) {
                dfs(cur);
            }
        }

        int val = n;
        for(List<Integer>  cycle: cycles) {
//            System.out.println(cycle);
            val -= cycle.size();
        }
        return val;
    }

    // 팀 만들기 cur -> nxt 이동하는 과정 중 만날 수 있는 상태
    // visited[nxt] = 0 : 방문하지 않음 -> dfs 진행 해야함
    // visited[nxt] = 1 : 방문중 - dfs 진행 중 ->
    // visited[nxt] = 2 : 탐색 완료한 곳 -> 따라서 dfs 진행할 필요 없음.
    // 1(0 -> 1) -> 2 / 2(0 -> 1) -> 3 / 3(0 -> 1) -5 / 5(0 -> 1) -> 2 / 2('1' => root => 종료 => '2')
    void dfs(int cur) {
        // 탐색시작
        visited[cur] = 1;
        path.add(cur);

        for (int nxt : adj.get(cur)) {
            // 방문한 적이 없을 때는 탐색
            if (visited[nxt] == 0) {
                dfs(nxt);
            }
            // 이미 다 돌았음. 볼 필요 없음.
            if (visited[nxt] == 2) {
                continue;
            }
            // nxt는 사이클의 일부.. path : a -> b -> [nxt -> ... -> cur] -> nxt
            if (visited[nxt] == 1) {
                int idx = path.indexOf(nxt);
                List<Integer> cycle = new ArrayList<>();
                for (int i = idx; i < path.size(); i++) {
                    cycle.add(path.get(i));
                }
                cycles.add(cycle);
            }
        }
        // dfs 탐색 종료
        visited[cur] = 2;
        path.remove(path.size() - 1);
    }
}

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < T; tc++) {
            int n = Integer.parseInt(br.readLine());
            int[] students = new int[n + 1];

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 1; i <= n; i++) {
                students[i] = Integer.parseInt(st.nextToken());
            }
            Solution solution = new Solution();
            System.out.println(solution.solution(n, students));
        }
    }
}

