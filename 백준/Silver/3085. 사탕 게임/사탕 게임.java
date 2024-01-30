import java.util.*;

public class Main {

    private static int n;
    private static char[][] board;

    private static int[] dr = new int[]{-1, 1, 0, 0};
    private static int[] dc = new int[]{0, 0, -1, 1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        // 왜 이래야해??
        sc.nextLine();
        board = new char[n][n];
        for (int i = 0; i < n; i++) {
            String row = sc.nextLine();
            for (int j = 0; j < n; j++) {
                board[i][j] = row.charAt(j);
            }
        }

        int maxCandy = 0;
        for (int cr = 0; cr < n; cr++) {
            for (int cc = 0; cc < n; cc++) {
                for (int d = 0; d < 4; d++) {
                    int nr = cr + dr[d];
                    int nc = cc + dc[d];
                    if (inRange(nr, nc)) {
                        // 인접한 곳끼리 swap
                        char tmp1 = board[cr][cc];
                        board[cr][cc] = board[nr][nc];
                        board[nr][nc] = tmp1;
                        maxCandy = Math.max(maxCandy, Math.max(rowBomb(), colBomb()));
                        // 원상복귀
                        char tmp2 = board[cr][cc];
                        board[cr][cc] = board[nr][nc];
                        board[nr][nc] = tmp2;
                    }
                }                
            }
        }

        System.out.println(maxCandy);
        
    }
    // 행에서 연속된 사탕의 수
    // 어떤 사탕이 연속되는지 알 필요는 없음!
    private static int rowBomb() {
        int maxRowCandy = 0;
        for (int i = 0; i < n; i++) {
            char startCandy = board[i][0];
            int rowCandy = 1;
            for (int j = 1; j < n; j++) {
                if (startCandy == board[i][j]) {
                    rowCandy++;
                }
                else {
                    startCandy = board[i][j];
                    rowCandy = 1;
                }
                maxRowCandy = Math.max(maxRowCandy, rowCandy);
            }
        }
        return maxRowCandy;
    }
    // 열에서 연속된 사탕의 수
    private static int colBomb() {
        int maxColCandy = 0;
        for (int j = 0; j < n; j++) {
            char startCandy = board[0][j];
            int colCandy = 1;
            for (int i = 1; i < n; i++) {
                if (startCandy == board[i][j]) {
                    colCandy++;
                }
                else {
                    startCandy = board[i][j];
                    colCandy = 1;
                }
            maxColCandy = Math.max(maxColCandy, colCandy);
            }
        }
        return maxColCandy;
    }

    private static boolean inRange(int r, int c) {
        return 0 <= r && r < n && 0 <= c && c < n;
    }

}