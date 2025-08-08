import java.io.*;
import java.util.*;

class Solution {
    static int N, M;
    static int[][] board;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static int solution(int N, int M, int[][] board) {
        Solution.N = N;
        Solution.M = M;
        Solution.board = board;

        int t = 0;
        while (true) {
            IceResult result = findIces();
            List<int[]> ices = result.ices;
            int cnt = result.cnt;

            if (cnt == 0) {
                return 0;
            }
            if (cnt >= 2) {
                return t;
            }

            event(ices);
            t++;
        }
    }

    static boolean inRange(int r, int c) {
        return 0 <= r && r < N && 0 <= c && c < M;
    }

    static List<int[]> bfs(int r, int c, boolean[][] inQueue) {
        List<int[]> ices = new ArrayList<>();
        Queue<int[]> dq = new LinkedList<>();

        dq.offer(new int[]{r, c});
        ices.add(new int[]{r, c});
        inQueue[r][c] = true;

        while (!dq.isEmpty()) {
            int[] cur = dq.poll();
            int cr = cur[0];
            int cc = cur[1];

            for (int k = 0; k < 4; k++) {
                int nr = cr + dr[k];
                int nc = cc + dc[k];

                if (inRange(nr, nc) && !inQueue[nr][nc] && board[nr][nc] != 0) {
                    dq.offer(new int[]{nr, nc});
                    ices.add(new int[]{nr, nc});
                    inQueue[nr][nc] = true;
                }
            }
        }

        return ices;
    }

    static class IceResult {
        List<int[]> ices;
        int cnt;

        IceResult(List<int[]> ices, int cnt) {
            this.ices = ices;
            this.cnt = cnt;
        }
    }

    static IceResult findIces() {
        List<int[]> ices = new ArrayList<>();
        boolean[][] inQueue = new boolean[N][M];

        int cnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] == 0 || inQueue[i][j]) {
                    continue;
                }
                List<int[]> ice = bfs(i, j, inQueue);
                cnt++;
                ices.addAll(ice);
            }
        }

        return new IceResult(ices, cnt);
    }

    static void event(List<int[]> ices) {
        int[][] eventBoard = new int[N][M];

        // 각 얼음 위치에서 인접한 물의 개수만큼 감소값 누적
        for (int[] pos : ices) {
            int r = pos[0];
            int c = pos[1];

            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];

                if (inRange(nr, nc) && board[nr][nc] == 0) {
                    eventBoard[r][c] -= 1;  // 수정: 얼음 위치에 감소값 누적
                }
            }
        }

        // 실제 보드에 적용
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] > 0) {
                    board[i][j] += eventBoard[i][j];
                    board[i][j] = Math.max(0, board[i][j]);
                }
            }
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] board = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(Solution.solution(N, M, board));
        br.close();
    }
}