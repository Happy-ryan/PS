import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();
        // next()와 nextLine()차이 공부하기
        sc.nextLine(); 

        char[][] board = new char[n][m];
        for (int i = 0; i < n; i++) {
            // String -> char[]로 변경
            board[i] = sc.nextLine().toCharArray();
        }

        int[][] bwBoard = new int[n][m];
        for (int idx = 0; idx < n; idx++) {
            for (int i = 0; i < m; i++) {
                if (idx % 2 == 0) {
                    if (i % 2 == 0 && board[idx][i] != 'B') {
                        bwBoard[idx][i] = 1;
                    } else if (i % 2 != 0 && board[idx][i] != 'W') {
                        bwBoard[idx][i] = 1;
                    }
                } else {
                    if (i % 2 == 0 && board[idx][i] != 'W') {
                        bwBoard[idx][i] = 1;
                    } else if (i % 2 != 0 && board[idx][i] != 'B') {
                        bwBoard[idx][i] = 1;
                    }
                }
            }
        }

        int[][] psum = new int[n + 1][m + 1];
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                psum[r + 1][c + 1] = bwBoard[r][c] + psum[r][c + 1] + psum[r + 1][c] - psum[r][c];
            }
        }

        int ans = k * k;
        for (int topR = 0; topR <= n - k; topR++) {
            for (int topC = 0; topC <= m - k; topC++) {
                int bottomR = topR + k - 1;
                int bottomC = topC + k - 1;
                int bwCnt = psum[bottomR + 1][bottomC + 1] - psum[topR][bottomC + 1] - psum[bottomR + 1][topC] + psum[topR][topC];
                ans = Math.min(ans, Math.min(bwCnt, k * k - bwCnt));
            }
        }

        System.out.println(ans);
    }
}
