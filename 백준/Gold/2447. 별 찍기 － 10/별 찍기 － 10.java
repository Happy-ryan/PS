import java.util.*;

public class Main {
    private static int n;
    private static char[][] board;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        StringBuilder sb = new StringBuilder();

        n = sc.nextInt();
        board = new char[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = ' ';
            }
        }
        
        f(0, 0, n);
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sb.append(board[i][j]);
            }
            sb.append('\n');
        }

        System.out.print(sb);
    }

    private static void f(int r, int c, int w) {

        if (w == 3) {
            for (int i = r; i < r + 3; i++) {
                for (int j = c; j < c + 3; j++) {
                    if (i == r + 1 && j == c + 1) {
                        continue;
                    } 
                    board[i][j] = '*';
                }
            }
            return;
        }

        int d = w / 3;

        f(r, c, d);
        f(r, c + d, d);
        f(r, c + 2 * d, d);

        f(r + d, c, d);
        f(r + d, c + 2 * d, d);

        f(r + 2 * d, c, d);
        f(r + 2 * d, c + d, d);
        f(r + 2 * d, c + 2 * d, d);
    }
}