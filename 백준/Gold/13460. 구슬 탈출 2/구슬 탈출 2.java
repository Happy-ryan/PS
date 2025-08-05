import java.util.*;

public class Main {
    static int n, m;
    static char[][] board;
    static int[] blank; // 구멍 위치
    static int[][][][] dist; // 방문 및 거리 기록

    static int[] dr = {0, 1, 0, -1}; // 오른쪽, 아래, 왼쪽, 위
    static int[] dc = {1, 0, -1, 0};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        board = new char[n][m];

        int[] red = new int[2];
        int[] blue = new int[2];
        blank = new int[2];

        for (int i = 0; i < n; i++) {
            String line = sc.next();
            for (int j = 0; j < m; j++) {
                board[i][j] = line.charAt(j);
                if (board[i][j] == 'R') {
                    red[0] = i;
                    red[1] = j;
                    board[i][j] = '.';
                }
                if (board[i][j] == 'B') {
                    blue[0] = i;
                    blue[1] = j;
                    board[i][j] = '.';
                }
                if (board[i][j] == 'O') {
                    blank[0] = i;
                    blank[1] = j;
                }
            }
        }

        System.out.println(bfs(red[0], red[1], blue[0], blue[1]));
    }

    static int bfs(int rr, int rc, int br, int bc) {
        dist = new int[n][m][n][m];
        for (int[][][] a : dist) {
            for (int[][] b : a) {
                for (int[] c : b) {
                    Arrays.fill(c, Integer.MAX_VALUE);
                }
            }
        }

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{rr, rc, br, bc});
        dist[rr][rc][br][bc] = 0;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r1 = cur[0], c1 = cur[1], r2 = cur[2], c2 = cur[3];
            int curDist = dist[r1][c1][r2][c2];

            if (curDist > 10) return -1;
            if (r1 == blank[0] && c1 == blank[1]) return curDist;

            for (int d = 0; d < 4; d++) {
                int[] next = moveBalls(r1, c1, r2, c2, d);
                int nr1 = next[0], nc1 = next[1], nr2 = next[2], nc2 = next[3];

                if (nr2 == blank[0] && nc2 == blank[1]) continue; // 파란 구슬이 구멍에 빠짐
                if (nr1 == -1) continue; // 둘 다 동시에 구멍에 빠짐

                if (dist[nr1][nc1][nr2][nc2] == Integer.MAX_VALUE) {
                    dist[nr1][nc1][nr2][nc2] = curDist + 1;
                    q.add(new int[]{nr1, nc1, nr2, nc2});
                }
            }
        }
        return -1;
    }

    static int[] moveBalls(int rr, int rc, int br, int bc, int dir) {
        int[] redMoved = move(rr, rc, dir);
        int[] blueMoved = move(br, bc, dir);

        int nrr = redMoved[0], nrc = redMoved[1];
        int nbr = blueMoved[0], nbc = blueMoved[1];

        // 둘 다 동시에 구멍에 빠짐
        if (nrr == blank[0] && nrc == blank[1] && nbr == blank[0] && nbc == blank[1]) {
            return new int[]{-1, -1, -1, -1};
        }

        // 같은 칸에 겹침 (구멍 제외)
        if (nrr == nbr && nrc == nbc) {
            if (nrr == blank[0] && nrc == blank[1]) {
                return new int[]{-1, -1, -1, -1};
            }
            // 이동 순서에 따라 보정
            if (dir == 0) { // 오른쪽
                if (rc > bc) nbc -= 1;
                else nrc -= 1;
            } else if (dir == 1) { // 아래
                if (rr > br) nbr -= 1;
                else nrr -= 1;
            } else if (dir == 2) { // 왼쪽
                if (rc < bc) nbc += 1;
                else nrc += 1;
            } else { // 위
                if (rr < br) nbr += 1;
                else nrr += 1;
            }
        }

        return new int[]{nrr, nrc, nbr, nbc};
    }

    static int[] move(int r, int c, int dir) {
        while (true) {
            int nr = r + dr[dir];
            int nc = c + dc[dir];
            if (board[nr][nc] == '#') break;
            r = nr;
            c = nc;
            if (r == blank[0] && c == blank[1]) break;
        }
        return new int[]{r, c};
    }
}
