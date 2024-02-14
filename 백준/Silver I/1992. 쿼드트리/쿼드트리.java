import java.util.*;

public class Main {
    private static int n, m;
    private static char[][] board;
    private static StringBuilder ans = new StringBuilder();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        sc.nextLine();
        board = new char[n][n];
        for (int i = 0; i < n; i++) {
            board[i] = sc.nextLine().toCharArray();
        }

        compress(0, 0, n);
        System.out.print(ans);
    }

    private static boolean canCompress(int r, int c, int w) {
        char compressResult = board[r][c];
        for (int i = r; i < r + w; i++) {
            for (int j = c; j < c + w; j++) {
                if (board[i][j] != compressResult) {
                    return false;
                }
            }
        }
        return true;
    }

    private static void compress(int r, int c, int w) {
        if (canCompress(r, c, w)) {
            ans.append(board[r][c]);
            return;
        }

        ans.append('(');
        compress(r, c, w / 2);
        compress(r, c + w / 2, w / 2);
        compress(r + w / 2, c, w / 2);
        compress(r + w / 2, c + w / 2, w / 2);
        ans.append(')');
    }
}