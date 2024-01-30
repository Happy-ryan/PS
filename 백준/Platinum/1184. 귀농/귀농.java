import java.util.*;

public class Main {

    private static int n;
    private static int[][] board;
    private static int[][] psum;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        board = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = sc.nextInt();
            }
        }

        psum = new int[n + 1][n + 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                psum[i + 1][j + 1] = board[i][j] + psum[i + 1][j] + psum[i][j + 1] - psum[i][j];
            }
        }

        int cnt = 0;
        // share 좌표는 (0,0) 에서 시작해 (n - 2, n - 2)까지!
        for (int shareR = 0; shareR < n - 1; shareR++) {
            for (int shareC = 0; shareC < n - 1; shareC++) {
                List<Integer> ans1 = new ArrayList<>();
                List<Integer> ans2 = new ArrayList<>();
                // 왼쪽 상단
                for (int topLeftR = 0; topLeftR <= shareR;  topLeftR++) {
                    for (int topLeftC = 0; topLeftC <= shareC; topLeftC++) {
                        // System.out.print(rangeSum(topLeftR, topLeftC, shareR, shareC) + " ");
                        ans1.add(rangeSum(topLeftR, topLeftC, shareR, shareC));
                    }
                }

                // 오른쪽 하단
                for (int bottomRigntR = shareR + 1; bottomRigntR < n; bottomRigntR++) {
                    for (int bottomRightC = shareC + 1; bottomRightC < n; bottomRightC++) {
                        // System.out.print(rangeSum(shareR + 1, shareC + 1, bottomRigntR, bottomRightC) + " ");
                        cnt += Collections.frequency(ans1,rangeSum(shareR + 1, shareC + 1, bottomRigntR, bottomRightC));
                    }
                }

                // 오른쪽 상단
                for (int topRightR = 0; topRightR <= shareR; topRightR++) {
                    for (int topRightC = shareC + 1; topRightC < n; topRightC++) {
                        // System.out.print(rangeSum(topRightR, shareC + 1, shareR, topRightC) + " ");
                        ans2.add(rangeSum(topRightR, shareC + 1, shareR, topRightC));
                    }
                }

                // 왼쪽 하단
                for (int bottomLeftR = shareR + 1; bottomLeftR < n; bottomLeftR++) {
                    for (int bottomLeftC = 0; bottomLeftC <= shareC; bottomLeftC++) {
                        // System.out.print(rangeSum(shareR + 1, bottomLeftC, bottomLeftR, shareC) + " ");
                        cnt += Collections.frequency(ans2, rangeSum(shareR + 1, bottomLeftC, bottomLeftR, shareC));
                    }
                }

            }
        }

        System.out.println(cnt);
    }
    // (r1, c1) - 좌측상단 / (r2, c2) - 우측하단
    // 0base좌표
    private static int rangeSum(int r1, int c1, int r2, int c2) {
        return psum[r2 + 1][c2 + 1] - psum[r1][c2 + 1] - psum[r2 + 1][c1] + psum[r1][c1];
    }
}
