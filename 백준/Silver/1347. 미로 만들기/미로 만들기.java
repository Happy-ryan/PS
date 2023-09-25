import java.util.Scanner;

public class Main {
    static final int MAX_N = 200;
    static final int[] dr = {0, 1, 0, -1}; // 동남서북
    static final int[] dc = {1, 0, -1, 0};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String cmds = sc.next();

        int[][] board = new int[MAX_N][MAX_N];
        int cr = MAX_N / 2, cc = MAX_N / 2;
        int dir = 1; // 초기 방향은 남쪽

        board[cr][cc] = 1;
        for (char cmd: cmds.toCharArray()) {
            if (cmd == 'R') {
                dir = (dir + 1) % 4;
            } else if (cmd == 'L') {
                dir = (dir + 3) % 4;
            } else {
                int nr = cr + dr[dir], nc = cc + dc[dir];
                cr = nr; cc = nc;
                board[cr][cc] = 1;
            }
        }

        int maxR = 0, minR = MAX_N, maxC = 0, minC = MAX_N;
        for (int r = 0; r < MAX_N; r++) {
            for (int c = 0; c < MAX_N; c++) {
                if (board[r][c] == 1) {
                    maxR = Math.max(maxR, r);
                    minR = Math.min(minR, r);
                    maxC = Math.max(maxC, c);
                    minC = Math.min(minC, c);
                }
            }
        }

        for (int r = minR; r <= maxR; r++) {
            for (int c = minC; c <= maxC; c++) {
                if (board[r][c] == 0) {
                    System.out.print("#");
                } else {
                    System.out.print(".");
                }
            }
            System.out.println();
        }
    }
}