import java.util.*;

public class Main {
    private static int n, m;
    private static char[][] board;
    private static int maxVal = 0;
    private static int[] dr = new int[]{-1, 1, 0, 0};
    private static int[] dc = new int[]{0, 0, -1, 1};
    private static List<Character> ans = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        n = sc.nextInt();
        m = sc.nextInt();
        // 개행 소비!
        sc.nextLine();

        board = new char[n][m];
        for (int i = 0; i < n; i++) {
            board[i] = sc.nextLine().toCharArray();
        }
        //  첫 번째 칸 포함!
        ans.add(board[0][0]);
        back(0, 0);
        System.out.print(maxVal);
    }

    private static void back(int r, int c) {
        maxVal = Math.max(maxVal, ans.size());
        for (int dir = 0; dir < 4; dir++) {
            int nr = r + dr[dir];
            int nc = c + dc[dir];
            if (inRange(nr, nc) && !ans.contains(board[nr][nc])) {
                ans.add(board[nr][nc]);
                back(nr, nc);
                ans.remove(ans.size() - 1);
            }
        }
    }

    private static boolean inRange(int r, int c) {
        return 0 <= r && r < n && 0 <= c && c < m;
    }

}