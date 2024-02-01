import java.util.*;

class Main
{	private static int n, m;
	private static int[][] board, dp;
	
	private static int[] dr = new int[]{-1, 1, 0, 0};
	private static int[] dc = new int[]{0, 0, -1, 1};
	
	public static void main (String[] args)
	{
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		
		board = new int[n][m];
		dp = new int[n][m];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				int x = sc.nextInt();
				board[i][j] = x;
				dp[i][j] = -1;
			}
		}
		
		System.out.print(dpf(n - 1, m - 1));
		
	}
	
	private static int dpf(int r, int c) {
		if (dp[r][c] != -1) {
			return dp[r][c];
		}
		
		int ret = 0;
		for (int d = 0; d < 4; d++) {
			int preR = r + dr[d];
			int preC = c + dc[d];
			if (inRange(preR, preC) && board[preR][preC] > board[r][c]) {
				ret += dpf(preR, preC);
			}
		}
		
		if (r == 0 && c == 0) {
			return 1;
		}
		
		dp[r][c] = ret;
		
		return ret;
	}
	
	private static boolean inRange(int r, int c) {
		return 0 <= r && r < n && 0 <= c && c < m;
	}
}