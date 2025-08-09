import java.io.*;
import java.util.*;

class Solution {
    int n, delNode;
    int[] nodes;
    int[] visited;
    // 인접행렬
    List<List<Integer>> adj = new ArrayList<>();

    public int solution(int n, int[] nodes, int delNode) {
        this.n = n;
        this.delNode = delNode;
        this.nodes = nodes;
        this.visited = new int[n];

        // 인접행렬 초기화
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        // 인접행렬 생성
        int root = 0;
        for (int i = 0; i < n; i++) {
            if (nodes[i] != -1) {
                adj.get(nodes[i]).add(i);
            } else {
                root = i;
            }
        }

        // 루트 노드를 삭제하는 경우
        if (root == delNode) {
            return 0;
        }


        int cnt = dfs(root, -1);

        return cnt;
    }

    int dfs(int cur, int par) {
        int ret = 0;

        if (visited[cur] == 1) {
            return 0;
        }
        visited[cur] = 1;
        boolean hasChild = false;
        for (int nxt : adj.get(cur)) {
           // 삭제할 아이 만나면 탐색 금지! 
            if (nxt == delNode) {
                continue;
            }
            if (nxt != par) {
                ret += dfs(nxt, cur);
                hasChild = true;
            }
        }
        if (!hasChild) {
            ret++;
        }
        return ret;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] nodes = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nodes[i] = Integer.parseInt(st.nextToken());
        }

        int delNode = Integer.parseInt(br.readLine());

        Solution sol = new Solution();
        System.out.println(sol.solution(n, nodes, delNode));
    }
}
