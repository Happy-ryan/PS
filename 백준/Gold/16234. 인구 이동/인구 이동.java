import java.io.*;
import java.util.*;

class Solution {
    static int N, L, R;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int[][] board;

    public static int solution(int N, int L, int R, int[][] board) {
        Solution.N = N;
        Solution.R = R;
        Solution.L = L;
        Solution.board = board;

        int day = 0;
        while (true) {
            boolean moved = oneDay();
            if (!moved) {  // 더 이상 인구 이동이 없으면 종료
                return day;
            }
            day++;
        }
    }

    // bfs - 연합 찾기
    static boolean inRange(int r, int c) {
        return 0 <= r && r < N && 0 <= c && c < N;
    }

    static List<int[]> bfs(int r, int c, boolean[][] inQueue) {
        List<int[]> union = new ArrayList<>();
        Queue<int[]> dq = new LinkedList<>();

        union.add(new int[]{r, c});
        dq.offer(new int[]{r, c});
        inQueue[r][c] = true;

        while (!dq.isEmpty()) {
            int[] cur = dq.poll();
            int cr = cur[0];
            int cc = cur[1];

            for (int k = 0; k < 4; k++) {
                int nr = cr + dr[k];
                int nc = cc + dc[k];
//                int val = Math.abs(board[nr][nc] - board[cr][cc]);
                if (inRange(nr, nc) && !inQueue[nr][nc] && (L <= Math.abs(board[nr][nc] - board[cr][cc]) && Math.abs(board[nr][nc] - board[cr][cc]) <= R)) {
                    union.add(new int[]{nr, nc});
                    dq.offer(new int[]{nr, nc});
                    inQueue[nr][nc] = true;
                }
            }
        }
        return union;
    }

    static boolean oneDay() {

        boolean[][] inQueue = new boolean[N][N];
        boolean hasMoved = false;

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (inQueue[r][c]) {
                    continue;
                }
                List<int[]> union = bfs(r, c, inQueue);
                if (union.size() > 1) {
                    move(union);
                    hasMoved = true;
                }
            }
        }
        return hasMoved;
    }

    static void move(List<int[]> union) {
        int cnt = union.size();
        int val = 0;
        for (int[] pos : union) {
            val += board[pos[0]][pos[1]];
        }

        val /= cnt;

        for (int[] pos : union) {
            board[pos[0]][pos[1]] = val;
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());

        int[][] board = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(Solution.solution(N, L, R, board));
        br.close();
    }
}